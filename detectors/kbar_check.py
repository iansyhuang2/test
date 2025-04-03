def check_kbar():
    open_price = 100
    close_price = 105
    high = 110
    low = 95

    body = abs(close_price - open_price)
    upper_shadow = high - max(open_price, close_price)
    lower_shadow = min(open_price, close_price) - low

    if upper_shadow > 1.5 * body:
        return '影轉弱'
    elif lower_shadow > 1.5 * body:
        return '影轉強'
    return None
