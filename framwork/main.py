import unittest
import os
from HTMLTestRunner import HTMLTestReportCN
import time
from common.SendEmail import sE
"""
1、定义一个获取测试套件的方法
 1、实例化 unittest.TestLoader
 2、获取测试用例目录
 3、调用discover方法查找测试用例
 4、将套件返回
2、定义一个生成报告的方法
    1、导入HTMLTestRunner
    2、获取日志路径
    3、实例化HTMLTestRunnerCN
    4、执行测试套件
3、定义一个清理报告的方法
    1、获取测试报告目录
    2、获取测试报告目录下所有的报告列表
    3、讲报告升序排序
    4、循环遍历表表，并分割
    5、删除报告
    
"""
def get_suit():
    # 1、实例化 unittest.TestLoaderder
    loader = unittest.TestLoader()
    # 2、获取测试用例目录
    casepath = os.path.dirname(__file__) + '/TestCase'
    # 3、调用discover方法查找测试用例
    suit = loader.discover(start_dir=casepath,pattern='test*.py',top_level_dir=None)
    #  4、将套件返回
    return suit

# 2、定义一个生成报告的方法
def case_html():
    # 1、获取日志路径
    t = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
    reportpath = os.path.dirname(__file__)+'/testReport/'+t+'report.html'
    # 2、写的方式打开html文件
    with open(reportpath,'wb') as f:
        # 2、实例化HTMLTestRunnerCN,并将报告写入html文件中
        runner = HTMLTestReportCN(stream=f,title='接口自动化测试',description='接口自动化测试结果',verbosity=2,tester='QA孙欢')
        # 3、执行测试套件
        runner.run(get_suit())
    return reportpath
def auto_clear():
    # 1、获取测试报告目录
    reportpath = os.path.dirname(__file__) + '/testReport/'
    # 2、获取测试报告目录下所有的报告列表
    reportlist = os.listdir(reportpath)
    # 3、将报告升序排序
    reportlist.sort()
    # 4、循环遍历列表，并分割
    for i in reportlist[:-5]:
        # 5、删除报告
        os.remove(reportpath + i)


if __name__ == '__main__':
    report = case_html()
    print(report)
    auto_clear()

    sE.sendEmail(report)
    # se.sendEmail(report.reportpath)