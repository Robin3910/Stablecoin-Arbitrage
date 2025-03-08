# Binance 稳定币USDC/USDT，FDUSD/USDT网格交易机器人

[English](README.md#binance-stablecoin-grid-trading-bot-for-usdcusdt-fdusdusdt) | [中文](README.md#binance-稳定币usdcusdt，fdusdusdt网格交易机器人)

这是一个基于 Binance API 的自动化稳定币网格交易机器人,支持多币种网格交易和自动理财管理。

目标在于通过稳定币的网格套利，获取稳定无风险收益。争取年化可以做到15%。
同时利用理财功能，在无法套利的情况下，自动将资金转入理财，获取理财收益。

## 主要功能

- 支持多币种同时网格交易
- 自动管理账户余额,在交易和理财之间动态调配资金
- 动态调整网格基准价格(base price)
- 自动发送微信通知
- 完整的日志记录系统

## 安装依赖

```bash
pip install binance-connector
pip install requests
```

## 配置说明

在运行之前需要创建 `config.py` 文件,包含以下配置:

```python
CONFIG = {
    "API_KEY": "你的API KEY",
    "API_SECRET": "你的API SECRET",
    "balance_buffer": 5,  # 余额缓冲区(网格数量)
    "SYMBOLS": {
        "USDCUSDT": {  # 交易对配置
            "BASE_PRICE": 1.0,  # 基准价格
            "PRICE_INTERVAL": 0.0001,  # 网格间距
            "ORDER_AMOUNT": 100,  # 每格订单数量
            "PROFIT_INTERVAL": 0.0001,  # 止盈间距
            "MAX_ORDERS": 10  # 最大订单数
        },
        # 可添加更多交易对...
    }
}
```

## 运行

```bash
python arbitrage.py
```

## 主要特性

1. **多币种支持**
   - 可同时运行多个交易对的网格策略
   - 每个交易对可独立配置参数

2. **智能资金管理**
   - 自动计算所需交易保证金
   - 多余资金自动转入理财
   - 资金不足时自动从理财赎回

3. **动态网格**
   - 基准价格随市场变动自动调整
   - 自动清理过远的网格订单

4. **风险控制**
   - 完整的日志记录
   - 微信实时通知
   - 异常自动处理

## 日志

程序运行日志保存在 `arbitrage.log` 文件中,使用 rotating 方式管理,单个文件最大 10MB,保留最近 5 个文件。

## 注意事项

1. 请确保 API KEY 具有交易权限
2. 建议先使用测试网进行测试
3. 请合理设置网格参数,避免资金占用过大
4. 建议定期检查日志确保系统正常运行

## 免责声明

本项目仅供学习交流使用,不构成投资建议。使用本程序进行交易造成的任何损失均由使用者自行承担。

---

# Binance Stablecoin Grid Trading Bot for USDC/USDT, FDUSD/USDT

[English](README.md#binance-stablecoin-grid-trading-bot-for-usdcusdt-fdusdusdt) | [中文](README.md#binance-稳定币usdcusdt，fdusdusdt网格交易机器人)

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
