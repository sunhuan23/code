import unittest
import os
from HTMLTestRunner import HTMLTestReportCN
import time
from common.SendEmail import sE
"""
1、定义一个测试套件方法
    获取测试用例目录
    实例化testloader
    使用discover查找
    
"""


def suite():
    casepath =os.path.dirname(__file__) +'/TestCase'
    loader = unittest.TestLoader()
    suit = loader.discover(start_dir=casepath,pattern='Test*.py',top_level_dir=None)
    return suit


"""
定义一个生成报告的方法
    获取报告地址
    打开报告，写入模式报告
    实例化hrmltestreportcn
"""


def report():
    t = time.strftime('%Y%m%d%H%M%S',time.localtime())
    reportpath = os.path.dirname(__file__) + '/TestReport/'+t+'report.html'
    with open(reportpath,'wb') as f:
        runner = HTMLTestReportCN(stream=f,title='接口测试报告',description='接口测试报告结果',tester='孙欢',verbosity=2)
        runner.run(suite())
    return reportpath
"""
定义一个方法删除报告
    获取报告路径
    获取路径下报告列表
    将列表正序排序
    分割循环列表，保留最新的五个
    删除列表
"""


def auto_report():
    reportpath = os.path.dirname(__file__) + '/TestReport/'
    report_list = os.listdir(reportpath)
    report_list.sort()
    for i in report_list[:-5]:
        print(i)
        os.remove(reportpath + i)



if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # suite = suite()
    # runner.run(suite)
    report = report()
    auto_report()
    sE.sendEmail(report)
