

# map（）
# def func1(num):
#     return num ** 2
# list1=[2,6,3,6,7,4,6,8]
# res = map(func1, list1)
# print(list(res))

# reduce（）
# import functools
# def func1(a,b):
#     return a + b
# list1=[2,6,3,6,7,4,6,8]
# result = functools.reduce(func1,list1)
# print(result)

# filter（）

list1=[2,6,3,6,7,4,6,8]
def func1(a):
    return a % 2 == 0
result = filter(func1,list1)
print(list(result))