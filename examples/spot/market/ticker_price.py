#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

spot_client = Client(base_url="https://testnet.binance.vision")

logging.info(spot_client.ticker_price("USDCUSDT"))
# logging.info(spot_client.ticker_price(symbols=["BTCUSDT", "BNBUSDT"]))
