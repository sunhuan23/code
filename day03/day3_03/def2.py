import os
"""
局部变量
全局变量 global
"""
b = 200
def t1():
    global a
    a = 100
    print(a)
t1()
print(b)
print(a)

"""
返回值作为参数传递
"""
def num(a,b):
    return a + b

def num1(num):
    return num +1


print(num1(num(1, 2)))

"""
多参数，
"""
def n(name,age,county):
    print(f"{age},{name},{county}")

n('小明',19,'北京')
"""
关键字参数
"""
def n(name,age,county):
    print(f"{name},{age},{county}")
n('小明',county='北京',age=19)

"""
缺省参数
"""
def n(name,age=19,county='北京'):
    print(f"{name},{age},{county}")
n('小明',county='北京',age=20)
n('小红')


"""
不定长传参
"""
def num(*args):
    for i in args:
        print(i)
    print(args)

num(*[1,2,4])


def num(**kwargs):
    for i in kwargs:
        print(i)
num(a=1,b=2)
dict1 = {'name':"xiaom"}
num(**dict1)
"""
文件
"""
# with open('info.txt','r',encoding='utf-8') as f:
#     print(f.read(0))
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())


"""
os
"""
# 修改文件名称
# os.rename('info.txt','info1.txt')
# 删除文件
# os.remove("/Users/sunhuan/chenghao/day11/day3/info1.txt")
# 创建文件夹
# os.mkdir("info")
# 删除文件夹
# os.rmdir('info')
# 获取当前目录
print(os.getcwd())
# 改变默认目录
# os.chdir('/Users/sunhuan/chenghao')
# print(os.getcwd())
print(os.listdir(os.path.dirname(__file__)))
print(os.path.dirname('/Users/sunhuan/chenghao/day11'))