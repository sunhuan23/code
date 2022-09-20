import unittest, os, time
from HTMLTestRunner import HTMLTestReportCN
from common.SendEmail import sE
"""
1、定义一个识别测试用例的方法
    获取测试用例路径
    实例化testloader类
    调用discover方法
    返回测试套件
"""


def suit():
    path = os.path.dirname(__file__) + '/TestCase'
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=path, pattern='Test*.py', top_level_dir=None)
    return suite


"""
创建一个生成html报告的方法
    获取报告路径
    打开报告，wb写入
    实例化htmltestreportcn
"""


def report():
    t = time.strftime('%Y%m%d%H%M%S', time.localtime())
    path = os.path.dirname(__file__) + '/TestReport/' + t + 'report.html'
    with open(path, 'wb') as f:
        hr = HTMLTestReportCN(stream=f, title='接口测试报告', description='接口测试报告结果', tester='孙欢')
        hr.run(suit())
    return path


"""
定义一个删除测试报告的方法
    获取所有报告
    将报告正序排序
    循环报告，
    删除报告 
"""
def del_report():
    path = os.path.dirname(__file__) + '/TestReport/'
    path_list =os.listdir(path)
    path_list.sort()
    print(path_list)
    for i in path_list[:-5]:
        os.remove(path + i)


if __name__ == '__main__':
    # loader = unittest.TextTestRunner()
    # loader.run(suit())
    report_path = report()
    del_report()
    sE.sendEmail(report_path)
