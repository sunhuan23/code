import openpyxl
import os

"""
1、获取文件路径
2、打开文件
3、获取文件的sheet页
4、获取最大行
5、获取最大列
6、获取某个单元格
"""
# 1、获取文件路径
filename = os.path.dirname(os.path.dirname(__file__))+'/testData/data.xlsx'
# 2、打开文件
inwb = openpyxl.load_workbook(filename)
# 3、获取文件的sheet页
sheetname = inwb.get_sheet_names()
print(sheetname)
# 4、获取最大行
# 5、获取最大列
# 6、获取某个单元格