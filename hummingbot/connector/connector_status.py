#!/usr/bin/env python

connector_status = {
    'opencex': 'gold',

    'binance': 'gold',
    'binance_perpetual': 'gold',
    'binance_us': 'bronze',
    'gate_io': 'silver',
    'gate_io_perpetual': 'silver',
    'okx': 'bronze',
    
    'uniswap': 'gold',
    'uniswapLP': 'gold',
    'pancakeswap': 'silver',
    'sushiswap': 'bronze',
    
    'bitfinex': 'bronze',
    'bitmart': 'bronze',
    'coinbase_pro': 'bronze',
    'hitbtc': 'bronze',
    'huobi': 'bronze',
    'kraken': 'bronze',
    'loopring': 'bronze',
    'mexc': 'bronze',
}

warning_messages = {
}

def get_connector_status(connector_name: str) -> str:
    """
    Xác định trạng thái hoạt động của Connector.
    GOLD/SILVER/BRONZE: Các cấp độ chứng nhận.
    UNKNOWN: Không có trong danh sách.
    """
    if connector_name not in connector_status.keys():
        status = "UNKNOWN"
    else:
        # Trả về cấp độ viết hoa kèm mã màu (&c)
        return f"&c{connector_status[connector_name].upper()}"
    return status