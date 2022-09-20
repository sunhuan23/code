"""
导包
    1、获取测试数据
    2、定义一个测试类
        2.1 创建一个测试用例方法
        2.2 获取测试数据内的请求所需要的关键字段
        2.3 进行请求获得返回结果
        2.4 断言接口返回结果，断言成功失败
"""
# 导包
# import unittest
# import requests
# import json
# from ddt import ddt,data,unpack
# from common.readData import ReadData
# #     1、获取测试数据
# re = ReadData()
# re_data = re.read_excl()
# print(re_data)
# #     2、定义一个测试类
# class TestCase(unittest.TestCase):
#     #         2.1 创建一个测试用例方法
#     def test_case(self):
#         #         2.2 获取测试数据内的请求所需要的关键字段
#
#         url  = re_data[0]["interfaceUrl"]
#         method = re_data[0]['method']
#         value = re_data[0]['value']
#         expect = re_data[0]['expect']
#         #         2.3 进行请求获得返回结果
#         if method.lower() == 'get':
#             res = requests.get(url=url,params=eval(value))
#         elif method.lower() == 'post':
#             res = requests.post(url=url,data=eval(value))
#         dict1 = res.json()
#         #         2.4 断言接口返回结果，断言成功失败
#         self.assertEqual(dict1["errorCode"], eval(expect),'测试不通过')
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#

"""
导包
    1、获取测试数据
    2、定义一个测试类
        2.1 创建一个测试用例方法
        2.2 获取测试数据内的请求所需要的关键字段
        2.3 进行请求获得返回结果
        2.4 断言接口返回结果，断言成功失败
"""
# 导包
import unittest
import requests
import json
# from common.readData import ReadData
# #     1、获取测试数据
# re = ReadData()
# re_data = re.read_excl()
# print(re_data)
#     2、定义一个测试类
# class TestCase(unittest.TestCase):
#     #         2.1 创建一个测试用例方法
#     def test_case(self):
#         #         2.2 获取测试数据内的请求所需要的关键字段
#         for i in range(len(re_data)):
#             url  = re_data[i]["interfaceUrl"]
#             method = re_data[i]['method']
#             value = re_data[i]['value']
#             expect = re_data[i]['expect']
#             name = re_data[i]['name']
#             #         2.3 进行请求获得返回结果
#
#             if method.lower() == 'get':
#                 res = requests.get(url=url,params=eval(value))
#             elif method.lower() == 'post':
#                 res = requests.post(url=url,data=eval(value))
#             dict1 = res.json()
#             #         2.4 断言接口返回结果，断言成功失败
#             if name == 'login':
#                 self.assertEqual(dict1["errorCode"], eval(expect),'测试不通过')
#             elif name == 'register':
#                 self.assertEqual(str(dict1["errorCode"]),expect,'测试不通过')
#             elif name == 'logout':
#                 self.assertEqual(dict1["errorCode"],eval(expect),'测试不通过')
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

"""
ddt数据驱动
"""

# 导包
import unittest
import requests
import json
from ddt import ddt,data,unpack
from common.readData import ReadData
#     1、获取测试数据
re = ReadData()
re_data = re.read_excl()
print(re_data)
#     2、定义一个测试类
@ddt
class TestCase(unittest.TestCase):
    #         2.1 创建一个测试用例方法
    @data(*re_data)
    @unpack
    def test_case(self,id,interfaceUrl,name,method,value,header,expect):
        #         2.2 获取测试数据内的请求所需要的关键字段

        # url  = re_data[0]["interfaceUrl"]
        # method = re_data[0]['method']
        # value = re_data[0]['value']
        # expect = re_data[0]['expect']
        #         2.3 进行请求获得返回结果
        if method.lower() == 'get':
            res = requests.get(url=interfaceUrl,params=eval(value))
        elif method.lower() == 'post':
            res = requests.post(url=interfaceUrl,data=eval(value))
        dict1 = res.json()
        #         2.4 断言接口返回结果，断言成功失败
        self.assertEqual(dict1["errorCode"], eval(expect),'测试不通过')
if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
ddt使用不定长参数
"""
import unittest
import requests
import json
from ddt import ddt,data,unpack
from common.readData import ReadData
from common.publicAssertion import PublicAssertion
#     1、获取测试数据
re = ReadData()
re_data = re.read_excl()
print(re_data)
#     2、定义一个测试类
@ddt
class TestCase(unittest.TestCase):
    #         2.1 创建一个测试用例方法
    @data(*re_data)
    @unpack
    def test_case(self,**kwargs):
        #         2.2 获取测试数据内的请求所需要的关键字段

        #         2.3 进行请求获得返回结果
        if kwargs['method'].lower() == 'get':
            res = requests.get(url=kwargs["interfaceUrl"],params=eval(kwargs["value"]))
        elif kwargs['method'].lower() == 'post':
            res = requests.post(url=kwargs["interfaceUrl"],data=eval(kwargs["value"]))
        dict1 = res.json()
        #         2.4 断言接口返回结果，断言成功失败
        self.assertEqual(dict1["errorCode"], eval(kwargs["expect"]),'测试不通过')


if __name__ == '__main__':
    unittest.main(verbosity=2)



