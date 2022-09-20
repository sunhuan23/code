import os
import xlrd
import json
import yaml
"""
定义一个读取数据并组装数据的类
    定义一个初始化方法
        获取excel的文件的路径
        获取json文件的路径
        获取yaml文件的路径
    定义一个读取excel的方法
        打开excel
        获取sheet页
        获取最大行
        获取最大列
        获取首行
        获取每一行，进行拼接
        
    定义一个读取json的方法
        打开json文件
        将json转为字典格式
        获取所有的value
        关闭json文件
        将数据添加到列表中
        返回列表

    定义一个读取yaml的方法
        打开yaml文件
        将yaml转为字典格式
        关闭yaml文件
        将数据添加到列表中
        返回列表
"""
class ReadData:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(__file__)) + '/TestData/'
        self.excelpath = self.path +"data.xls"
        self.jsonpath = self.path +"data.json"
        self.yamlpath = self.path +"data.yaml"
        self.listdata = []

    def __read_excel(self,sheet):
        max_row = sheet.nrows
        max_col = sheet.ncols
        first_value = sheet.row_values(0)
        for i in range(1,max_row):
            value = sheet.row_values(i)
            dict1 = {first_value[i]:value[i] for i in range(max_col)}
            self.listdata.append(dict1)
    def readExcel(self,sheet=None):
        workbook = xlrd.open_workbook(self.excelpath)
        if sheet == None:
            sheetname = workbook.sheet_names()
            for i in sheetname:
                sheetname = workbook.sheet_by_name(i)
                self.__read_excel(sheetname)
        else:
            sheetname = workbook.sheet_by_name(sheet)
            self.__read_excel(sheetname)
        return self.listdata
    # 定义一个读取json的方法
    def readJson(self):
    #     打开json文件
        f = open(self.jsonpath,'r')
    #     将json转为字典格式
        dict_data = json.load(f)
    #     获取所有的value
        dict1 = list(dict_data.values())
    #     关闭json文件
        f.close()
    #     将数据添加到列表中
        for i in dict1:
            self.listdata.append(i)
        return self.listdata
    #     返回列表
    # 定义一个读取yaml的方法
    def readYaml(self):
    #     打开yaml文件
        f = open(self.yamlpath)
    #     将yaml转为字典格式
        dict_data = yaml.load(f,Loader=yaml.FullLoader)
    #     关闭yaml文件
        f.close()
    #     将数据添加到列表中
        for i in dict_data:
            self.listdata.append(i)
    #     返回列表
        return self.listdata


if __name__ == '__main__':
    rd = ReadData()
    print(rd.readExcel())
