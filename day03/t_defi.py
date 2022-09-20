# def fun1():
#     print('------------')
#     print('查询余额')
#     print('存款')
#     print('取款')
#     print('------------')
# fun1()
#
# def fun2(x, y):
#     """
#     求两个数的和
#     :param x: 数值类型
#     :param y: 数值类型
#     :return: 返回两个数值的和
#     """
#     sum = x + y
#     return sum
# fresult = fun2(2,4)
# print(fresult)
# help(fun2)

# def line():
#     print('---------')
#
# def line1(num):
#     for i in range(num):
#         line()
# line1(10)

# def sum(x, y, z):
#     return x + y + z
#
# def avg(x,y,z):
#     sum1 = sum(x,y,z)
#     return sum1 / 3
# hav = avg(7, 8, 9)
# print(hav)

# a = 100
# def fun():
#     global a
#     a = 200
#     print(a)
# def fun1():
#     print(a+1)
# fun()
# fun1()
# print(a)

# def user_info(name,age,gender,country='中国'):
#     print(f"您的名字{name}，性别是{gender},年龄是{age},您的国籍是{country}")
# # 位置传参：个数和位置必须一致
# user_info('tom','18','男')
# # 缺省参数，如果没有传参使用默认参数
#
# # 关键字传参：不存在顺序关系，但是位置传参和关键字传参一起使用时位置传参必须在关键字传参前边
# user_info('汤姆',gender='男',age=19)
# user_info(name='汤姆',gender='男',age=19)
# user_info('tom','18','男','m国')
# user_info(country='美国',name='汤姆',gender='男',age=19)

# 不定长穿参
# def user(*args):
#     print(args)
#
# list1 = [1,3]
# user('xiaom','18')
# # 加*是序列中的元素分开在元祖内，不加*是一个列表当做一个元素
# user(*list1)
#
# # 包裹关键字传递
# def user_info(**ywargs):
#     print(ywargs)
# # 可以直接转成字典格式
# user_info(name='xiaom')
# dict1 = {'name':"xiaom",'age':18}
# dict2 = {'name':"xiaom",'age':18}

# # 传递指定的序列，需要加**不然会报错
# user_info(**dict1)
# dict1 = {"name":"xiaom",'age':18}
# # 字典拆包拆的是key，要拆value使用.values,拆键值对.items
# a, b = dict1
# print(a)
# print(b)

def test1(a):
    print(a)
    print(id(a))
    a += a

    print(a)
    print(id(a))
test1(1)
test1([1])
test1((1,))
test1('a')
