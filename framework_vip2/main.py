import unittest,os
from common.log import logger
from HTMLTestRunner import HTMLTestReportCN
import time
from common.readConfig import ReadConfig
from common.SendEmail import SendEmail
"""
1、查找测试用例生成测试套件
    获取测试用例路径
    实例化testLoader类
    调用discover方法
    生成测试套件

"""
# 1、查找测试用例生成测试套件
def creat_suite():
    #     获取测试用例路径
    case_path = os.path.dirname(__file__) + '/testCase'
    #     实例化testLoader类
    # loader = unittest.TestLoader()
    # #     调用discover方法
    # suite = loader.discover(start_dir=case_path,pattern='Test*.py',top_level_dir=None)
    suite = unittest.defaultTestLoader.discover(start_dir=case_path,pattern='Test*.py',top_level_dir=None)
    #     返回生成测试套件
    logger.debug(suite)
    return suite
def auto_clear():
    dir = os.path.dirname(__file__) + '/testReport/'
    #   获取目录中所有文件列表
    file_list = os.listdir(dir)
    file_list.sort()
    print(file_list)
    for i in file_list[:-5]:
        os.remove(dir + i)

    # os.listdir()
    # 获取目录下全部文件得到一个列表
    # 获取文件的创建时间: os.path.getctime()
    # 使用字典推导式生成一个字典: 时间为key, 文件名为value
    # 按照时间进行排序
    # 截取开头至倒数5个的文件, 获得一个列表
    # 循环删除每一个文件

if __name__ == '__main__':
    suite = creat_suite()
    # 报告路径
    cur_time = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
    report = os.path.dirname(__file__) + '/testReport/' +cur_time + 'report.html'
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # 打开报告
    with open(report,'wb') as fb:

        runner = HTMLTestReportCN(stream=fb,title='接口自动化测试',description='接口自动化测试结果',verbosity=2)
        runner.run(suite)
    auto_clear()
    # 发邮箱
    rc = ReadConfig()
    kwargs = rc.get_config('email')
    se = SendEmail(**kwargs)
    se.connection_server(report)