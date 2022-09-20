def sum_numbers(num):
    if num == 1:
        return 1
    return num + sum_numbers(num - 1)
sum_result = sum_numbers(4)

"""
lambda表达式
"""
def fn1():
    return 200

a = lambda : 200
print(a())

b = lambda a,b:a + b
"""
默认参数
"""
c = lambda a,b, c=100:a + b + c
print(c(1,3))

d = lambda *args: args
print(d(*[12,2]))
e = lambda **kwargs : kwargs["小明"]

dict1 = {"小明":19}
print(e(**dict1))

students = [ {'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19}, {'name': 'Jack', 'age': 22}]
students.sort(key=lambda x : x["name"])
students.sort(key=lambda x : x["age"],reverse=True)

print(students)


"""
高阶函数
"""

"""
数字的绝对值
"""
print(abs(-100))

"""
对数字进行四舍五入,如果是1.5结果为2，如果是2.5结果还是2，结果更靠近偶数
"""
print(round(2.5))

"""
任意两个数字, 按照指定要求整理数字后在进行求和计算
"""
def sum(a,b,f):
    return f(a) + f(b)


print(sum(-100, 10, abs))
print(sum(1.5,3.4,round))


"""
需求:计算list1序列中各个数字的2次方。
"""
list1 = [1, 2, 3, 4, 5]
def func(x):
    return x ** 2
result = map(func,list1)
print(list(result))

"""
计算list1序列中各个数字的累加和
"""
import functools
list1 = [1,2,3,4,5]
def func(a,b):
    return a + b
result = functools.reduce(func,list1)
print(result)

"""
filter(func, Ist)函数用于过滤序列,过滤掉不符合条件的元素,返回一个filter对象。如果要转换为列表,可以
使用list()来转换
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def func(a):
    return a % 2 == 0
result = filter(func,list1)
print(list(result))

