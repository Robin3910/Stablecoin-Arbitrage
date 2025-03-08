# Binance Stablecoin Arbitrage Trading Bot for USDC/USDT, FDUSD/USDT

[English](README.md#binance-stablecoin-grid-trading-bot-for-usdcusdt-fdusdusdt) | [中文](README_CN.md)

This is an automated grid trading bot for stablecoins based on the Binance API, supporting multi-pair grid trading and automated financial management.

The goal is to achieve stable, risk-free returns through stablecoin grid arbitrage, aiming for an annual return of 15%.
Additionally, it utilizes financial management features to automatically transfer funds to savings products when arbitrage opportunities are not available.

## Main Features

- Support for multiple trading pairs simultaneously
- Automatic account balance management with dynamic fund allocation between trading and savings
- Dynamic adjustment of grid base price
- Automatic WeChat notifications
- Comprehensive logging system

## Dependencies

```bash
pip install binance-connector
pip install requests
```

## Configuration

Create a `config.py` file with the following configuration before running:

```python
CONFIG = {
    "API_KEY": "Your API KEY",
    "API_SECRET": "Your API SECRET",
    "balance_buffer": 5,  # Balance buffer (number of grids)
    "SYMBOLS": {
        "USDCUSDT": {  # Trading pair configuration
            "BASE_PRICE": 1.0,  # Base price
            "PRICE_INTERVAL": 0.0001,  # Grid interval
            "ORDER_AMOUNT": 100,  # Order amount per grid
            "PROFIT_INTERVAL": 0.0001,  # Take profit interval
            "MAX_ORDERS": 10  # Maximum number of orders
        },
        # Add more trading pairs...
    }
}
```

## Running

```bash
python arbitrage.py
```

## Key Features

1. **Multi-Pair Support**
   - Run grid strategies for multiple trading pairs simultaneously
   - Independent parameter configuration for each pair

2. **Smart Fund Management**
   - Automatic calculation of required trading margin
   - Excess funds automatically transferred to savings
   - Automatic redemption from savings when funds are insufficient

3. **Dynamic Grid**
   - Base price automatically adjusts with market movements
   - Automatic cleanup of distant grid orders

4. **Risk Control**
   - Complete logging system
   - Real-time WeChat notifications
   - Automatic exception handling

## Logging

Program logs are saved in the `arbitrage.log` file, managed using rotation with a maximum size of 10MB per file, keeping the 5 most recent files.

## Important Notes

1. Ensure API KEY has trading permissions
2. Recommended to test on testnet first
3. Set grid parameters reasonably to avoid excessive fund occupation
4. Regular log checking recommended to ensure system normal operation

## Disclaimer

This project is for learning and communication purposes only and does not constitute investment advice. Any losses incurred from using this program are solely the responsibility of the user.

---


