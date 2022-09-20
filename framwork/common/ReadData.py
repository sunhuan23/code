import xlrd
import os
import json
import yaml
"""
1、创建一个读取数据的类
    1.1 定义一个初始化方法
        获取excel文件目录
        获取json文件目录
        获取yaml文件目录
        最终返回的数据列表datalist=[]
    1.2 定义一个读取excel的方法
        1、打开excel
        2、获取sheet页
        3、获取最大行，可以知道有多少条用例
        4、获取最大列，可以知道有多少个键值对
        5、获取首行，key值
        6、获取每一行测试数据
        7、循环每一行的数据和key组成一个字典格式
        8、将组装好的数据添加至列表中
        9、将列表返回
    1.3 定义一个读取json的方法
        1、打开json文件
        2、将json转为字典
        3、读取字典的所有value
        4、关闭json文件
        5、将数据添加至列表
        6、返回列表
    1.4 定义一个读取yaml的方法
        1、打开yaml文件
        2、将数据转为字典
        3、关闭yaml文件
        4、将数据添加至列表中
        5、将列表返回
"""
# 1、创建一个读取数据的类
class ReadData:
    #     1.1 定义一个初始化方法
    def __init__(self):
        #         获取excel文件目录
        self.excelpath = os.path.dirname(os.path.dirname(__file__))+'/testData/data.xls'
        #         获取json文件目录
        self.jsonpath = os.path.dirname(os.path.dirname(__file__))+'/testData/data.json'
        #         获取yaml文件目录
        self.yamlpath = os.path.dirname(os.path.dirname(__file__))+'/testData/data.yaml'
        #         最终返回的数据列表datalist=[]
        self.datalist = []
    #     1.2 定义一个读取excel的方法
    def __readexcel(self,sheet):
        #         获取最大行，可以知道有多少条用例
        max_row = sheet.nrows
        #         获取最大列，可以知道有多少个键值对
        max_col = sheet.ncols
        #         获取首行，key值
        first_row = sheet.row_values(0)
        #         获取每一行测试数据
        #         循环每一行的数据和key组成一个字典格式
        for i in range(1, max_row):
            row_value = sheet.row_values(i)
            data_dict = {first_row[j]: row_value[j] for j in range(max_col)}
            self.datalist.append(data_dict)
        return self.datalist



    def readExcel(self,sheetname=None):
        #         1、打开excel
        workbook = xlrd.open_workbook(self.excelpath)
        #         2、获取所有sheet页的名字
        sheet_name = workbook.sheet_names()
        # 如果调用方法没有传入sheetname，会获取所有的sheet页的内容
        if sheetname is None:
            for i in sheet_name:
                sheet = workbook.sheet_by_name(i)
                data = self.__readexcel(sheet)
            return data
        else:
            sheet = workbook.sheet_by_name(sheetname)
            return self.__readexcel(sheet)


    def readJson(self):
        # 1、打开json文件
        f = open(self.jsonpath,'r')
        # 2、将json转为字典
        all_dict = json.load(f)
        # 3、关闭json文件
        f.close()
        # 4、读取字典的所有value
        value_dict = all_dict.values()
        # 5、将数据添加至列表
        self.datalist.append(list(value_dict))
        # 6、返回列表
        return self.datalist

    def readYaml(self):
        # 1、打开yaml文件
        f = open(self.yamlpath,'r')
        # 2、将数据转为字典
        data_dict = yaml.load(f,Loader=(yaml.FullLoader))
        # 3、关闭yaml文件
        f.close()
        # 4、将数据添加至列表中
        self.datalist.append(data_dict)
        # 5、将列表返回
        return self.datalist

if __name__ == '__main__':
    excel = ReadData()
    print(excel.readExcel())