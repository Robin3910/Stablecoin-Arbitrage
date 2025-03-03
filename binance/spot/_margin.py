from binance.lib.utils import check_required_parameter
from binance.lib.utils import check_required_parameters
from binance.error import ParameterArgumentError


def borrow_repay(
    self, asset: str, isIsolated: str, symbol: str, amount, type: str, **kwargs
):
    """Margin account borrow/repay (MARGIN)

    Margin account borrow/repay(MARGIN)

    POST /sapi/v1/margin/borrow-repay

    https://developers.binance.com/docs/margin_trading/borrow-and-repay/Margin-Account-Borrow-Repay

    Args:
        asset (str): The asset being transferred, e.g., BTC.
        isIsolated (str): for isolated margin or not,"TRUE", "FALSE", default "FALSE".
        symbol (str): isolated symbol
        amount (float):
        type (str): BORROW or REPAY
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [asset, "asset"],
            [amount, "amount"],
            [type, "type"],
            [isIsolated, "isIsolated"],
            [symbol, "symbol"],
        ]
    )

    payload = {
        "asset": asset,
        "amount": amount,
        "type": type,
        "isIsolated": isIsolated,
        "symbol": symbol,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/margin/borrow-repay", payload)


def margin_all_assets(self, **kwargs):
    """Get All Margin Assets (MARKET_DATA)

    GET /sapi/v1/margin/allAssets

    https://developers.binance.com/docs/margin_trading/market-data/Get-All-Margin-Assets


    Keyword Args:
        asset (str, optional)
    """

    return self.limit_request("GET", "/sapi/v1/margin/allAssets", kwargs)


def margin_all_pairs(self, **kwargs):
    """Get All Margin Pairs (MARKET_DATA)

    GET /sapi/v1/margin/allPairs

    https://developers.binance.com/docs/margin_trading/market-data/Get-All-Cross-Margin-Pairs

    Keyword Args:
        symbol (str, optional)
    """

    return self.limit_request("GET", "/sapi/v1/margin/allPairs", kwargs)


def margin_pair_index(self, symbol: str, **kwargs):
    """Query Margin PriceIndex (MARKET_DATA)

    GET /sapi/v1/margin/priceIndex

    https://developers.binance.com/docs/margin_trading/market-data/Query-Margin-PriceIndex

    Args:
        symbol (str)
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.limit_request("GET", "/sapi/v1/margin/priceIndex", payload)


def new_margin_order(self, symbol: str, side: str, type: str, **kwargs):
    """Margin Account New Order (TRADE)

    Post a new order for margin account.

    POST /sapi/v1/margin/order

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-New-Order

    Args:
        symbol (str)
        side (str): BUY or SELL
        type (str)
    Keyword Args:
        quantity (float, optional)
        quoteOrderQty (float, optional)
        price (float, optional)
        stopPrice (float, optional): Used with STOP_LOSS,STOP_LOSS_LIMIT,TAKE_PROFIT and TAKE_PROFIT_LIMIT orders.
        newClientOrderId (str, optional): A unique id among open orders. Automatically generated if not sent.
        icebergQty (float, optional): Used with LIMIT, STOP_LOSS_LIMIT and TAKE_PROFIT_LIMIT to create an iceberg order.
        newOrderRespType (str, optional): Set the response JSON. ACK, RESULT or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
        sideEffectType (str, optional): NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY; default NO_SIDE_EFFECT.
        timeInForce (str, optional): GTC,IOC,FOK
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE" default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [type, "type"],
        ]
    )

    payload = {"symbol": symbol, "side": side, "type": type, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/order", payload)


def cancel_margin_order(self, symbol: str, **kwargs):
    """Margin Account Cancel Order (TRADE)

     Cancel an active order for margin account.

    DELETE /sapi/v1/margin/order

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-Cancel-Order

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        origClientOrderId (str, optional)
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", "/sapi/v1/margin/order", payload)


