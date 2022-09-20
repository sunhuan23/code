# # 绝对值
# print(abs(-10))
# # 四舍五入
# print(round(1.6))
#
# def fun1(a, b):
#     res = abs(a) + abs(b)
#     return res
#
# print(fun1(5, -5))
#
# def fun2(a,b,f):
#     res = f(a) + f(b)
#     return res
# print(fun2(5 ,-5,abs))
# print(fun2(1.5 ,2.5,round))

list1 = [1, 2, 3, 4, 5,6 ,7, 8]
# map,将列表中的每个元素赋值给fun1的a
def fun1(a):
    return a **2
res = map(fun1, list1)
print(list(res))

# reduce,中的fun2必须有两个参数，将列表中的前两个值给a和b，之后a是两个数的和，b是list中的元素
# 相当于累加和
def fun2(a, b):
    return a + b
import functools
res = functools.reduce(fun2, list1)
print(res)

# filter，fun3中为true的元素，返回一个对象
def fun3(a):
    return a % 2 ==0
res = filter(fun3, list1)
print(list(res))


