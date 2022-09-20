import unittest
from jsonpath import jsonpath
from common.ReadData import ReadData
from common.ConfigHttp import ConfigHttp
"""
定义一个断言的类
    定义一个初始化方法，预期结果，实际结果
        获取预期结果
        获取实际结果
    定义一个断言方法
        循环断言字段，
        获取响应结果的断言字段
        进行断言
"""
class PublicAssertion(unittest.TestCase):
    def __init__(self,expect,res):
        super().__init__()
        self.expect =eval(expect)
        self.res = res.json()
    def publicAssertion(self):
        for k,v in self.expect.items():
            res1 = jsonpath(self.res,'$..'+k)[0]
            self.assertEqual(v,str(res1),"测试不通过")


if __name__ == '__main__':
    rd = ReadData()
    datalist = rd.readExcel('Sheet1')
    ch = ConfigHttp(datalist[0])
    res =ch.configHttp()
    pa = PublicAssertion("{'errorCode':'0','username':'liangchao'}",res)
    pa.publicAssertion()