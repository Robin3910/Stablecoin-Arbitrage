import time
from typing import Dict, Optional
from dataclasses import dataclass
from config import CONFIG
from binance.spot import Spot as Client
import logging
from logging.handlers import RotatingFileHandler
from binance.error import ClientError
import threading
from enum import Enum
import math
import requests

spot_client = Client(api_key=CONFIG["API_KEY"], api_secret=CONFIG["API_SECRET"])
balance_buffer = CONFIG["balance_buffer"]

def send_wx_notification(title, message):
    """
    发送微信通知
    
    Args:
        title: 通知标题
        message: 通知内容
    """
    try:
        mydata = {
            'text': title,
            'desp': message
        }
        requests.post(f'https://wx.xtuis.cn/{WX_TOKEN}.send', data=mydata)
        logger.info('发送微信消息成功')
    except Exception as e:
        logger.error(f'发送微信消息失败: {str(e)}')

# 配置日志
def setup_logger():
    logger = logging.getLogger('arbitrage')
    logger.setLevel(logging.INFO)
    
    # 创建 rotating file handler，最大文件大小为 10MB，保留 5 个备份文件
    handler = RotatingFileHandler('arbitrage.log', maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

logger = setup_logger()

class OrderStatus(Enum):
    NO_ORDER = "无订单"
    ENTRY_PLACED = "已挂入场单"
    WAITING_PROFIT = "等待止盈"

@dataclass
class OrderInfo:
    entry_order_id: Optional[str] = None    # 入场订单ID
    exit_order_id: Optional[str] = None     # 出场订单ID
    status: OrderStatus = OrderStatus.NO_ORDER  # 订单状态
    entry_price: float = 0.0                # 入场价格
    exit_price: float = 0.0                # 出场价格



class BalanceManager:
    def __init__(self):
        self.last_balance_check = 0  # 上次检查余额的时间
        self.last_deposit_check = 0  # 上次检查存款的时间

    def get_balance(self):
        response = spot_client.account()
        for balance in response["balances"]:
            if balance["asset"] == "USDT":
                return float(balance["free"]) + float(balance["locked"])
        return 0

    def redeem_simple_earn(self, amount: float):
        response = spot_client.redeem_flexible_product("USDT001", amount=amount, recvWindow=5000)
        return response

    def deposit_simple_earn(self, amount: float):
        try:
            response = spot_client.subscribe_flexible_product("USDT001", amount=amount, recvWindow=5000)
            logger.info(f"存入理财: {amount} USDT|response: {response}")
            send_wx_notification(title="存入理财", message=f"存入理财: {amount} USDT|response: {response}")
            # logger.info(response)
        except ClientError as error:
            logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def calculate_total_required_balance(self):
        """计算所有品种balance_buffer个interval所需的总资金"""
        total_required = 0
        for symbol, config in CONFIG["SYMBOLS"].items():
            # 获取当前价格
            try:
                current_price = float(spot_client.ticker_price(symbol)["price"])
                
                # 如果当前价格高于base_price，跳过该品种
                if current_price >= config["BASE_PRICE"]:
                    continue
                
                # 计算当前价格和base_price的差值（以格子数量计）
                price_diff = (config["BASE_PRICE"] - current_price) / config["PRICE_INTERVAL"]
                # 计算需要的总格子数（差值 + buffer）
                total_intervals = min(
                    price_diff + balance_buffer,
                    config["MAX_ORDERS"]  # 确保不超过最大订单数
                )
                # 向上取整，确保有足够的余额
                required_intervals = math.ceil(total_intervals)
                
                required_per_symbol = required_intervals * config["ORDER_AMOUNT"] * config["BASE_PRICE"]
                total_required += required_per_symbol
                
            except Exception as e:
                logger.error(f"计算{symbol}所需余额时发生错误: {e}")
                # 发生错误时使用最大可能值作为安全措施
                required_per_symbol = config["MAX_ORDERS"] * config["ORDER_AMOUNT"] * config["BASE_PRICE"]
                total_required += required_per_symbol
                
        return total_required

    def manage_balance(self):
        """管理账户余额，确保有足够的资金进行交易"""
        current_time = time.time()
        
        # 每30秒检查一次余额
        if current_time - self.last_balance_check >= 30:
            self.last_balance_check = current_time
            current_balance = self.get_balance()
            required_balance = self.calculate_total_required_balance()
            logger.info(f"当前余额: {current_balance} USDT|所需余额: {required_balance} USDT")
            if current_balance < required_balance:
                # 需要赎回的金额（多赎回10%作为缓冲）
                redeem_amount = round((required_balance - current_balance) * 1.1, 0)
                try:
                    response = self.redeem_simple_earn(amount=redeem_amount)
                    send_wx_notification(title="从理财赎回", message=f"从理财赎回: {redeem_amount} USDT|response: {response}")
                    logger.info(f"从理财赎回: {redeem_amount} USDT|response: {response}")
                except Exception as e:
                    logger.error(f"赎回理财失败: {e}")

        # 每天20点检查是否需要存入理财
        current_hour = time.localtime().tm_hour
        if current_hour == 20 and current_time - self.last_deposit_check >= 3600:  # 确保一小时内只检查一次
            self.last_deposit_check = current_time
            current_balance = self.get_balance()
            required_balance = self.calculate_total_required_balance()
            
            if current_balance > required_balance:
                # 将超出部分的90%存入理财（保留一些缓冲）
                deposit_amount = round((current_balance - required_balance) * 0.9, 0)
                try:
                    response = self.deposit_simple_earn(amount=deposit_amount)
                    logger.info(f"存入理财: {deposit_amount} USDT|response: {response}")
                except Exception as e:
                    logger.error(f"存入理财失败: {e}")

class UsdcArbitrage:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.config = CONFIG["SYMBOLS"][symbol]  # 获取该品种的具体配置
        self.position_map: Dict[float, OrderInfo] = {}

    # 批量获取订单
    def get_open_orders(self):
        try:
            response = spot_client.get_open_orders(self.symbol)
            # logger.info(response)
            return response
        except ClientError as error:
            logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def place_limit_order(self, price: float, amount: float, side: str) -> str:
        """
        下限价单（示例实现）
        """
        params = {
            "symbol": self.symbol,
            "side": side,
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": amount,
            "price": price,
        }

        try:
            response = spot_client.new_order(**params)
            if response:
                logger.info(f"下单成功: {response}|下单参数：{params}")
                return response["orderId"]
            # logger.info(response)
        except ClientError as error:
            logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        return None

    def check_order_status(self, order_id: str, order_list: list) -> bool:
        """
        从order_list中检查订单是否成交
        """
        for order in order_list:
            if str(order["orderId"]) == str(order_id):
                return order["status"] == "FILLED"
            
        # 如果在order_list中没找到订单,通过API查询订单状态
        try:
            order_status = spot_client.get_order(symbol=self.symbol, orderId=order_id)
            logger.info(f"查询订单状态: {order_status}")
            return order_status["status"] == "FILLED"
        except ClientError as error:
            logger.error(
                "查询订单状态出错. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        return False

    def get_current_price(self) -> float:
        """
        获取当前USDC价格
        """
        response = spot_client.ticker_price(self.symbol)
        return float(response["price"])

    def place_entry_orders(self, current_price: float):
        for i in range(self.config["MAX_ORDERS"]):
            price = math.floor((self.config["BASE_PRICE"] - i * self.config["PRICE_INTERVAL"]) * 10000) / 10000
            
            if price > current_price:
                continue
                
            if price <= self.config["BASE_PRICE"] - (balance_buffer * self.config["PRICE_INTERVAL"]):
                break
            
            # 只有在无订单状态下才需要挂入场单
            if price not in self.position_map or self.position_map[price].status == OrderStatus.NO_ORDER:
                order_info = OrderInfo()
                order_id = self.place_limit_order(price=price, amount=self.config["ORDER_AMOUNT"], side="BUY")
                order_info.entry_order_id = order_id
                order_info.entry_price = price
                order_info.exit_price = price + self.config["PROFIT_INTERVAL"]
                order_info.status = OrderStatus.ENTRY_PLACED
                self.position_map[price] = order_info

    def check_and_update_orders(self):
        current_price = self.get_current_price()
        order_list = self.get_open_orders()
        
        for price, order_info in list(self.position_map.items()):
            # 检查入场订单是否成交
            if order_info.status == OrderStatus.ENTRY_PLACED:
                if self.check_order_status(order_id=order_info.entry_order_id, order_list=order_list):
                    # 入场订单成交，设置止盈单
                    exit_order_id = self.place_limit_order(
                        price=order_info.exit_price, 
                        amount=self.config["ORDER_AMOUNT"], 
                        side="SELL"
                    )
                    order_info.exit_order_id = exit_order_id
                    order_info.status = OrderStatus.WAITING_PROFIT
                    logger.info(f"设置止盈单: {exit_order_id}")
            # 检查出场订单是否成交
            elif order_info.status == OrderStatus.WAITING_PROFIT:
                if self.check_order_status(order_id=order_info.exit_order_id, order_list=order_list):
                    send_wx_notification(title="止盈单成交", message=f"止盈单成交: {order_info.exit_order_id}")
                    # 止盈单成交，重置该点位
                    if current_price >= price:
                        # 如果当前价格高于入场价，可以重新布局入场单
                        new_entry_order_id = self.place_limit_order(
                            price=price, 
                            amount=self.config["ORDER_AMOUNT"], 
                            side="BUY"
                        )
                        self.position_map[price] = OrderInfo(
                            entry_order_id=new_entry_order_id,
                            entry_price=price,
                            exit_price=price + self.config["PROFIT_INTERVAL"],
                            status=OrderStatus.ENTRY_PLACED
                        )
                    else:
                        # 否则删除该点位信息
                        del self.position_map[price]

        self.place_entry_orders(current_price)
    def run(self):
        """
        运行策略
        """
        while True:
            try:
                self.check_and_update_orders()
                time.sleep(1)  # 每秒检查一次
            except Exception as e:
                logger.error(f"发生错误: {e}")
                time.sleep(1)


# 启动余额管理
def manage_balance_thread():
    while True:
        try:
            balance_manager.manage_balance()
            time.sleep(5)
        except Exception as e:
            logger.error(f"余额管理发生错误: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # 初始化余额管理器
    balance_manager = BalanceManager()
    arbitrage_instances = []

    # 初始化所有symbol的策略
    for symbol in CONFIG["SYMBOLS"].keys():
        arbitrage = UsdcArbitrage(symbol=symbol)
        arbitrage_instances.append(arbitrage)


    # 启动余额管理线程
    balance_thread = threading.Thread(target=manage_balance_thread, daemon=True)
    balance_thread.start()

    # 运行所有策略
    for arbitrage in arbitrage_instances:
        arbitrage.run()
