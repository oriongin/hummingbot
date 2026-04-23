#!/usr/bin/env python

connector_status = {
    'opencex': 'gold',
    'binance': 'gold',
    'binance_perpetual': 'gold',
    'binance_us': 'bronze',
    'gate_io': 'silver',
    'gate_io_perpetual': 'silver',
    'okx': 'bronze',
    'bybit': 'bronze',
    'uniswap': 'gold',
    'uniswapLP': 'gold',
    'pancakeswap': 'silver',
    'sushiswap': 'bronze',
    'bitfinex': 'bronze',
    'bitmart': 'bronze',
    'coinbase_pro': 'bronze',
    'huobi': 'bronze',
    'kraken': 'bronze',
    'loopring': 'bronze',
    'mexc': 'bronze',
}

warning_messages = {
}


def get_connector_status(connector_name: str) -> str:
    """
    Indicator whether a connector is working properly or not.
    UNKNOWN means the connector is not in connector_status dict.
    RED means a connector doesn't work.
    YELLOW means the connector is either new or has one or more issues.
    GREEN means a connector is working properly.
    """
    if connector_name not in connector_status.keys():
        status = "UNKNOWN"
    else:
        return f"&c{connector_status[connector_name].upper()}"
    return status
