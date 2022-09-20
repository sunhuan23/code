from configparser import ConfigParser
import os
"""
定义一个读取配置文件的类：
    定义一个初始化方法
        1、获取配置文件的路径
        2、实例化Configparser
        3、读取config文件数据
    定义一个获取配置信息的方法
        需要两个参数
        判断如果传入一个参数则是获取option信息
        如果传入两个参数则是获取section信息
"""
class ReadConfig:
    def __init__(self):
        self.config_path = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
        self.conf = ConfigParser()
        self.conf.read(self.config_path)
        self.config = {}
    def get_config(self,section,option=None):
        if option is None:
            # 获取option的key
            # return self.conf.options(section)

            # 获取option的k，v
            tup = self.conf.items(section)
            for i in tup:
                self.config[i[0]] = i[1]
            return self.config

        else:
            return self.conf.get(section,option)

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.get_config('email'))
    print(rc.get_config('mysql','host'))
