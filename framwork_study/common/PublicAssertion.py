import unittest
from jsonpath import jsonpath
from common.ConfigHttp import ConfigHttp
"""
1、定义一个类继承unittest.TestCase
    定义一个初始化方法
        获取预期结果
        获取实际结果
    定义一个外界使用的方法
        循环预期结果
        判断
"""

# 1、定义一个类继承unittest.TestCase
class PulicAssertion(unittest.TestCase):
    #     定义一个初始化方法
    def __init__(self,expect,res):
        super().__init__()
    #         获取预期结果
        self.expect = eval(expect['expect'])
    #         获取实际结果
        self.res = res
    #     定义一个外界使用的方法
    def publicAssertion(self):
        #         循环预期结果
        for k,v in self.expect.items():
            res_value = jsonpath(self.res,'$..'+ k)[0]
            self.assertEqual(v,str(res_value),'测试不通过')



        #         判断
if __name__ == '__main__':
    dict1 = {'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'header': '{}', 'expect': "{'errorCode':'0','username':'liangchao'}"}
    ch = ConfigHttp(dict1)
    res = ch.configHttp()
    pa = PulicAssertion(dict1,res)
    pa.publicAssertion()
    # print(pa)