def margin_transfer_history(self, asset: str, **kwargs):
    """Get Cross Margin Transfer History (USER_DATA)

    GET /sapi/v1/margin/transfer

    https://developers.binance.com/docs/margin_trading/transfer/Get-Cross-Margin-Transfer-History

    Args:
        asset (str)
    Keyword Args:
        type (str, optional): Transfer Type: ROLL_IN, ROLL_OUT
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        isolatedSymbol (str, optional): Symbol in Isolated Margin
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/transfer", payload)


def borrow_repay_record(self, type: str, **kwargs):
    """Query borrow/repay records in Margin account (USER_DATA)

    GET /sapi/v1/margin/borrow-repay

    https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Borrow-Repay

    Args:
        type (str): BORROW or REPAY
    Keyword Args:
        asset (str, optional)
        isolatedSymbol (str, optional): isolated symbol
        txId (int, optional): the tranId in POST /sapi/v1/margin/loan
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(type, "type")
    payload = {"type": type, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/borrow-repay", payload)


def margin_interest_history(self, **kwargs):
    """Get Interest History (USER_DATA)

    GET /sapi/v1/margin/interestHistory

    https://developers.binance.com/docs/margin_trading/borrow-and-repay/Get-Interest-History

    Keyword Args:
        asset (str, optional)
        isolatedSymbol (str, optional): isolated symbol
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        archived (str, optional): Default: false. Set to true for archived data from 6 months ago
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/interestHistory", kwargs)


def margin_force_liquidation_record(self, **kwargs):
    """Get Force Liquidation Record (USER_DATA)

    GET /sapi/v1/margin/forceLiquidationRec

    https://developers.binance.com/docs/margin_trading/trade/Get-Force-Liquidation-Record

    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        startTime (int, optional)
        endTime (int, optional)
        current (int, optional): Currently querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/forceLiquidationRec", kwargs)


def margin_account(self, **kwargs):
    """Query Cross Margin Account Details (USER_DATA)

    GET /sapi/v1/margin/account

    https://developers.binance.com/docs/margin_trading/account/Query-Cross-Margin-Account-Details

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/account", kwargs)


def margin_order(self, symbol: str, **kwargs):
    """Query Margin Account's Order (USER_DATA)

    GET /sapi/v1/margin/order

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Order

    Args:
        symbol (str)
    Keyword Args:
        orderId (str, optional)
        origClientOrderId (str, optional)
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/order", payload)


def margin_open_orders(self, **kwargs):
    """Query Margin Account's Open Order (USER_DATA)

    GET /sapi/v1/margin/openOrders

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Open-Orders

    Keyword Args:
        symbol (str, optional)
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/openOrders", kwargs)


def margin_open_orders_cancellation(self, symbol: str, **kwargs):
    """Margin Account Cancel all Open Orders on a Symbol (USER_DATA)

    DELETE /sapi/v1/margin/openOrders

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-Cancel-All-Open-Orders

    Args:
        symbol (str)
    Keyword Args:
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", "/sapi/v1/margin/openOrders", payload)


def margin_all_orders(self, symbol: str, **kwargs):
    """Query Margin Account's All Orders (USER_DATA)

    GET /sapi/v1/margin/allOrders

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-Orders

    Args:
        symbol (str)
    Keyword Args:
        orderId (int, optional)
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500; max 500.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/allOrders", payload)


def margin_my_trades(self, symbol: str, **kwargs):
    """Query Margin Account's Trade List (USER_DATA)

    GET /sapi/v1/margin/myTrades

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Trade-List

    Args:
        symbol (str)
    Keyword Args:
        fromID (int, optional): TradeId to fetch from. Default gets most recent trades.
        isIsolated (str, optional): for isolated margin or not,"TRUE", "FALSE"，default "FALSE".
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default 500; max 500.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(symbol, "symbol")

    payload = {"symbol": symbol, **kwargs}

    return self.sign_request("GET", "/sapi/v1/margin/myTrades", payload)


def margin_max_borrowable(self, asset: str, **kwargs):
    """Query Max Borrow (USER_DATA)

    GET /sapi/v1/margin/maxBorrowable

    https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Max-Borrow

    Args:
        asset (str)
    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/maxBorrowable", payload)


def margin_max_transferable(self, asset: str, **kwargs):
    """Query Max Transfer-Out Amount (USER_DATA)

    GET /sapi/v1/margin/maxTransferable

    https://developers.binance.com/docs/margin_trading/transfer/Query-Max-Transfer-Out-Amount

    Args:
        asset (str)
    Keyword Args:
        isolatedSymbol (str, optional): isolated symbol
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/maxTransferable", payload)


def isolated_margin_account(self, **kwargs):
    """Query Isolated Margin Account Info (USER_DATA)

    GET /sapi/v1/margin/isolated/account

    https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Account-Info

    Keyword Args:
        symbols (str, optional): Max 5 symbols can be sent; separated by ",". e.g. "BTCUSDT,BNBUSDT,ADAUSDT"
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/isolated/account", kwargs)


def isolated_margin_all_pairs(self, **kwargs):
    """Get All Isolated Margin Symbol(USER_DATA)

    GET /sapi/v1/margin/isolated/allPairs

    https://developers.binance.com/docs/margin_trading/market-data/Get-All-Isolated-Margin-Symbol

    Keyword Args:
        symbol (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/isolated/allPairs", kwargs)


def toggle_bnbBurn(self, **kwargs):
    """Toggle BNB Burn On Spot Trade And Margin Interest (USER_DATA)

    POST /sapi/v1/bnbBurn

    https://developers.binance.com/docs/margin_trading/account/Toggle-BNB-Burn-On-Spot-Trade-And-Margin-Interest

    Keyword Args:
        spotBNBBurn (str, optional): "true" or "false"; Determines whether to use BNB to pay for trading fees on SPOT
        interestBNBBurn (str, optional): "true" or "false"; Determines whether to use BNB to pay for margin loan's interest
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("POST", "/sapi/v1/bnbBurn", kwargs)


def bnbBurn_status(self, **kwargs):
    """Get BNB Burn Status (USER_DATA)

    GET /sapi/v1/bnbBurn

    https://developers.binance.com/docs/margin_trading/account/Get-BNB-Burn-Status

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/bnbBurn", kwargs)


def margin_interest_rate_history(self, asset: str, **kwargs):
    """Get Margin Interest Rate History (USER_DATA)

    GET /sapi/v1/margin/interestRateHistory

    https://developers.binance.com/docs/margin_trading/borrow-and-repay/Query-Margin-Interest-Rate-History

    Args:
        asset (str)
    Keyword Args:
        vipLevel (str, optional): Default: user's vip level
        startTime (int, optional): Default: 7 days ago.
        endTime (int, optional): Default: present. Maximum range: 1 month.
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameter(asset, "asset")
    payload = {"asset": asset, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/interestRateHistory", payload)


def new_margin_oco_order(
    self,
    symbol: str,
    side: str,
    quantity: float,
    price: float,
    stopPrice: float,
    **kwargs
):
    """Margin Account New OCO (TRADE)

    Send in a new OCO for a margin account

    POST /sapi/v1/margin/order/oco

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-New-OCO

    Args:
        symbol (str)
        side (str)
        quantity (float)
        price (float)
        stopPrice (float)

    Keyword Args:
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        listClientOrderId (str, optional): A unique Id for the entire orderList
        limitClientOrderId (str, optional): A unique Id for the limit order
        limitIcebergQty (float, optional)
        stopClientOrderId (str, optional): A unique Id for the stop loss/stop loss limit leg
        stopLimitPrice (float, optional): If provided, stopLimitTimeInForce is required
        stopIcebergQty (float, optional)
        stopLimitTimeInForce (str, optional): Valid values are GTC/FOK/IOC
        newOrderRespType (str, optional): Set the response JSON
        sideEffectType (str, optional): NO_SIDE_EFFECT, MARGIN_BUY, AUTO_REPAY,AUTO_BORROW_REPAY; default NO_SIDE_EFFECT
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters(
        [
            [symbol, "symbol"],
            [side, "side"],
            [quantity, "quantity"],
            [price, "price"],
            [stopPrice, "stopPrice"],
        ]
    )
    payload = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "price": price,
        "stopPrice": stopPrice,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/margin/order/oco", payload)


def cancel_margin_oco_order(
    self, symbol, orderListId: int = None, listClientOrderId: str = None, **kwargs
):
    """Margin Account Cancel OCO (TRADE)

    Cancel an entire Order List for a margin account.

    DELETE /sapi/v1/margin/orderList

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-Cancel-OCO

    Args:
        symbol (str)
        orderListId (int, optional): Either orderListId or listClientOrderId must be provided
        listClientOrderId (str, optional): Either orderListId or listClientOrderId must be provided
    Keyword Args:
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        newClientOrderId (str, optional): Used to uniquely identify this cancel. Automatically generated by default.
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")
    payload = {
        "symbol": symbol,
        "orderListId": orderListId,
        "listClientOrderId": listClientOrderId,
        **kwargs,
    }
    return self.sign_request("DELETE", "/sapi/v1/margin/orderList", payload)


def get_margin_oco_order(
    self, orderListId: int = None, origClientOrderId: str = None, **kwargs
):
    """Query Margin Account's OCO (USER_DATA)

    Retrieves a specific OCO based on provided optional parameters

    GET /sapi/v1/margin/orderList

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-OCO

    Args:
        orderListId (int, optional): Either orderListId or origClientOrderId must be provided
        origClientOrderId (str, optional): Either orderListId or origClientOrderId must be provided.
    Keyword Args:
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        symbol (str, optional): Mandatory for isolated margin, not supported for cross margin
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    if kwargs.get("isIsolated"):
        check_required_parameter(kwargs.get("symbol"), "symbol")
    payload = {
        "orderListId": orderListId,
        "origClientOrderId": origClientOrderId,
        **kwargs,
    }
    return self.sign_request("GET", "/sapi/v1/margin/orderList", payload)


def get_margin_oco_orders(self, **kwargs):
    """Query Margin Account's all OCO (USER_DATA)

    Retrieves all OCO for a specific margin account based on provided optional parameters

    GET /sapi/v1/margin/allOrderList

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-All-OCO

    Keyword Args:
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE"，default "FALSE"
        symbol (str, optional): Mandatory for isolated margin, not supported for cross margin
        fromId (int, optional): If supplied, neither startTime or endTime can be provided
        startTime (int, optional)
        endTime (int, optional)
        limit (int, optional): Default Value: 500; Max Value: 1000
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    if kwargs.get("isIsolated"):
        check_required_parameter(kwargs.get("symbol"), "symbol")
    if kwargs.get("fromId") and (kwargs.get("startTime") or kwargs.get("endTime")):
        raise ParameterArgumentError(
            "If fromId is supplied, neither startTime or endTime can be provided."
        )
    return self.sign_request("GET", "/sapi/v1/margin/allOrderList", {**kwargs})


def get_margin_open_oco_orders(self, **kwargs):
    """Query Margin Account's Open OCO (USER_DATA)

    GET /sapi/v1/margin/openOrderList

    https://developers.binance.com/docs/margin_trading/trade/Query-Margin-Account-Open-OCO

    Keyword Args:
        isIsolated (str, optional): For isolated margin or not "TRUE", "FALSE" default "FALSE"
        symbol (str, optional): Mandatory for isolated margin, not supported for cross margin
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    if kwargs.get("isIsolated"):
        check_required_parameter(kwargs.get("symbol"), "symbol")
    return self.sign_request("GET", "/sapi/v1/margin/openOrderList", {**kwargs})


def cancel_isolated_margin_account(self, symbol: str, **kwargs):
    """Disable Isolated Margin Account (TRADE)
    Disable isolated margin account for a specific symbol. Each trading pair can only be deactivated once every 24 hours.

    DELETE /sapi/v1/margin/isolated/account

    https://developers.binance.com/docs/margin_trading/account/Disable-Isolated-Margin-Account

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("DELETE", "/sapi/v1/margin/isolated/account", payload)


def enable_isolated_margin_account(self, symbol: str, **kwargs):
    """Enable Isolated Margin Account (TRADE)
    Enable isolated margin account for a specific symbol (Only supports activation of previously disabled accounts).

    POST /sapi/v1/margin/isolated/account

    https://developers.binance.com/docs/margin_trading/account/Enable-Isolated-Margin-Account

    Args:
        symbol (str)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/isolated/account", payload)


def isolated_margin_account_limit(self, **kwargs):
    """Query Enabled Isolated Margin Account Limit (USER_DATA)
    Query enabled isolated margin account limit.

    GET /sapi/v1/margin/isolated/accountLimit

    https://developers.binance.com/docs/margin_trading/account/Query-Enabled-Isolated-Margin-Account-Limit

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/margin/isolated/accountLimit", kwargs)


def margin_fee(self, **kwargs):
    """Query Cross Margin Fee Data (USER_DATA)
    Get cross margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

    GET /sapi/v1/margin/crossMarginData

    https://developers.binance.com/docs/margin_trading/account/Query-Cross-Margin-Fee-Data

    Keyword Args:
        vipLevel (int, optional): User's current specific margin data will be returned if vipLevel is omitted
        coin (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/margin/crossMarginData", kwargs)


def isolated_margin_fee(self, **kwargs):
    """Query Isolated Margin Fee Data (USER_DATA)
    Get isolated margin fee data collection with any vip level or user's current specific data as https://www.binance.com/en/margin-fee

    GET /sapi/v1/margin/isolatedMarginData

    https://developers.binance.com/docs/margin_trading/account/Query-Isolated-Margin-Fee-Data

    Keyword Args:
        vipLevel (int, optional): User's current specific margin data will be returned if vipLevel is omitted
        symbol (str, optional)
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/margin/isolatedMarginData", kwargs)


def isolated_margin_tier(self, symbol: str, **kwargs):
    """Query Isolated Margin Tier Data (USER_DATA)
    Get isolated margin tier data collection with any tier as https://www.binance.com/en/margin-data

    GET /sapi/v1/margin/isolatedMarginTier

    https://developers.binance.com/docs/margin_trading/market-data/Query-Isolated-Margin-Tier-Data

    Args:
        symbol (str)
    Keyword Args:
        tier (int, optional): All margin tier data will be returned if tier is omitted
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(symbol, "symbol")
    payload = {"symbol": symbol, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/isolatedMarginTier", payload)


def margin_order_usage(self, **kwargs):
    """Query Current Margin Order Count Usage (TRADE)
    Displays the user's current margin order count usage for all intervals.

    GET /sapi/v1/margin/rateLimit/order

    https://developers.binance.com/docs/margin_trading/trade/Query-Current-Margin-Order-Count-Usage

    Keyword Args:
        isIsolated (str, optional): for isolated margin or not, "TRUE", "FALSE", default "FALSE"
        symbol (str, optional): isolated symbol, mandatory for isolated margin
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    return self.sign_request("GET", "/sapi/v1/margin/rateLimit/order", kwargs)


def summary_of_margin_account(self, **kwargs):
    """Get Summary of Margin account (USER_DATA)
    Get personal margin level information

    GET /sapi/v1/margin/tradeCoeff

    https://developers.binance.com/docs/margin_trading/account/Get-Summary-Of-Margin-Account

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/margin/tradeCoeff", kwargs)


def cross_margin_collateral_ratio(self):
    """Cross margin collateral ratio (MARKET_DATA)


    Weight(IP): 100

    GET /sapi/v1/margin/crossMarginCollateralRatio

    https://developers.binance.com/docs/margin_trading/market-data/Cross-margin-collateral-ratio

    """

    url_path = "/sapi/v1/margin/crossMarginCollateralRatio"
    return self.limit_request("GET", url_path)


def get_small_liability_exchange_coin_list(self, **kwargs):
    """Get Small Liability Exchange Coin List (USER_DATA)

    Query the coins which can be small liability exchange

    Weight(UID): 100

    GET /sapi/v1/margin/exchange-small-liability

    https://developers.binance.com/docs/margin_trading/trade/Get-Small-Liability-Exchange-Coin-List

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    url_path = "/sapi/v1/margin/exchange-small-liability"
    return self.sign_request("GET", url_path, {**kwargs})


def get_small_liability_exchange_history(self, current: int, size: int, **kwargs):
    """Get Small Liability Exchange History (USER_DATA)

    Get Small liability Exchange History

    Weight(UID): 100

    GET /sapi/v1/margin/exchange-small-liability-history

    https://developers.binance.com/docs/margin_trading/trade/Get-Small-Liability-Exchange-History

    Args:
        current (int, optional): Current querying page. Start from 1. Default:1
        size (int, optional): Default:10 Max:100
    Keyword Args:
        startTime (int, optional): UTC timestamp in ms
        endTime (int, optional): UTC timestamp in ms
        recvWindow (int, optional): The value cannot be greater than 60000
    """

    check_required_parameters([[current, "current"], [size, "size"]])
    payload = {"current": current, "size": size, **kwargs}
    url_path = "/sapi/v1/margin/exchange-small-liability-history"
    return self.sign_request("GET", url_path, payload)


def get_a_future_hourly_interest_rate(self, assets: str, isIsolated: bool, **kwargs):
    """Get a future hourly interest rate (USER_DATA)

    Get user the next hourly estimate interest

    Weight(UID): 100

    GET /sapi/v1/margin/next-hourly-interest-rate

    https://developers.binance.com/docs/margin_trading/borrow-and-repay/Get-a-future-hourly-interest-rate

    Args:
        assets (str, optional): List of assets, separated by commas, up to 20
        isIsolated (IsIsolated, optional): for isolated margin or not, "TRUE", "FALSE"
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[assets, "assets"], [isIsolated, "isIsolated"]])

    if isIsolated:
        isIsolated = "TRUE"
    else:
        isIsolated = "FALSE"
    params = {"assets": assets, "isIsolated": isIsolated, **kwargs}
    url_path = "/sapi/v1/margin/next-hourly-interest-rate"
    return self.sign_request("GET", url_path, params)


def adjust_cross_margin_max_leverage(self, maxLeverage: int, **kwargs):
    """Adjust cross margin max leverage (USER_DATA)

    Adjust cross margin max leverage

    Weight(IP): 3000

    POST /sapi/v1/margin/max-leverage

    https://developers.binance.com/docs/margin_trading/account/Adjust-Cross-Margin-Max-Leverage

    Args:
        maxLeverage (int)
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(maxLeverage, "maxLeverage")

    params = {"maxLeverage": maxLeverage, **kwargs}
    url_path = "/sapi/v1/margin/max-leverage"
    return self.sign_request("POST", url_path, params)


def margin_available_inventory(self, type: str, **kwargs):
    """Query Margin Available Inventory (USER_DATA)

    GET /sapi/v1/margin/available-inventory

    https://developers.binance.com/docs/margin_trading/market-data/Query-margin-avaliable-inventory

    Args:
        type (str): "MARGIN", "ISOLATED"
    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameter(type, "type")
    payload = {"type": type, **kwargs}
    return self.sign_request("GET", "/sapi/v1/margin/available-inventory", payload)


def margin_manual_liquidation(self, type: str, **kwargs):
    """Margin manual liquidation (MARGIN)

    POST /sapi/v1/margin/manual-liquidation

    https://developers.binance.com/docs/margin_trading/trade/Margin-Manual-Liquidation

    Args:
        type (str): "MARGIN", "ISOLATED"
    Keyword Args:
        symbol (str, optional): When type selects ISOLATED, symbol must be filled in
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    check_required_parameters([[type, "type"]])
    payload = {"type": type, **kwargs}
    return self.sign_request("POST", "/sapi/v1/margin/manual-liquidation", payload)


def margin_new_oto_order(
    self,
    symbol: str,
    workingType: str,
    workingSide: str,
    workingPrice: float,
    workingQuantity: float,
    pendingType: str,
    pendingSide: str,
    pendingQuantity: float,
    **kwargs
):
    """Margin Account New OTO (TRADE)

    Post a new OTOCO order for margin account

    Weight(UID): 6

    POST /sapi/v1/margin/order/oto

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-New-OTO

    Args:
        symbol (str)
        workingType (str)
        workingSide (str)
        workingPrice (float)
        workingQuantity (float)
        pendingType (str)
        pendingSide (str)
        pendingQuantity (float)
    Keyword Args:
        isIsolated (str, optional): for isolated margin or not: "TRUE", "FALSE". Default: "FALSE"
        listClientOrderId (str, optional): Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.
        newOrderRespType (str, optional): Set the response JSON. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.
        sideEffectType (str, optional): `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY` or `AUTO_BORROW_REPAY`
        selfTradePreventionMode (str, optional): The allowed enums is dependent on what is configured on the symbol. The possible supported values are `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`
        autoRepayAtCancel (bool, optional): Only when MARGIN_BUY order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true
        workingClientOrderId (str, optional): Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
        workingIcebergQty (float, optional): This can only be used if `workingTimeInForce` is `GTC`.
        workingTimeInForce (str, optional): `GTC`, `IOC` or `FOK`
        pendingClientOrderId (str, optional): Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent.
        pendingPrice (float, optional)
        pendingStopPrice (float, optional)
        pendingTrailingDelta (float, optional)
        pendingIcebergQty (float, optional): This can only be used if `pendingTimeInForce` is `GTC`.
        pendingTimeInForce (str, optional): `GTC`, `IOC` or `FOK`
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [workingType, "workingType"],
            [workingSide, "workingSide"],
            [workingPrice, "workingPrice"],
            [workingQuantity, "workingQuantity"],
            [pendingType, "pendingType"],
            [pendingSide, "pendingSide"],
            [pendingQuantity, "pendingQuantity"],
        ]
    )
    payload = {
        "symbol": symbol,
        "workingType": workingType,
        "workingSide": workingSide,
        "workingPrice": workingPrice,
        "workingQuantity": workingQuantity,
        "pendingType": pendingType,
        "pendingSide": pendingSide,
        "pendingQuantity": pendingQuantity,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/margin/order/oto", payload)


def margin_new_otoco_order(
    self,
    symbol: str,
    workingType: str,
    workingSide: str,
    workingPrice: float,
    workingQuantity: float,
    pendingSide: str,
    pendingQuantity: float,
    pendingAboveType: str,
    **kwargs
):
    """Margin Account New OTOCO (TRADE)

    Post a new OTOCO order for margin account

    Weight(UID): 6

    POST /sapi/v1/margin/order/otoco

    https://developers.binance.com/docs/margin_trading/trade/Margin-Account-New-OTOCO

    Args:
        symbol (str)
        workingType (str)
        workingSide (str)
        workingPrice (float)
        workingQuantity (float)
        pendingSide (str)
        pendingQuantity (float)
        pendingAboveType (str)
    Keyword Args:
        isIsolated (str, optional): for isolated margin or not: "TRUE", "FALSE". Default: "FALSE"
        sideEffectType (str, optional): `NO_SIDE_EFFECT`, `MARGIN_BUY`, `AUTO_REPAY` or `AUTO_BORROW_REPAY`
        autoRepayAtCancel (bool, optional): Only when `MARGIN_BUY` order takes effect, true means that the debt generated by the order needs to be repay after the order is cancelled. The default is true
        listClientOrderId (str, optional): Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.
        newOrderRespType (str, optional): Format of the JSON response.
        selfTradePreventionMode (str, optional): The allowed enums is dependent on what is configured on the symbol. The possible supported values are `EXPIRE_TAKER`, `EXPIRE_MAKER`, `EXPIRE_BOTH`, `NONE`
        workingClientOrderId (str, optional): Arbitrary unique ID among open orders for the working order. Automatically generated if not sent.
        workingIcebergQty (float, optional): This can only be used if `workingTimeInForce` is `GTC`.
        workingTimeInForce (str, optional): `GTC`, `IOC` or `FOK`
        pendingAboveClientOrderId (str, optional): Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent.
        pendingAbovePrice (float, optional)
        pendingAboveStopPrice (float, optional)
        pendingAboveTrailingDelta (float, optional)
        pendingAboveIcebergQty (float, optional): This can only be used if `pendingAboveTimeInForce` is `GTC`.
        pendingAboveTimeInForce (str, optional)
        pendingBelowType (str, optional): Supported values: `LIMIT_MAKER`, `STOP_LOSS`, and `STOP_LOSS_LIMIT`
        pendingBelowClientOrderId (str, optional): Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent.
        pendingBelowPrice (float, optional)
        pendingBelowStopPrice (float, optional)
        pendingBelowTrailingDelta (float, optional)
        pendingBelowIcebergQty (float, optional): This can only be used if `pendingBelowTimeInForce` is `GTC`.
        pendingBelowTimeInForce (str, optional)
    """
    check_required_parameters(
        [
            [symbol, "symbol"],
            [workingType, "workingType"],
            [workingSide, "workingSide"],
            [workingPrice, "workingPrice"],
            [workingQuantity, "workingQuantity"],
            [pendingSide, "pendingSide"],
            [pendingQuantity, "pendingQuantity"],
            [pendingAboveType, "pendingAboveType"],
        ]
    )
    payload = {
        "symbol": symbol,
        "workingType": workingType,
        "workingSide": workingSide,
        "workingPrice": workingPrice,
        "workingQuantity": workingQuantity,
        "pendingSide": pendingSide,
        "pendingQuantity": pendingQuantity,
        "pendingAboveType": pendingAboveType,
        **kwargs,
    }
    return self.sign_request("POST", "/sapi/v1/margin/order/otoco", payload)


def liability_coin_leverage_bracket(self, **kwargs):
    """Query Liability Coin Leverage Bracket in Cross Margin Pro Mode(MARKET_DATA)

    GET /sapi/v1/margin/leverageBracket

    https://developers.binance.com/docs/margin_trading/market-data/Query-Liability-Coin-Leverage-Bracket-in-Cross-Margin-Pro-Mode

    Keyword Args:
        recvWindow (int, optional): The value cannot be greater than 60000
    """
    return self.sign_request("GET", "/sapi/v1/margin/leverageBracket", kwargs)
