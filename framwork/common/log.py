import logging
import os
"""
使用面向过程的形式
1、创建一个可供外界使用的方法
    1、设置日志等级/格式
    2、设置日志记录器
    3、返回日志记录器
2、创建一个可供外界使用的方法
    1、设置日志记录器
    2、设置日志等级
    3、设置日志格式
    4、设置日志输出位置
"""
# 方式一：
# def log():
#     logging.basicConfig(level=logging.DEBUG,
#                         format='日志:%(name)s-级别:%(levelname)s-时间%(asctime)s-模块%(module)s.py-第%(lineno)d行:%(message)s')
#     logger = logging.getLogger('Test')
#     return logger
def log():
    logger = logging.getLogger('Test')
    logger.setLevel(logging.DEBUG)
    format1 = logging.Formatter('日志:%(name)s-级别:%(levelname)s-时间%(asctime)s-模块%(module)s.py-第%(lineno)d行:%(message)s')
    sh = logging.StreamHandler()
    sh.setFormatter(format1)
    logger.addHandler(sh)
    path = os.path.dirname(os.path.dirname(__file__)) + '/testLog/'
    fh = logging.FileHandler(path + 'log.log')
    fh.setFormatter(format1)
    logger.addHandler(fh)
    return logger
log = log()


# if __name__ == '__main__':
    # log1 = log()