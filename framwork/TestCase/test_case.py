import unittest
from ddt import ddt,data,unpack
from common.ReadData import ReadData
from common.ConfigHttp import ConfigHttp
from common.PublicAssertion import PublicAssertion
import warnings
from common.Interface_rely import InterfaceRely

"""
1、创建一个测试类
    1.1 定义一个初始化方法
        读取测试数据
    1.2 编写一条测试用例
        使用ddt进行数据驱动
        网络请求 
        断言
    
"""

rd = ReadData()
data_list = rd.readExcel('Sheet1')
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
    @data(*data_list)
    @unpack
    def test_case(self,**kwargs):
        rel = InterfaceRely(data_list,kwargs)
        kwargs['header'],kwargs['value'] = rel.interfaceRely()
        ch = ConfigHttp(kwargs)
        res = ch.configHttp()
        pa = PublicAssertion(kwargs['expect'],res)
        pa.publicAssertion()
if __name__ == '__main__':
    unittest.main(verbosity=2)




