import xlrd
import os
import json
import yaml
# 打开ecxel
# 绝对路径
# readbook = xlrd.open_workbook('/Users/sunhuan/chenghao/framework_vip2/testData/data.xls')

# 相对路径
# file_path = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
# readbook = xlrd.open_workbook(file_path)
#
# print(file_path)
# #  获取指定sheet页
# # sheet = readbook.sheet_by_index(0)
# sheet = readbook.sheet_by_name('sheet1')
# # 获取所有sheet页的名称
# print(readbook.sheet_names())
#
# # 获取最大行/列
# max_row = sheet.nrows
# max_col = sheet.ncols
# print(max_row)
# print(max_col)
#
# # 获取某个单元格的值
# cell_value = sheet.cell_value(0,1)
# print(cell_value)
#
# # 获取某行/列的数据
# row_value = sheet.row_values(0)
# print(row_value)
# col_value = sheet.col_values(1)
# print(col_value)
#
# list1 = ["name","age","sex"]
# list2 = ["tom",18,"男"]
#
# # 方式一
# dict1 = {}
# for i in range(len(list1)):
#     dict1[list1[i]] = list2[i]
# print(dict1)
# # 方式二
# dict2 = {list1[i] : list2[i] for i in range(len(list1)) }
# print(dict2)
#
# # zip实现
# dict3 =dict(zip(list1, list2))
# print(dict3)
"""
定义一个类：
1、创建一个init初始化方法
    1.1 获取文件路径
    1.2 打开文件
    1.3 获取指定sheet页
    1.4 获取文件的最大行
    1.5 获取文件的最大列
    1.6 获取文件的第一行数据作为key
    1.7 返回一个组装好的列表
2、定义一个组装数据的对外方法
    循环取出每一行的数据作为测试用例
    2.1 获取每一行数据
    2.2 组装成为一个字典
    2.4 添加到列表中
    2.5 返回列表
3、定义一个读取json的方法
    3.1 获取文件路径
    3.2 打开json文件
    3.3 将json转为字典格式
    3.4 关闭json
    3.5 获取字典的所有value转为列表格式
    3.6 返回列表
4、定义一个读取yaml的方法
    3.1 获取文件路径
    3.2 打开yaml文件
    3.3 将yaml转为字典格式
    3.4 关闭yaml文件
    3.5 获取字典的所有value转为列表格式
    3.6 返回列表
"""
# 定义一个类：
class ReadData:
    # 1、创建一个init初始化方法
    def __init__(self):
        #     1.1 获取文件路径
        self.file_path = os.path.dirname(os.path.dirname(__file__))+ r'/testData/data.xls'
        #     1.2 打开文件
        self.workbook = xlrd.open_workbook(self.file_path)
        #     1.3 获取指定sheet页
        self.sheet = self.workbook.sheet_by_index(1)
        #     1.4 获取文件的最大行
        self.max_row = self.sheet.nrows
        #     1.5 获取文件的最大列
        self.max_col = self.sheet.ncols
        #     1.6 获取文件的第一行数据作为key
        self.frist_row = self.sheet.row_values(0)
        #     1.7 返回一个组装好的列表
        self.res_list1 = []
    # 2、定义一个组装数据的对外方法
    def read_excl(self):
        #     循环取出每一行的数据作为测试用例
        for i in range(1,self.max_row):
            #     2.1 获取每一行数据
            row_value = self.sheet.row_values(i)
            #     2.2 组装成为一个字典
            dict1 = {self.frist_row[j]:row_value[j] for j in range(self.max_col)}
            #     2.4 添加到列表中
            self.res_list1.append(dict1)
        #     2.5 返回列表
        return self.res_list1

    # 3、定义一个读取json的方法
    def read_json(self):
        # 3.1   获取文件路径
        json_path = os.path.dirname(os.path.dirname(__file__))+ r'/testData/data.json'
        # 3.2  打开json文件
        f = open(json_path,'r')
        # 3.3  将json转为字典格式
        json_dict = json.load(f)
        # 3.4    关闭json
        f.close()
        # 3.5    获取字典的所有value转为列表格式
        list_data = list(json_dict.values())
        # 3.6   返回列表
        return list_data

    # 4、定义一个读取yaml的方法
    def read_yaml(self):
        # 3.1    获取文件路径
        yaml_path = os.path.dirname(os.path.dirname(__file__))+ r'/testData/data.yaml'
        # 3.2    打开yaml文件
        f = open(yaml_path, 'r')
        # 3.3    将yaml转为列表
        list_data = yaml.load(f,Loader=yaml.FullLoader)
        # 3.4    关闭yaml文件
        f.close()
        # 3.6 返回列表
        return list_data
if __name__ == '__main__':
    read = ReadData()
    # print(read.read_excl())
    # print(read.read_json())
    print(read.read_yaml())
