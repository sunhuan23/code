import requests

"""
定义一个请求类
    定义一个初始化方法
        测试数据
    定义一个请求方法
"""
class ConfigHttp:

    def __init__(self,data_dict):
        """
        封装请求方法
        :param data_dict: 接收一个字典
        """
        self.data_dict = data_dict
        # 获取字典中的url
        self.url = self.data_dict['interfaceUrl']
        # 获取字典中的请求方式
        self.method = self.data_dict['method']
        # 获取字典中的请求参数
        self.value = eval(self.data_dict['value'])
        self.header = eval(self.data_dict['header'])
    def configHttp(self):
        if self.method.lower() == 'get':
            return self.__get()
        elif self.method.lower() == 'post':
            return self.__post()
    def __get(self):
        s = requests.session()
        res = s.get(url=self.url,params=self.value,headers=self.header)
        return res
    def __post(self):
        s = requests.session()
        res = s.post(url=self.url,data=self.value,headers=self.header)
        return res
if __name__ == '__main__':
    data = {'id': 1.0, 'interfaceUrl': 'http://www.zhibo.tv/app/user/andlogin', 'name': 'login', 'method': 'post', 'value': "{'email': '13664769063','password': '000000'}", 'header': '{}', 'expect': "{'status':200,'room_num':'34723990'}"}
    ch = ConfigHttp(data)
    print(ch.configHttp().text)
