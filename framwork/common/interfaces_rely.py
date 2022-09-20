import re
from common.ConfigHttp import ConfigHttp
from jsonpath import jsonpath
"""
1、封装一个类解决接口依赖
    1、定义一个初始化方法
        接收所有用例的数据
    2、定义一个解决依赖的方法
        判断rely是不是y，caseid是不是不为空
            是，通过正则表达式提取出需要依赖的数据
            通过caseid取到需要执行的前置用例
            拿到结果
            替换header或value
    3、定义一个方法提取需要的依赖的字段,data
        将data的数据通过正则提取出来想要的字段
        如果len（）>0
            取第一个数
        else
            返回None
    4、定义一个执行前置用例的方法，caseid，header=None,value=None
        获取需要执行的测试用例
        调用请求类
        将响应转为字典格式
        判断header是否不为空
            取到header
            得到结果后使用jsonpath拿到想要的数据
        判断value是否为空
            取到text
            得到结果后使用jsonpath拿到想要的数据
        返回 header value            
"""

# 封装一个类解决接口依赖
class InterfacesRely:
    #     1、定义一个初始化方法
    def __init__(self,data_list):
        #         接收所有用例的数据
        self.data_list = data_list

    #     2、定义一个解决依赖的方法
    def interfaces_raly(self,kwags):
        #       获取需要的字段
        rely = kwags['rely']
        caseid = kwags['caseid']
        value = kwags['value']
        header = kwags['header']
        #         判断rely是不是y，caseid是不是不为空
        if rely.lower() =='y' and caseid != '':
            #            是，通过正则表达式提取出需要依赖的数据
            golb_h = self.get_data(header)
            golb_b = self.get_data(value)
        #            通过caseid取到需要执行的前置用例
            h,b = self.pre_case(caseid,golb_h,golb_b)
            if h != None:
                header = header.replace("${"+golb_h+"}",h)
            if b != None:
                value = value.replace("${" + golb_b + "}",b)
        #            拿到结果
        #            替换header或value
            return header,value
        else:
            return header,value

    # 提取需要依赖的数据
    def get_data(self,data):
        # 将data的数据通过正则提取出来想要的字段
        res = re.findall(r'\${(.*?)}',data)
        # 判断取出来的时间是否 > 0
        if len(res) > 0:
            resoult = res[0]
        else:
            resoult = None
        return resoult

    # 4、定义一个执行前置用例的方法，caseid，header=None,value=None
    def pre_case(self,caseid,header=None,value=None):
        # 获取需要执行的测试用例
        case_data = self.data_list[int(caseid)-1]
        # 调用请求类
        ch = ConfigHttp(case_data)
        res = ch.configHttp()
        # 判断header是否不为空
        if header != None:
            # 取到header
            header = res.headers[header]
        #        判断value是否为空
        if value != None:
            #            得到结果后使用jsonpath拿到想要的数据
            value = jsonpath(res.json(), '$..' + value)[0]
        #        返回 header value
        return header,value



