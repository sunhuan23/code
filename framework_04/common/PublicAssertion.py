import unittest
from jsonpath import jsonpath
"""
1、定义一个类，用来做断言
    定义一个初始化方法，预期结果，实际结果
        获取预期结果
        获取实际结果
        
    定义一个断言方法
        进行断言     
"""
class PublicAssertion(unittest.TestCase):
    def __init__(self,expect,res):
        super().__init__()
        self.expct =eval(expect)
        self.res = res.json()
    def publicAssertion(self):
        for k,v in self.expct.items():
            res_dict = jsonpath(self.res,'$..'+k)[0]
            self.assertEqual(str(res_dict),v,'测试不通过')





