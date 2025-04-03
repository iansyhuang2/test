import time
import logging
from detectors.volume_check import check_volume
from detectors.kbar_check import check_kbar
from detectors.ma_check import check_ma
from sender import send_message

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    logger.info("交易信号检测Worker启动")
    while True:
        try:
            # 执行检测
            results = [
                check_volume(),
                check_kbar(),
                check_ma()
            ]

            # 发送有效消息
            for msg in filter(None, results):
                send_message(msg)
                logger.info(f"已发送消息: {msg}")

            # 等待下一次检测
            time.sleep(CHECK_INTERVAL)

        except Exception as e:
            logger.error(f"发生错误: {str(e)}")
            time.sleep(60)  # 错误后等待1分钟再重试

if __name__ == "__main__":
    main()


