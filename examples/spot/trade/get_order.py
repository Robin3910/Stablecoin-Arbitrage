#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

# api_key, api_secret = get_api_key()
api_secret = "QuD20YF3W0oaBsXffIpnMnMzcyzoT9NSUOvbqyhw03718hUPQdmNAwGG8XzuAmzy"
api_key = "QSPznQMukvutuZIk01uevHZ9hYhCtXA3tLfSHsJGxEfJsnEOkEwGqvjVwC5MZM6N"


client = Client(api_key, api_secret, base_url="https://testnet.binance.vision")

try:
    response = client.get_order("BTCUSDT", orderId="15254631")
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
