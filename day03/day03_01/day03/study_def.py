def func1():
    print('-'*20)
    print('查询余额')
    print('取钱')
    print('查询余额')
    print('取卡')
    print('-'*20)

print('密码输入成功')
func1()

# 完成需求如下: 一个函数完成两个数1和2的加法运算,如何书写程序?
# 一：
def sum():
    a = 1+2
    print(a)
sum()

# 二：带参数
def sum1(a, b):
    c = a + b
    print(c)
sum1(1, 2)

# 需求: 制作一个计算器, 计算任意两数字之和, 并保存结果。

def sum2(a, b):
    """
    计算两个数的和并返回结果

    """
    return a+b

print(sum2(2,3))
help(sum2)

"""
函数嵌套
所谓函数嵌套调用指的是一个函数里面又调用了另外一个函数。
"""
def testB():
    print('---- testB start----')
    print('这里是testB函数执行的代码')
    print('---- testB end----')
def testA():
    print('---- testA start----')
    testB()
    print('---- testA end----')
testA()

# 打印一条横线
def print_line():
    print('-'*20)

# 打印多行

def num(num):
    i = 0
    while i< num:
        print_line()
        i+=1
num(10)


# 1. 求三个数之和
def sum_num(a, b, c):
    return a + b + c
print(sum_num(1, 2, 4))


# 求三个数平均值
def avg_num(a, b, c):
    return sum_num(a,b,c) / 3
print(avg_num(2,5,10))

# 位置函数
def func(name,age,gender,country ='中国'):
    print(f'我的名字是{name},我的年龄是{age},我的性别是{gender}，我的国家是{country}')
func('rose',19,'男')
# 关键字参数
func(name='小名', gender='女',age=22)
func('小名', gender='女',age=22)
func('rose',19,'男','美国')
func('rose',19,gender='男',country='美国')


def func(*args):

    print(args[0])
func(1,2,3,4,6)
dict1 = {'name':'rose','age' :18}
def func(**kwargs):
    print(kwargs['name'])
    print(kwargs)
func(name = 'xiaom',age=18)
func(**dict1)

