import unittest
from common.readData import ReadData
from common.configHttp import ConfigHttp
import requests
from ddt import ddt,data,unpack
from common.publicAssertion import PublicAssertion
from common.log import logger
from common.PreSolve import PreSolve
# 获取测试数据
# data_test = ReadData()
# data_list = data_test.read_excl()
#
# @ddt
# class TestCase(unittest.TestCase):
#     @data(*data_list)
#     @unpack
#     def test_case(self,**kwargs):
#         if kwargs['method'].lower() == 'get':
#             res = requests.get(url=kwargs['interfaceUrl'], params=eval(kwargs['value']))
#
#         elif kwargs['method'].lower() == 'post':
#             res = requests.post(url=kwargs['interfaceUrl'], data=eval(kwargs['value']))
#
#         res_dict = res.json()
#         self.assertEqual(res_dict['errorCode'],eval(kwargs['expect']),'测试不通过')
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

data_test = ReadData()
data_list = data_test.read_excl()

@ddt
class TestCase(unittest.TestCase):
    @data(*data_list)
    @unpack
    def test_case(self,**kwargs):

        ps = PreSolve(data_list)

        kwargs['header'],kwargs['value'] =  ps.preSolve(kwargs)
        logger.debug(kwargs)
        print('----->',kwargs['header'],kwargs['value'])

        ch = ConfigHttp(kwargs)
        res = ch.run()
        # res_dict = res.json()
        # self.assertEqual(res_dict['errorCode'],eval(kwargs['expect']),'测试不通过')
        # 实例化
        pa = PublicAssertion(kwargs['expect'],res)
        pa.public_assert()

        # if 1 == 2:
        #     print('测试通过')
        # else:
        #     print('测试不通过')
        #     raise AssertionError

        # try:
        #     pa = PublicAssertion(kwargs['expect'], res)
        #     pa.public_assert()
        # except Exception  as msg:
        #     print(msg)
        #     raise




if __name__ == '__main__':
    unittest.main(verbosity=2)
