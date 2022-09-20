import re
from common.ConfigHttp import ConfigHttp
from jsonpath import jsonpath
"""
定义一个处理接口依赖的类
    定义一个初始化的方法
        获取所有用例
        获取当前用例
        获取是否依赖字段
        获取caseid
        获取header
        获取value
    定义一个提供给外界使用处理接口依赖的方法
        判断依赖字段是否为y且caseid不为空
            是，使用正则表达式提取${}
                {"cookie":"${Set-Cookie}"}
                根据caseid执行前置用例
                根据正则表达式取响应结果
            否，返回原始数据
"""


class InterfaceRely:
    def __init__(self, datalist, kwargs):
        self.datalist = datalist
        self.kwargs = kwargs
        self.header = kwargs['header']
        self.value = kwargs['value']
        self.caseid = kwargs['caseid']
        self.rely = kwargs['rely']

    def interface(self):
        if self.rely == 'y' and self.caseid != None:
            h = self.get_rely(self.header)
            v = self.get_rely(self.value)
            self.header,self.value = self.pre_case(h,v)
            return self.header,self.value
        else:
            return self.header, self.value

    def get_rely(self,data):
        res = re.findall('\${(.*?)}',data)
        if len(res) > 0 :
            res_data = res[0]
        else:
            res_data = None
        return res_data


    def pre_case(self,h,v):
        case = self.datalist[int(self.caseid)-1]
        ch = ConfigHttp(case)
        res = ch.configHttp()
        if h != None:
            header = res.headers[h]
            self.header = self.header.replace('${'+h+'}',header)
        if v != None:
            value = jsonpath(res.json(),'$..'+ v)[0]
            self.value = self.value.replace('${'+v+'}',value)
        return self.header,self.value
