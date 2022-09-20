# 1.使用列表推导式生成能被5整除的数（100以内）

list1 = [i for i in range(100) if i % 5 == 0]
print(list1)

# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
list1 = ["小明", "小红"]
list2 = [18, 19]
dict1 = {}

for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)

# 斐波那契
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-2) + fib(n-1)
res = fib(6)
print(res)

list3 = [{'name':'q'}]
def l():
    global list3
    for i in list3:
        print(i)
l()