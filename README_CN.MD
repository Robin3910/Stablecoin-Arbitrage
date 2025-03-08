
# Binance 稳定币USDC/USDT，FDUSD/USDT网格交易机器人

[English](https://github.com/Robin3910/Stablecoin-Arbitrage/blob/main/README.md) | [中文](https://github.com/Robin3910/Stablecoin-Arbitrage/blob/main/README_CN.MD)

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