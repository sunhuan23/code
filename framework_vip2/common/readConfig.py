import os
from configparser import ConfigParser

"""
导包
1、定义一个类
    定义一个初始化方法
        获取config.ini路径
        实例化ConfigParser
        读取config数据
    定义一个读取section的方法
    定义一个读取option的方法
"""
# 1、定义一个类
class ReadConfig:
    #     定义一个初始化方法
    def __init__(self):
        #         获取config.ini路径
        self.config_path = os.path.dirname(os.path.dirname(__file__))+'/config.ini'
        #         实例化ConfigParser
        self.con = ConfigParser()
        #         读取config数据
        self.con.read(self.config_path,encoding='utf-8')
        self.dict1 = {}
    #     定义一个读取section的方法
    # def get_section(self,section):
    #
    #     # return self.con.options(section)
    #     return self.con.items(section)
    # #     定义一个读取option的方法
    # def get_option(self,section,option):
    #     return  self.con.get(section,option)
    def get_config(self,section,option=None):
        if option is None:
            a = self.con.items(section)
            for i in a:
                self.dict1[i[0]] = i[1]

            return self.dict1
        else:
            return self.con.get(section,option)
if __name__ == '__main__':
    re = ReadConfig()
    # print(re.get_section("mysql"))
    # print(re.get_option('mysql','host'))
    print(re.get_config('mysql','host'))