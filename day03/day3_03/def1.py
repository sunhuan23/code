"""
需求: 用户到ATM机取钱: 1. 输入密码后显示"选择功能"界面
2. 查询余额后显示"选择功能"界面
3. 取2000钱后显示"选择功能"界面

"""
# print("-"*20)
# print("1查询余额")
# print("2存款")
# print("3取款")
# print("-"*20)
#
# p = int(input("请输入你的操作："))
#
# def master():
#     if p == 1:
#         money()
#     elif p == 2:
#         del_money()
#     elif p == 3:
#         add_money()
#
# def money():
#     m = 100
#     print(f"余额{m}")
# def del_money():
#     print("取了100")
# def add_money():
#     print("存了100")
# master()


"""
函数的参数
"""
def num(a,b):
    print(a + b)
num(1,2)

"""
函数的返回值
"""
def num(a,b):
    return a + b
print(num(3, 4))

"""
函数的说明文档
"""
def num(a,b):
    """
    实现 两个数相加和
    :param a: 一个数字
    :param b: 一个数字
    :return: 返回两个数相加和
    """
    return a+b
help(num)

"""
函数的嵌套
"""
# 1. 打印一条横线
def t1():
    print("-"*10)

# 2. 打印多条横线
def t2(a):
    i = 0
    while i < a:
        t1()
        i += 1

t2(3)

