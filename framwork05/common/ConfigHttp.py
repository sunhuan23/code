import requests

"""
定义一个接口请求的类
    定义一个初始化方法
        获取url
        获取请求方法
        获取header
        获取value
    定义一个给外界使用的请求方法
        判断请求方法为get
            调用get方法
        判断请求方法为post
            调用post方法
    定义一个私有的请求get的方法
        进行接口请求
        返回响应
    定义一个私有的请求post的方法
        进行接口请求
        返回响应
"""


# 定义一个接口请求的类
class ConfigHttp:
    #     定义一个初始化方法,接收当前用例的数据
    def __init__(self, kwargs):
        #         获取url
        self.url = kwargs['interfaceUrl']
        #         获取请求方法
        self.method = kwargs['method']
        #         获取header
        self.header = eval(kwargs['header'])
        #         获取value
        self.value = eval(kwargs['value'])

    #     定义一个给外界使用的请求方法
    def configHttp(self):
        #         判断请求方法为get
        if self.method.lower() == 'get':
            return self.__get()
        #             调用get方法
        #       判断请求方法为post
        elif self.method.lower() == 'post':
            return self.__post()

    #             调用post方法
    def __get(self):
        #     定义一个私有的请求get的方法
        res = requests.get(url=self.url, params=self.value, headers=self.header)
        #         进行接口请求
        return res

    #         返回响应
    #     定义一个私有的请求post的方法
    def __post(self):
        #         进行接口请求
        res = requests.post(url=self.url, data=self.value, headers=self.header)
        return res
#         返回响应
