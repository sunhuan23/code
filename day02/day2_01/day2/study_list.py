"""
查找
1、根据下标
2、函数index
3、函数count
4、函数len
5、in
6、notin
"""
# 根据下标查找
list1 = ['小明', '小红', '大壮','rose','小明']
# print(list1[1])

# 函数
# index，返回数据下标，找不到会报错
print(list1.index('小明',1,5))

# count，返回数据存在序列中的个数
print(list1.count('小明'))

# len,返回列表的长度
print(len(list1))

# in，判断数据是否在列表中
print('小明' in list1)

# not in,判断数据收否不存在列表中
print('小明' not in list1)
print('小强' not in list1)

"""
增加：
append
eextend
inser
"""
# append
list1.append(['hh','aa'])
# extend
list1.extend(['hell','world'])
print(list1)
# insert
list1.insert(11,'捷克')
print(list1)

"""
删除
del
pop
remove
clear
"""
# del
del list1[0]
print(list1)
# pop
list1.pop(0)
print(list1)
# remove
list1.remove('小明')
print(list1)
# clear
list1.clear()
print(list1)


"""
修改
1、reverse
1、reversed
3、sort
4、sorted
"""

list1 = [1, 4, 7, 5, 3,10]
# list1.reverse()
# print(list1)
# res = list(reversed(list1))
# print(res)

# sort
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

# sorted
# res = sorted(list1)
# print(res)
# print(sorted(list1,reverse=True))
#
# # copy
# lis = list1.copy()
# print(id(list1))
# print(id(lis))
# print(lis)

"""
列表的循环遍历
"""
list3 = [1, 4, 7, 5, 3,10]
# while
i = 0
while i < len(list3):
    print(list3[i])
    i += 1

for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])






