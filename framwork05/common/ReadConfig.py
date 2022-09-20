from configparser import ConfigParser
import os

"""
定义一个读取配置文件的类
    定义一个初始化方法
        获取config文件地址
        实例化configparser
        抵用读取的方法
    定义一个给外界调用的方法
        判断section和option
"""
class ReadConfig:
    def __init__(self):
        self.con_path =os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
        self.con = ConfigParser()
        self.con.read(self.con_path)
    def readConfig(self,section,option=None):
        if option ==None:
            data = self.con.items(section)
            data_dict = {i[0]:i[1] for i in data}
            return data_dict
        else:
            data = self.con.get(section,option)
            return data
if __name__ == '__main__':
    rd = ReadConfig()
    print(rd.readConfig('email'))