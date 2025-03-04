import time
from typing import Dict, Optional
from dataclasses import dataclass
from config import CONFIG
from binance.spot import Spot as Client
import logging
from logging.handlers import RotatingFileHandler
from binance.error import ClientError

spot_client = Client(api_key=CONFIG["API_KEY"], api_secret=CONFIG["API_SECRET"])

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

@dataclass
class OrderInfo:
    entry_order_id: Optional[str] = None    # 入场订单ID
    exit_order_id: Optional[str] = None     # 出场订单ID
    waiting_profit: bool = False            # 是否在等待止盈
    entry_price: float = 0.0                # 入场价格
    exit_price: float = 0.0                # 出场价格

class UsdcArbitrage:
    def __init__(self):
        self.position_map: Dict[float, OrderInfo] = {}  # 用价格作为key的订单信息map
        
    def place_limit_order(self, symbol: str, price: float, amount: float, side: str) -> str:
        """
        下限价单（示例实现）
        """
        params = {
            "symbol": symbol,
            "side": side,
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": amount,
            "price": price,
        }

        try:
            response = spot_client.new_order(**params)
            if response:
                return response["orderId"]
            logger.info(response)
        except ClientError as error:
            logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        return None

    def check_order_status(self, symbol: str, order_id: str) -> bool:
        """
        检查订单是否成交
        """

        try:
            response = spot_client.get_order(symbol, orderId=order_id)
            logger.info(response)
            if response["status"] == "FILLED":
                return True
        except ClientError as error:
            logger.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
        return False

    def get_current_price(self) -> float:
        """
        获取当前USDC价格
        """
        response = spot_client.ticker_price("USDCUSDT")
        return float(response["price"])


    def place_entry_orders(self, current_price: float):
        """
        根据当前价格布置入场订单
        """
        for i in range(CONFIG["MAX_ORDERS"]):
            price = CONFIG["BASE_PRICE"] - i * CONFIG["PRICE_INTERVAL"]
            if price > current_price:
                continue
                
            # 如果该价格点位不存在或者没有在等待止盈
            if price not in self.position_map or not self.position_map[price].waiting_profit:
                order_info = OrderInfo()
                order_id = self.place_limit_order(symbol="USDCUSDT", price=price, amount=CONFIG["ORDER_AMOUNT"], side="BUY")
                order_info.entry_order_id = order_id
                order_info.entry_price = price
                order_info.exit_price = price + CONFIG["PROFIT_INTERVAL"]
                self.position_map[price] = order_info

    def check_and_update_orders(self):
        """
        检查并更新订单状态
        """
        current_price = self.get_current_price()
        
        # 检查所有订单点位
        for price, order_info in list(self.position_map.items()):
            # 检查入场订单是否成交
            if order_info.entry_order_id and not order_info.waiting_profit:
                if self.check_order_status(symbol="USDCUSDT", order_id=order_info.entry_order_id):
                    # 入场订单成交，设置止盈单
                    exit_order_id = self.place_limit_order(
                        symbol="USDCUSDT",
                        price=order_info.exit_price, 
                        amount=CONFIG["ORDER_AMOUNT"], 
                        side="SELL"
                    )
                    order_info.exit_order_id = exit_order_id
                    order_info.waiting_profit = True
                    logger.info(f"设置止盈单: {exit_order_id}")
            # 检查出场订单是否成交
            elif order_info.exit_order_id and order_info.waiting_profit:
                if self.check_order_status(symbol="USDCUSDT", order_id=order_info.exit_order_id):
                    # 止盈单成交，重置该点位
                    if current_price > price:
                        # 如果当前价格高于入场价，可以重新布局入场单
                        new_entry_order_id = self.place_limit_order(
                            symbol="USDCUSDT",
                            price=price, 
                            amount=CONFIG["ORDER_AMOUNT"], 
                            side="BUY"
                        )
                        self.position_map[price] = OrderInfo(
                            entry_order_id=new_entry_order_id,
                            entry_price=price,
                            exit_price=price + CONFIG["PROFIT_INTERVAL"]
                        )
                    else:
                        # 否则删除该点位信息
                        del self.position_map[price]

        # 检查是否需要布置新的入场订单
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
                print(f"发生错误: {e}")
                time.sleep(1)

if __name__ == "__main__":
    arbitrage = UsdcArbitrage()
    arbitrage.run()
