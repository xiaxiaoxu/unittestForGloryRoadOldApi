#encoding=utf-8

import logging.config
import os

from config.config import log_path


#读取日志的配置文件
logging.config.fileConfig(log_path+"\\config\\Logger.conf")
#选择一个日志格式
logger=logging.getLogger("example01") #example01


if __name__=="__main__":
    print("conf file path:", log_path+"\\config\\Logger.conf")
    logger.info("hi")
    logger.error("world!")
    logger.warning("gloryroad!")