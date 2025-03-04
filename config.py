# API配置
CONFIG = {
    "API_KEY": "",
    "API_SECRET": "",
    "balance_buffer": 5, # 预留5个区间的资金进行开仓
    "WX_TOKEN": "",

    # 交易配置
    "SYMBOLS": {
        # "USDCUSDT": {
        #     "BASE_PRICE": 1.0000,
        #     "MAX_ORDERS": 5,
        #     "ORDER_AMOUNT": 10,
        #     "PRICE_INTERVAL": 0.0001,
        #     "PROFIT_INTERVAL": 0.0001
        # },
        "FDUSDUSDT": {
            "BASE_PRICE": 0.9984,
            "MAX_ORDERS": 10,
            "ORDER_AMOUNT": 10,
            "PRICE_INTERVAL": 0.0001,
            "PROFIT_INTERVAL": 0.0001
        }
    }
}

