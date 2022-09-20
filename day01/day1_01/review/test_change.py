"""
int(x)   ： 将x转换为一个整数
float(x) ： 将x转换为一个浮点数
str(x)   ： 将对象x转换为字符串
tuple(s) ： 将序列s转换为一个元组
list(s)  ： 将序列s转换为一个列表
eval(str)： 用来计算在字符串中的有效Python表达式,并返回一个对象
"""
a = "123"  # -->str
print(type(a))
print(type(eval(a)))  # -->int，返回"123"中的表达式123

b = 11    # -->int
print(type(b))
print(type(float(b)))  # 转为浮点数，11.0

c = "11.1"  # -->str
print(type(eval(c)))  # -->float，返回"11.1"中的表达式11.1

l = [1, 2, 3, "hh"]  # -->list
print(type(l))
l = tuple(l)  # --> 转元祖
print(type(l))  # --> tuple
l = list(l)
print(type(l))

