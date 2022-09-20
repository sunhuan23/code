import re
from common.ConfigHttp import ConfigHttp
from jsonpath import jsonpath
"""
1、定义一个类接口依赖的类
    定义一个初始化方法
        获取全部测试用例
        获取当前测试用例
        获取header
        获取value
        获取rely
        获取caseid
    定义一个接口依赖的方法
        判断是否有依赖，caseid是否为空
            是，使用正则将数据提取出来
            执行前置用例
            提取需要的字段
            替换数据
            否，返回heade，value
"""
class InterfaceRely:
    def __init__(self,dataliast,kwargs):
        self.datalist = dataliast
        self.kwargs = kwargs
        self.header = self.kwargs['header']
        self.value = self.kwargs['value']
        self.rely = self.kwargs['rely']
        self.caseid = self.kwargs['caseid']
    def interfaceRely(self):
        if self.rely == 'y' and self.caseid != '':
            header = self.get_pre(self.header)
            value = self.get_pre(self.value)
            self.header,self.value = self.run_pre(header,value)
            return self.header,self.value

        else:
            return self.header,self.value
    def get_pre(self,data):
        res = re.findall('\${(.*?)}',data)
        if len(res)>0:
            data = res[0]
        else:
            data = None
        return data
    def run_pre(self,h=None,v=None):
        case = self.datalist[int(self.caseid)-1]
        ch = ConfigHttp(case)
        res = ch.configHttp()
        if h != None:
            header = res.headers[h]
            self.header = self.header.replace('${'+h+'}',header)
        if v != None:
            res1 = res.json()
            value = jsonpath(res1,'$..'+ v)[0]
            self.value = self.value.replace('${' + h + '}', value)
        return self.header,self.value