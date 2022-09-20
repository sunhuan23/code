import unittest
from ddt import ddt, unpack, data
from common.ReadData import ReadData
from common.ConfigHttp import ConfigHttp
from common.PublicAssertion import PublicAssertion
from common.InterfaceRely import InterfaceRely
"""
读取测试数据
定义一个测试用例的类
    定义一个测试用例的方法
    进行接口请求
    进行断言

"""


@ddt
class TestCase(unittest.TestCase):
    rd = ReadData()
    data_list = rd.readExcel('Sheet2')

    @data(*data_list)
    @unpack
    def testCase(self, **kwargs):
        # 进行接口请求
        re = InterfaceRely(self.data_list,kwargs)
        kwargs['header'],kwargs['value'] = re.interface()
        ch = ConfigHttp(kwargs)
        res = ch.configHttp()
        pa = PublicAssertion(kwargs["expect"],res)
        pa.publicAssertion()


if __name__ == '__main__':
    unittest.main(verbosity=2)
