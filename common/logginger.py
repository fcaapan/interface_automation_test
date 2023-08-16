import logging, os
import time

from config import BASE_PATH

# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

#初始化日志
class Logger():
    def __init__(self):
        # 1. 创建日志器对象
        self.logger = logging.getLogger()
        self.logger.setLevel("INFO")
        # 2. 创建处理器对象
        #    1. 创建控制台处理器（配置将日志打印到控制台）
        self.sh = logging.StreamHandler()
        #    2. 创建文件处理器（配置将日志打印到指定的文件夹中）
        # 保存日志的文件地址
        self.filename = BASE_PATH+"/log/" + "{}.log".format(time.strftime("%Y%m%d"))
        self.fh = logging.handlers.TimedRotatingFileHandler(self.filename, "midnight", 1, 7, encoding="utf-8")
        # 3. 创建格式化器对象
        # 日志打印格式
        self.fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
        self.formatter = logging.Formatter(self.fmt)

        # 4. 将格式化器对象添加到处理器对象中
        #    1. 设置控制台处理器
        self.sh.setFormatter(self.formatter)
        #    2. 设置文件处理器
        self.fh.setFormatter(self.formatter)

        # 5. 将处理器对象添加到日志器对象中
        #    1. 将控制台处理器添加日志器对象
        self.logger.addHandler(self.sh)
        #    2. 将文件处理器添加日志器对象
        self.logger.addHandler(self.fh)


logging =Logger().logger
print(111)

if __name__ == '__main__':
    logging.debug("最低级别的日志")
    logging.info("这是一个消息级别的日志")
    logging.warning("这是一个警告")
    logging.error("出现BUG了")
    logging.critical("系统马上就要崩溃了")


