import xlrd
import os
"""
1、创建一个读取数据的类
    1、定义一个初始化的方法，init只放属性
        获取excel文件的路径
        获取json文件的路径
        获取yaml文件的路径
        返回给外界使用的组装好数据的列表，默认为空列表
    2、定义一个获取excel数据的方法
        打开文件
        获取sheet页
        获取最大行，测试用例条数
        获取最大列，有多少个键值对
        获取第一行数，得到key
        循环最大行
        获取每一行数据
        将第一行的每一列数据和每一行的每列数据进行组装为一个字典
        将字典添加至列表中
        返回列表
        
        
"""
# 1、创建一个读取数据的类
class ReadData:
    # 1、定义一个初始化的方法，init只放属性
    def __init__(self):
        # 获取excel文件的路径
        self.excelpath = os.path.dirname(os.path.dirname(__file__))+'/testData/data.xls'
        # 获取json文件的路径
        self.jsonlpath = os.path.dirname(os.path.dirname(__file__)) + '/testData/data.json'
        # 获取yaml文件的路径
        self.yamlpath = os.path.dirname(os.path.dirname(__file__)) + '/testData/data.yaml'
        # 返回给外界使用的组装好数据的列表，默认为空列表
        self.data_list = []

    # 2、定义一个获取excel数据的方法
    def readExcel(self):
        # 打开文件
        workbook = xlrd.open_workbook(self.excelpath)
        # 获取sheet页
        sheet = workbook.sheet_by_index(2)
        # 获取最大行，测试用例条数
        max_row = sheet.nrows
        # 获取最大列，有多少个键值对
        max_col = sheet.ncols
        # 获取第一行数，得到key
        first_row = sheet.row_values(0)
        # print(first_row)
        # 循环最大行
        for i in range(1,max_row):
            # 获取每一行数据
            row_value = sheet.row_values(i)
            # 将第一行的每一列数据和每一行的每列数据进行组装为一个字典
            data_dict = {first_row[j]:row_value[j] for j in range(max_col)}
            # data_dict={}
            # for i in range(max_col):
            #     data_dict[first_row[i]] =row_value[i]
            # 将字典添加至列表中
            self.data_list.append(data_dict)
        # 返回列表
        return self.data_list



if __name__ == '__main__':
    rd = ReadData()
    print(rd.readExcel())
    # list1 = ['a','b']
    # list2 = [1,2]
    # dict1 = {}
    # # dict1[list1[0]] =list2[0]
    # for i in range(len(list1)):
    #     dict1[list1[i]] = list2[i]
    # print(dict1)