from common.readData import ReadData
from common.log import logger
import re
from common.configHttp import ConfigHttp
from jsonpath import jsonpath
"""
定义一个类
1. 定义初始化方法
1.1 获取所有测试用例并绑定为实例属性
2. 定义一个方法:根据当前的用例id,执行依赖的前置用例并返回替换好的header和body
2.1 获取用于判断是否有前置用例的关键字段:rely,caseid,header,value
2.2 判断是否有前置用例,判断caseid是否不为空:
2.2.1 是:根据正则找到请求头/体里面依赖的字段:?可以封装成一个独立方法进行调用
2.2.2 执行前置用例得到返回结果,在返回结果里获取依赖字段数据?可以封装一个前置用例方法
2.2.3 获取到依赖的字段替换原来的数据
2.2.4 返回替换好的header和body
2.3 否:返回当前的header和body

3. 定义一个方法:提取需要依赖的请求头/体的字段
3.1 根据正则提取依赖字段,得到一个列表
3.2 判断得到的列表是否有数据
3.2.1 是:返回依赖字段
3.2.2 否:返回个None

4.定义一个方法:执行前置用例,根据准备好的目标字段提取实际的数据:头/体
4.1 准备前置用例请求所需要的数据
4.2 调用confighttp进行请求,并获得结果
4.3 判断请求头里面是否有依赖数据,有则根据依赖进行替换
4.4 判断请求体里面是否有依赖数据,有则根基依赖进行替换
4.5 返回依赖字段
"""

# 定义一个类
class PreSolve:
    # 1. 定义初始化方法
    def __init__(self,datalist):
        # 1.1 获取所有测试用例并绑定为实例属性
        self.datalist = datalist
    # 2. 定义一个方法:根据当前的用例id,执行依赖的前置用例并返回替换好的header和body
    def preSolve(self,dic):
        # 2.1 获取用于判断是否有前置用例的关键字段:rely,caseid,header,value
        rely = dic['rely']
        caseid = dic['caseid']
        header = dic['header']
        value = dic['value']
        # 2.2 判断是否有前置用例,判断caseid是否不为空:
        if rely.lower() == 'y' and caseid != '':
            # 2.2.1 是:根据正则找到请求头/体里面依赖的字段:?可以封装成一个独立方法进行调用
            gola_h = self.get_predata(header)
            gola_b = self.get_predata(value)
            # 2.2.2 执行前置用例得到返回结果,在返回结果里获取依赖字段数据?可以封装一个前置用例方法
            h,b = self.run_pre(caseid,gola_h,gola_b)
            if h != None:
                # 2.2.3 获取到依赖的字段替换原来的数据
                header = header.replace('${'+gola_h+'}',h)
            if b != None:
                value = value.replace('${'+gola_b+'}',b)

            # 2.2.4 返回替换好的header和body
            return header,value
        # 2.3 否:返回当前的header和body
        else:
            print('返回原有数据')
            return header,value
    # 3. 定义一个方法:提取需要依赖的请求头/体的字段
    def get_predata(self,data):
        # 3.1 根据正则提取依赖字段,得到一个列表
        res = re.findall(r'\${(.*?)}', data)
        # 3.2 判断得到的列表是否有数据
        if len(res)>0:
            # 3.2.1 是:返回依赖字段
            resdata = res[0]
        else:
            # 3.2.2 否:返回个None
            resdata =  None
        return resdata

    # 4.定义一个方法: 执行前置用例, 根据准备好的目标字段提取实际的数据: 头 / 体
    def run_pre(self,caseid,gola_h=None,gola_b=None):
        # 4.1 准备前置用例请求所需要的数据
        data = self.datalist[int(caseid)-1]
        # 4.2 调用confighttp进行请求,并获得结果
        ch = ConfigHttp(data)
        res = ch.run()
        # 4.3 判断请求头里面是否有依赖数据,有则根据依赖进行替换
        if gola_h is not None:
            gola_h =res.headers[gola_h]
        # 4.4 判断请求体里面是否有依赖数据,有则根基依赖进行替换
        if gola_b is not None:
            gola_b =jsonpath(res.json(),'$..'+ gola_b)[0]
        return gola_h,gola_b

        # 4.5 返回依赖字段



if __name__ == '__main__':
    rd = ReadData()
    data = rd.read_excl()
    ps = PreSolve(data)
    ps.preSolve(data[3])
    print(ps.get_predata(data[3]['header']))
    print(ps.get_predata(data[4]['header']))
    print(ps.run_pre('1', 'Set-Cookie', 'username'))
    print(ps.preSolve(data[0]))

