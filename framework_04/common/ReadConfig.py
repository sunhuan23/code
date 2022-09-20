from configparser import ConfigParser
import os
"""
定义一个读取配置文件的类
    定义一个初始化的方法
    获取配置文件路径
    初始化configparser
    定义一个读取配置文件的方法，  section，option
    判断传参数量
    如果一个，读取某个section的option
    如果两个，读取section的指定option的值
"""
class ReadConfig:
    def __init__(self):
        self.confpath = os.path.dirname(os.path.dirname(__file__)) +'/config.ini'
        self.con = ConfigParser()
        self.con.read(self.confpath)
    def readConfig(self,section,option=None):
        if option == None:
            datalist = self.con.items(section)
            data_dict = {i[0]:i[1] for i in datalist}
            return data_dict
        else:
            return self.con.get(section,option)
if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.readConfig('email'))