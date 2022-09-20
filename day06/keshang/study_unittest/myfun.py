# coding:utf-8
# -----看做开发写好的接口代码/函数、方法---被测代码
def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multi(a, b):
    return a * b


def divide(a, b):
    return a / b

a = input("输入：")
dict1 = eval(a)
print(dict1)
print(type(dict1))