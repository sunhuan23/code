# import re
# from common.ConfigHttp import ConfigHttp
# from jsonpath import jsonpath
# """
# 1、定义一个类，处理接口依赖
#     定义一个初始化方法
#     接收header和value，caseid，依赖
#     定义一个解决依赖的方法
#     判断是否有依赖
#     有，进行正则提取
#         进行请求前置接口
#         替换
#         返回header，value
#     没有返回header和value
# """
# class InterfaceRely:
#     def __init__(self,datalist,kwargs):
#         self.datalist = datalist
#         self.header = kwargs['header']
#         self.value = kwargs['value']
#         self.caseid = kwargs['caseid']
#         self.rely = kwargs['rely']
#
#
#     def interfaceRely(self):
#         if self.rely.lower() == 'y' and self.caseid != None:
#             h = self.get_rely(self.header)
#             v = self.get_rely(self.value)
#             header,value = self.pre_case(h,v)
#             if header != None:
#                 self.header = self.header.replace('${'+h+'}',header)
#             if value != None:
#                 self.value = self.value.replace('${'+v+'}',value)
#
#
#             return self.header,self.value
#         else:
#             print('返回原数据')
#             return self.header,self.value
#
#
#     def get_rely(self,data):
#         res = re.findall('\${(.*?)}',data)
#         if len(res) > 0:
#             data = res[0]
#         else:
#             data = None
#         return data
#
#
#     def pre_case(self,header=None,value=None):
#         case = self.datalist[int(self.caseid)-1]
#         ch  = ConfigHttp(case)
#         res = ch.configHttp()
#         if header != None:
#             header = res.headers[header]
#         if value != None:
#             value =jsonpath(res.json(),'$..'+ value)[0]
#         return header,value
import re
from common.ConfigHttp import ConfigHttp
from jsonpath import jsonpath
"""
1、定义一个类，处理接口依赖
    定义一个初始化方法
    接收header和value，caseid，依赖
    定义一个解决依赖的方法
    判断是否有依赖
    有，进行正则提取
        进行请求前置接口
        替换
        返回header，value
    没有返回header和value
"""
class InterfaceRely:
    def __init__(self,datalist,kwargs):
        self.datalist = datalist
        self.header = kwargs['header']
        self.value = kwargs['value']
        self.caseid = kwargs['caseid']
        self.rely = kwargs['rely']


    def interfaceRely(self):
        if self.rely.lower() == 'y' and self.caseid != None:
            h = self.get_rely(self.header)
            v = self.get_rely(self.value)
            self.header,self.value = self.pre_case(h,v)



            return self.header,self.value
        else:
            print('返回原数据')
            return self.header,self.value


    def get_rely(self,data):
        res = re.findall('\${(.*?)}',data)
        if len(res) > 0:
            data = res[0]
        else:
            data = None
        return data


    def pre_case(self,header=None,value=None):
        case = self.datalist[int(self.caseid)-1]
        ch  = ConfigHttp(case)
        res = ch.configHttp()
        if header != None:
            h = res.headers[header]
            self.header = self.header.replace('${' + header + '}', h)
        if value != None:
            v =jsonpath(res.json(),'$..'+ value)[0]
            self.value = self.value.replace('${' + value + '}', v)
        return self.header,self.value