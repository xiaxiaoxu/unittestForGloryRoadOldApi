#encoding=utf-8
import hashlib
from log import logger

# md5加密方法，用于调试
def md5Hash(password):
    """md5 加密分为digest和hexdigest两种格式，前者是二进制，后者是十六进制格式，这里默认为十六进制"""
    try:
        m5 = hashlib.md5()
        m5.update(password.encode(encoding = 'utf-8'))
        pwd = m5.hexdigest()
        return pwd
    except Exception as e:
        logger.info("md5Hash error: %s" % e)

if __name__ == '__main__':
    logger.info(md5Hash("wulaoshi2019"))