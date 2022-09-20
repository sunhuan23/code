# # 1.需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
# import random
# of = [[],[],[]]
# teacher = 1,3,4,6,7,8,5,3
# for i in teacher:
#     ind = random.randint(0,2)
#     of[ind].append(i)
# print(of)
#
# # 2、求100以内能被3整除的数，并将作为列表输出
# list1 = []
# for i in range(1,100):
#     if i % 3 == 0:
#         list1.append(i)
# print(list1)
#
# # 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  #不允许用强制类型转化
# list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
#
# # 4、求斐波那契数列 1 1 2 3 5 8 13 ……
# # 方式一：
# list1 = [1,1]
# for i in range(2,10):
#     list1.append(list1[i-1]+list1[i-2])
# print(list1)
#
# # 方式二：
# list1 = []
# n = 1
# sum = 0
# for i in range(10):
#     if i == 0 or i ==1:
#         list1.append(n)
#     else:
#         sum = list1[i-1] +list1[i-2]
#         n = sum
#         list1.append(n)
# print(list1)
#
# # 5、求100以内的质数（只能被1和它本身整除）
# list1 = []
# for i in range(2,100):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         list1.append(i)
# print(list1)
#
# # 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化
# str1 = "aabbbcddef"
# str2 = ''
# for i in str1:
#     if str1.count(i) == 1:
#         str2 += i
# print(str2)
#
# # 7、有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引
# str1 = "welocme to super&Test"
# list1 = str1.split(' ')[-1].split('&')
# str2 = ''
# for i in list1:
#     str2 += i
# print(str2)
#
# # 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed
# str1 = 'welocme to super&Test'
# list1 = list(str1)
# print(list1)
# for i in range(len(list1)//2):
#     list1[i],list1[-i-1] = list1[-i-1],list1[i]
# str2 = ''.join(list1)
# print(str2)

# 9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长

# 10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
str1 = 'aabbbcddef'
str2 = ''
print(id(str2))
for i in str1:
    if i not in str2:
        str2+=i
print(str2)
print(id(str2))
