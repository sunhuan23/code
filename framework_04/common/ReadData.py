import xlrd
import json
import yaml
import os
"""
读取excel，json，yaml
将数据组装成字典并放在列表中
"""
"""
1、定义一个读取数据的类
    1、定义一个初始化方法
        excel路径
        json路径
        yaml路径
        组装好的数据，空列表
    2、定义一个方法用来搭配excel使用，sheet
        1、获取最大行
        2、获取最大列
        3、获取首行内容，作为用例的key
        4、循环每一行的用例
            将首行和每一行的数据进行组装
            将组装好的数据添加到列表中
        返回列表
    3、定义一个读取excel的方法，sheet页的名字，默认为空
        打开excel
        获取sheet页所以名称
        判断sheet为None
            遍历每个sheet页
            调用2
        否 
            调用2    
    4、定义一个读取json的方法
        打开json文件
        将内容转为字典格式
        关闭文件
        提取value
        添加到列表
    5、定义一个读取yaml的方法
        打开yaml文件
        将内容转为字典格式
        关闭文件
        将数据添加到列表
"""
class ReadData:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(__file__)) + '/TestData'
        self.excelpath = self.path + '/data.xls'
        self.jsonpath = self.path + '/data.json'
        self.yamlpath = self.path + '/data.yaml'
        self.datalist = []

    def __get_excel(self,sheet):
        """
            2、定义一个方法用来搭配excel使用，sheet
        1、获取最大行
        2、获取最大列
        3、获取首行内容，作为用例的key
        4、循环每一行的用例
            将首行和每一行的数据进行组装
            将组装好的数据添加到列表中
        返回列表
        :param sheet:
        :return:
        """
        max_row = sheet.nrows
        max_col = sheet.ncols
        first_value = sheet.row_values(0)
        for i in range(1,max_row):
            value = sheet.row_values(i)
            dict1 = {first_value[j]:value[j] for j in range(max_col)}
            self.datalist.append(dict1)

    def readExcel(self,sheet=None):
        """
            3、定义一个读取excel的方法，sheet页的名字，默认为空
        打开excel
        获取sheet页所以名称
        判断sheet为None
            遍历每个sheet页
            调用2
        否
            调用2
        :param sheet: sheet页名称
        :return: 返回组装好的列表
        """
        workbook = xlrd.open_workbook(self.excelpath)
        sheetname = workbook.sheet_names()
        if sheet == None:
            for i in sheetname:
                sheet = workbook.sheet_by_name(i)
                self.__get_excel(sheet)

        else:
            sheet = workbook.sheet_by_name(sheet)
            self.__get_excel(sheet)
        return self.datalist

    def readJson(self):
        """
        4、定义一个读取json的方法
        打开json文件
        读取json内容
        将内容转为字典格式
        关闭文件
        提取value
        添加到列表
        :return:组装好的列表
        """
        f = open(self.jsonpath,'r')
        data_dict = json.load(f)
        data =list(data_dict.values())
        f.close()
        return data


    def readYaml(self):
        """
        5、定义一个读取yaml的方法
        打开yaml文件
        将内容转为字典格式
        关闭文件
        将数据添加到列表
        :return: 组装好的列表
        """
        f = open(self.yamlpath,'r')
        data = yaml.load(f,Loader=yaml.FullLoader)
        f.close()
        return data





if __name__ == '__main__':
    r = ReadData()
    print(r.readExcel())
    # print(r.readJson())
    # r.readYaml()



