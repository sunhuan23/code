import logging
import os
"""
定义一个使用log的方法

"""
# def logger():
#     logging.basicConfig(level="DEBUG",
#                         format="日志:%(name)s-级别:%(levelname)s-时间%(asctime)s-模块%(module)s.py-第%(lineno)d行:%(message)s")
#     logger = logging.getLogger('test')
#     return logger

def log():
    logger = logging.getLogger('test')
    logger.setLevel('DEBUG')
    format1 = logging.Formatter('日志:%(name)s-级别:%(levelname)s-时间%(asctime)s-模块%(module)s.py-第%(lineno)d行:%(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(format1)
    logger.addHandler(sh)
    path = os.path.dirname(os.path.dirname(__file__)) + '/TestLog/log.log'
    fh = logging.FileHandler(path)
    fh.setFormatter(format1)
    logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    log=log()
    log.debug('打印')