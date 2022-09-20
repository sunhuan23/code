import unittest
from common.ReadData import ReadData
from ddt import ddt,data,unpack
from common.ConfigHttp import ConfigHttp
from common.PublicAssertion import PublicAssertion
from common.InterfaceRely import InterfaceRely
"""
获取测试数据
使用ddt数据驱动
创建一个测试用例类，继承unittest.testCase
    使用data接收数据
    使用unpack拆包
    1、定义一个测试用例的方法
        进行网络请求
        进行断言
"""
rd = ReadData()
data_list = rd.readExcel('Sheet2')
@ddt
class TestCase(unittest.TestCase):
    @data(*data_list)
    @unpack
    def testcase(self,**kwargs):
        pre = InterfaceRely(data_list,kwargs)
        kwargs['header'],kwargs['value']=pre.interfaceRely()
        print(kwargs)
        ch = ConfigHttp(kwargs)
        res = ch.configHttp()
        pa = PublicAssertion(kwargs['expect'],res)
        pa.publicAssertion()



if __name__ == '__main__':
    unittest.main(verbosity=2)

