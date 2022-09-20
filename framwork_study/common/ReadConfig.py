from configparser import ConfigParser
import os
"""
定义一个读取配置文件的类
    定义一个初始化方法
        获取配置文件路径
        实例化configparser
        读取config文件内容
    定义一个读取获取配置文件的方法
        判断参数个数
        一个获取某个section的option
        两个获取指定section的指定option的值
"""
class ReadConfoig:
    def __init__(self):
        self.configpath = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
        self.con = ConfigParser()
        self.con.read(self.configpath)
        self.config = {}
    def readConfig(self,section,option=None):
        if option == None:
            config_list = self.con.items(section)
            for i in config_list:
                self.config[i[0]] = i[1]
            return self.config
        else:
            config = self.con.get(section,option)
            return config
if __name__ == '__main__':
    rc = ReadConfoig()
    print(rc.readConfig('email'))
