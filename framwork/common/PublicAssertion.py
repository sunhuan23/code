import unittest
from jsonpath import jsonpath
from common.ConfigHttp import ConfigHttp
"""
1、创建一个类
    1.1 定义一个初始化方法
            获取用例的预期结果
            获取用例的实际结果,响应内容
    1.2 定义一个给外界使用的断言
            对比预期结果和实际结果
"""
class PublicAssertion(unittest.TestCase):
    def __init__(self,expect,res):
        super().__init__()
        self.expect = eval(expect)
        self.res = res.json()
    def publicAssertion(self):
        for k,v in self.expect.items():
            value = jsonpath(self.res,'$..'+k)[0]
            self.assertEqual(str(value),v,'测试不通过')

if __name__ == '__main__':

    data = {'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'header': '{}', 'expect': "{'errorCode':'0','username':'liangchao'}"}
    ch = ConfigHttp(data)
    res = ch.configHttp()
    print(res.text)
    
    pa = PublicAssertion(data['expect'],res)
    pa.publicAssertion()