import requests
"""
1、定义一个接口请求类
    定义一个初始化方法
    接收需要的字段
    定义一个请求方法
    判断method是get还是post
    最终返回请求结果
"""

class ConfigHttp:
    def __init__(self,kwargs):
        self.url = kwargs['interfaceUrl']
        self.method = kwargs['method']
        self.value =eval(kwargs['value'])
        self.header = eval(kwargs['header'])
    def configHttp(self):
        if self.method.lower() == 'get':
            return self.__get()
        elif self.method.lower() == 'post':
            return self.__post()

    def __get(self):
        res = requests.get(url=self.url,params=self.value,headers=self.header)
        return res
    def __post(self):
        res = requests.post(url=self.url,data=self.value,headers=self.header)
        return res


