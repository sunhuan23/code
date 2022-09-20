"""
字符串
"""
"""
字符串输出
"""
str1 = 'hello'
print(f'{str1}')
print('%s'% str1)

"""
下标
find
index
"""
str2 = 'hello'
# 根据下标取值
print(str2[1])
# find 查找，找不到不会报错,返回-1，找到返回下标
print(str2.find('w'))
# index ,找不到会报错，返回下标
print(str2.index('h'))
# count 查找字符出现的次数
print(str2.count("h"))
"""
切片
[开始下标：结束下标：步长]
特点：去尾不去头
找不到返回0

"""
str3 = 'hello'
# 切片
print(str3[-1:1:-1])
print(str3[-2:1:-2])

"""
修改
replace()替换
replce(老得字符，新的字符，替换个数)
"""
str3 = 'hehlo'
print(str3.replace('h','a',1))

"""
分割
split(分割的字符)
1、返回列表
"""
str4 = 'h，e，l，lo'
list1 = str4.split('，')
print(list1)

"""
连接 join
"""
str4 = 'hello'
st2 = '_'.join(str4)
print(st2)

"""
capitalize()
将字符串第一个字母改成大写
"""
str4 = 'hello'
print(str4.capitalize())

"""
title
将字符串中每个单词的首字母换成大写
"""
str4 = 'hell o aaa bbbccc'
print(str4.title())

"""
lower() 将字符串中所有的字符转为小写
"""
str4 = 'hell o aAa bbbccc'
print(str4.lower())

"""
upper() 将字符串中小写转大写
"""
str4 = 'hell o aAa bbbccc'
print(str4.upper())

"""
lstrip() 删除字符串左侧空格
"""
str4 = '  hell o aAa bbbccc   '
print(str4.lstrip())

"""
rstrip() 删除字符串右侧空格
"""
str4 = '  hell o aAa bbbccc   '
print(str4.rstrip())

"""
strip() 删除字符串两侧空格
"""
str4 = '  hell o aAa bbbccc   '
print(str4.strip())

"""
ljust() 左对齐，返回原数据左对齐，指定字符填充剩余长度
"""
str4 = '  hell o aAa bbbccc   '
print(str4.ljust(30,','))

"""
rjust() 右对齐，返回原数据右对齐，指定字符填充剩余长度
"""
str4 = '  hell o aAa bbbccc   '
print(str4.rjust(30,','))

"""
center() 居中，返回原数据居中，指定字符填充剩余长度
"""
str4 = '  hell o aAa bbbccc   '
print(str4.center(30,','))

"""
startswith（子串，开始位置下标，结束位置下标）
检查字符串是不是以指定子串开头,返回布尔值
"""
str4 = 'hell o aAa bbbccc   '
print(str4.startswith('h'))

"""
endswith（子串，开始位置下标，结束位置下标）
检查字符串是不是以指定子串开头,返回布尔值
"""
str4 = 'hell o aAa bbbccc'
print(str4.endswith('c',10,12))

"""
isalpha() 如果字符串至少有一个字符，且所有字符都为字母，返回True
"""
str4 = 'hell1oaAabbbccc'
print(str4.isalpha())

"""
isdigit() 如果字符串只包含数字返回True
"""
str4 = '1234567'
print(str4.isdigit())

"""
isalnum() 所有的都为数字或字母返回True
"""
str4 = '123456a7'
print(str4.isalnum())

"""
如果字符只有空格，返回True
"""
str4 = ' '
print(str4.isspace())

"""
3.正方形,三角形,九九乘法表
4.三角形的不同样子（右对齐，等腰三角形）
"""
# 正方形
j = 1
while j <= 5:
    i = 1
    while i <= 5:
        print('*', end=' ')
        i +=1
    print()
    j +=1
# 三角形
j = 1
while j <= 5:
    i = 1
    while i <= j:
        print('*', end=' ')
        i +=1
    print()
    j +=1
# 九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i*j}', end='\t ')
        i +=1
    print()
    j +=1
# 右三角形
j = 1
while j <= 5:
    i = 5
    while i > j:
        print(' ',end=' ')
        i -= 1
    else:
        print("* "* j, end=' ')

    print()
    j +=1
# 右三角形
j = 1
while j <=5:
    i = 5
    while i > j:
        print(' ',end=' ')
        i -= 1
    l = 1
    while l <= j:
        print('*',end=' ')
        l += 1
    print()
    j +=1
# 等腰三角形

i = 1
while i<=5:
    j = 5
    while j>i:
        print(' ', end=' ')
        j -= 1
    else:
        print('* ' * (i*2-1),end=' ')

    print()
    i +=1



