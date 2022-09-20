import re
from common.ConfigHttp import ConfigHttp
from jsonpath import jsonpath
"""
1、封装一个接口依赖的类
    1、定义一个初始化方法，
        获取所有的用例，后期需要执行前置用例
    2、定义一个interfaceRely方法，当前用例
        判断是否有依赖，caseid是否不为空
            是，提取需要依赖的字段
            根据caseid执行前置用例
            将执行结果替换
            返回替换好的header，value 
        否，返回现有的header，value
    3、定义一个获取依赖字段的方法，data（header/value）
        使用断言将的数据提取出来
        判断提取的数据是否不为空
            是，取列表第一个
            否 空
            返回提取的数据
    4、定义一个执行前置用例的方法，caseid，header，value
        在所有用例中取到前置用例（caseid-1）
        执行前置用例
        判断header是否不为空
            是，获取请求头中的header
        判断value是否不为空
            是，获取响应中value
        将header和value返回   
"""
# 1、封装一个接口依赖的类
class InterfaceRely:
    #     1、定义一个初始化方法，
    def __init__(self,datalist,kwargs):
        #         获取所有的用例，后期需要执行前置用例
        self.datalist = datalist
        self.rely = kwargs['rely']
        self.caseid = kwargs['caseid']
        self.header = kwargs['header']
        self.value = kwargs['value']
    #     2、定义一个interfaceRely方法，当前用例
    def interfaceRely(self):
        #         判断是否有依赖，caseid是否不为空
        if self.rely.lower() == 'y' and self.caseid != '':
            #             是，提取需要依赖的字段
            h = self.get_pre(self.header)
            v = self.get_pre(self.value)
            return self.pre_run(h,v)
            #             根据caseid执行前置用例
            #             将执行结果替换
            #             返回替换好的header，value
            #         否，返回现有的header，value
    #     3、定义一个获取依赖字段的方法，data（header/value）
        return self.header,self.value
    def get_pre(self,data):
        #         使用断言将的数据提取出来
        res = re.findall(r"\${(.*?)}", data)
        #         判断提取的数据是否不为空
        if len(res)>0:
            #             是，取列表第一个
            res_data = res[0]
            #             否 空
        else:
            res_data = None
        return res_data
            #             返回提取的数据
    #     4、定义一个执行前置用例的方法并替换原始数据，caseid，header，value
    def pre_run(self,header=None,value=None):
        #         在所有用例中取到前置用例（caseid-1）
        casedata = self.datalist[int(self.caseid) - 1]
        #         执行前置用例
        ch = ConfigHttp(casedata)
        res = ch.configHttp()
        #         判断header是否不为空
        if header != None:
            #             是，获取请求头中的header
            h = res.headers[header]
            self.header = self.header.replace('${'+header+'}',h)
        #         判断value是否不为空
        if value != None:
            #             是，获取响应中value
            v = jsonpath(res.json(),'$..'+value)[0]
            self.value =self.value.replace('${'+header+'}',v)
            #         将header和value返回
        return self.header,self.value

if __name__ == '__main__':
    data = 'a'
    pre = InterfaceRely(data)
    print(pre.get_pre("{'name':'${username}','link':'www.baidu.com'}"))
