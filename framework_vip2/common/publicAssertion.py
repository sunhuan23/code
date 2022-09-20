import unittest
from jsonpath import jsonpath
from common.configHttp import ConfigHttp
"""
思路分析：
    1、  创建一个类
    1.1  定义一个初始化的方法
        1.1.1 获取用例的预期结果
        1.1.2 获取用例的实际结果
    1.2  定义一个对外提供的断言方法
        1.2.1  循环获取断言字典中的键值对
        1.2.2  根据取出的键获取返回结果里面的对应结果
        1.2.3  断言取到的实际结果和预期结果是否一致
"""
# 1、  创建一个类
class PublicAssertion(unittest.TestCase):
# 1.1  定义一个初始化的方法
    def __init__(self, expect, res):
        # 1.1.1  获取用例的预期结果
        super().__init__()
        self.expect = eval(expect)
        # 1.1.2 获取用例的实际结果
        self.res = res.json()
    # 1.2 定义一个对外提供的断言方法
    def public_assert(self):
        # 1.2.1 循环获取断言字典中的键值对
        for k,v in self.expect.items():
            # 1.2.2 根据取出的键获取返回结果里面的对应结果
            real = jsonpath(self.res, '$..' + k)[0]
            # 1.2.3 断言取到的实际结果和预期结果是否一致

            self.assertEqual(str(real),v,'测试不通过')
if __name__ == '__main__':
    expect = "{'errorCode':'0','username':'liangchao'}"
    data = {'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'method': 'post',
            'value': "{'username':'liangchao','password':'123456'}", 'header': '{}', 'expect': '0'}
    ch = ConfigHttp(data)
    res = ch.run()
    print(res.text)
    pa = PublicAssertion(expect,res)
    pa.public_assert()