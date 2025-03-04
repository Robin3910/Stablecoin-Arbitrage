#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError

from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)
logger = logging.getLogger(__name__)

# api_key, api_secret = get_api_key()

api_key = "0yGQaN84eHkF72gTM6vVjz4Zf1WMG6aBZo0wzz5whR5pFqaui0Q7z6qr16pf6z6N"
api_secret = "PFIy1ygYl3ymNZKdzEf38UsqYkZz1ZmZnStQaGAuXeqisIZdBv2TsvJHthdefGZH"

client = Client(api_key, api_secret)

try:
    response = client.simple_account(recvWindow=5000)
    logger.info(response)
except ClientError as error:
    logger.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
