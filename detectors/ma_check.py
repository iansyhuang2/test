def check_ma():
    current_ma = 102
    previous_ma = 100
    if current_ma > previous_ma:
        return "均變強"
    elif current_ma < previous_ma:
        return "均變弱"
    return None
