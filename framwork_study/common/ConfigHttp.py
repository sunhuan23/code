import requests
"""
1、创建一个网络请求类
    1、定义一个初始化方法
        请求数据
    2、定义一个提供给外界使用的方法
        1、判断网络请求方式
            如果为get
                进行get请求
            如果为post
                进行post请求
"""
class ConfigHttp:
    def __init__(self,dict1):
        """

        :param dict1: 需要一个字典
        """
        # self.dict1 = dict1
        self.url = dict1['interfaceUrl']
        self.value = dict1['value']
        self.method = dict1['method']

    def configHttp(self):
        if self.method.lower() == 'get':
            return self.__get()
        elif self.method.lower() == 'post':
            return self.__post()
    def __get(self):
        res = requests.get(url=self.url, params=eval(self.value))

        return res
    def __post(self):
        res = requests.post(url=self.url, data=eval(self.value))

        return res



if __name__ == '__main__':
    dict1 = {'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'method': 'post', 'value': "{'username':'liangchao','password':'123456'}", 'header': '{}', 'expect': "{'errorCode':'0','username':'liangchao'}"}
    ch = ConfigHttp(dict1)
    res = ch.configHttp()

    print(res)

