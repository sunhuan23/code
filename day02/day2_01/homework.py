# 1.需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
import random

classroom = [[], [], []]
teacher = ['小明', '小红', 'rose', '杰克', '菲菲', 'lily', '娜娜', '小强']
for i in range(len(teacher)):
    t_index = random.randint(0, 2)
    classroom[t_index].append(teacher[i])
print(classroom)

# 2、求100以内能被3整除的数，并将作为列表输出
num_list = []
for i in range(1, 100):
    if i % 3 == 0:
        num_list.append(i)
print(num_list)
# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表  #不允许用强制类型转化
num_list1 = [1, 2, 3, 4, 3, 4, 2, 5, 5, 8, 9, 7]
only_list = []
for i in num_list1:
    if i not in only_list:
        only_list.append(i)
print(only_list)

# 4、求斐波那契数列 1 1 2 3 5 8 13 ……
Fi = [0, 1]
for i in range(20):
    Fi.append(Fi[-1] + Fi[-2])
print(Fi)

# 5、求100以内的质数（只能被1和它本身整除）
numbers = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        numbers.append(i)
print(numbers)

# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef #不允许用类型转化
str1 = 'aabbbcddef'
for i in range(len(str1)):
    if str1.count(str1[i]) == 1:
        print(str1[i], end='')


# 7、有一堆字符串，“welocme to super&Test”，打印出superTest，#不能查字符的索引
super_str = 'welocme to super&Test'
result_list = super_str.split(' ')[2].split('&')
for i in result_list:
    print(i, end='')

# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ... #不允许用reverse,和reversed
str1 = 'welocme to super&Test'
list_str = list(str1)
for i in range(0,len(list_str)//2):
    for j in range(len(list_str)-1-i, len(list_str)//2,-1):
        list_str[i],list_str[j] = list_str[j],list_str[i]
        break
reverse_str = "".join(list_str)
print(reverse_str)


# 9、有一堆字符串，“abcdef”，将首尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现,不允许用步长
str2 = 'abcdef'
reverse_str = ''
for i in range(len(str2)-1,-1,-1):
    reverse_str += str2[i]
print(reverse_str)

# 10、有一堆字符串，“aabbbcddef”，输出abcdef # 不允许用set
str3 = 'aabbbcddef'
d_str3 = ''
for i in str3:
    if i not in d_str3:
        d_str3 += i
print(d_str3)