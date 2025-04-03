def check_volume():
    current_volume = 300
    average_volume = 100
    if average_volume == 0:
        return None
    if current_volume > 1.8 * average_volume:
        return "爆量強"
    return None
