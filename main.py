from config import *
from detectors.volume_check import check_volume
from detectors.kbar_check import check_kbar
from detectors.ma_check import check_ma
from sender import send_message

import time

while True:
    result_volume = check_volume()
    result_kbar = check_kbar()
    result_ma = check_ma()

    messages = [msg for msg in [result_volume, result_kbar, result_ma] if msg]

    for msg in messages:
        send_message(msg)

    time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()


