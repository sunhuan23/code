import requests
class ConfigHttp:
    def __init__(self,i):
        self.kwargs = i
    def run(self):
        if self.kwargs['method'].lower() == 'get':
            return self.__get()

        elif self.kwargs['method'].lower() == 'post':
            return self.__post()
    def __get(self):
        res = requests.get(url=self.kwargs['interfaceUrl'], params=eval(self.kwargs['value']),headers =eval(self.kwargs['header']))
        return res

    def __post(self):
        res = requests.post(url=self.kwargs['interfaceUrl'], data=eval(self.kwargs['value']),headers=eval(self.kwargs['header']))
        return res


if __name__ == '__main__':
    data = {'id': '1', 'interfaceUrl': 'https://www.wanandroid.com/user/login', 'name': 'login', 'method': 'post',
        'value': "{'username':'liangchao','password':'123456'}", 'header': '{}', 'expect': '0'}
    ch = ConfigHttp(data)
    res1 = ch.run()
    print(res1.text)