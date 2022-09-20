import unittest
import os
from HTMLTestRunner import HTMLTestReportCN
import time
from common.SendEmail import sE
"""
执行测试用例入口
"""
"""
定义一个方法加载测试用例套件
    实例化TestLoader
    获取测试用例目录
    使用discover方法将目录下的测试用例加载到测试套件中
    将测试套件返回
"""


def loader_suite():
    loader = unittest.TestLoader()
    casepath = os.path.dirname(__file__) + '/testCase'
    suite = loader.discover(start_dir=casepath,pattern='Test*.py',top_level_dir=None)
    return suite
"""
定义一个生成测试报告的方法
    获取报告路径
    写入模式打开html报告
    实例化HTMLTestReport,路径，标题，描述，等级，测试人员
    调用run方法执行测试用例
"""


def html_report():
    t = time.strftime('%Y%m%d%H%M%S',time.localtime())
    reportpath = os.path.dirname(__file__) + '/testReport/'+t+'report.html'
    with open(reportpath,'wb') as f:
        runner = HTMLTestReportCN(stream=f,title='自动化测试报告',description='接口测试结果',verbosity=2)
        runner.run(loader_suite())
    return reportpath
"""
定义一个清理报告的方法
    获取测试报告的路径
    获取里边的报告列表
    选择将报告删除
"""
def auto_clear():
    reportpath = os.path.dirname(__file__) + '/testReport/'
    report_list = os.listdir(reportpath)
    report_list.sort()
    for i in report_list[:-5]:
        os.remove(reportpath+i)


if __name__ == '__main__':
    report = html_report()
    auto_clear()
    sE.sendemail(report)