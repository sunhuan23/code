import unittest
from common.ReadData import ReadData
import requests
from ddt import ddt,data,unpack
from common.ConfigHttp import ConfigHttp
from common.PublicAssertion import PulicAssertion
from common.InterfaceRely import InterfaceRely
"""
1、获取测试数据
2、创建一个类，继承unittest.TestCase
    编写一条测试用例
        获取需要的字段
        进行网络请求
        断言
"""
# 1、获取测试数据
rd = ReadData()
data_list = rd.readExcel()
print(data_list)
# 2、创建一个类，继承unittest.TestCase
@ddt
class TestCase(unittest.TestCase):
    #     编写一条测试用例
    @data(*data_list)
    @unpack
    def testCase(self,**kwargs):
        #         获取需要的字段
        # url = kwargs["interfaceUrl"]
        # value = kwargs['value']
        # method = kwargs['method']
        # expect = kwargs['expect']
        # #         进行网络请求
        # if method.lower() == 'get':
        #     res = requests.get(url=url,params=eval(value))
        # elif method.lower() == 'post':
        #     res = requests.post(url=url,data=eval(value))
        # res_dict = res.json()
        pre = InterfaceRely(data_list,kwargs)
        kwargs['header'],kwargs['value'] = pre.interfaceRely()

        ch = ConfigHttp(kwargs)
        res = ch.configHttp()
        res1 =res.json()

        #         断言
        # self.assertEqual(eval(expect)['errorCode'],str(res['errorCode']),'测试不通过')
        pa = PulicAssertion(kwargs,res1)

        pa.publicAssertion()
if __name__ == '__main__':
    unittest.main(verbosity=2)