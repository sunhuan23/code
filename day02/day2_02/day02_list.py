import copy
"""
列表
"""
"""
查找
"""
list1 = ['小明','小黑','小红','小明']
print(list1[0])
print(list1.count('小明'))
print(list1.index('小黑'))
print(len(list1))

"""
判断是否存在
"""
print('小黑' in list1)
print('小刚' not in list1)

"""
增加
"""
list1.append('小刚')
print(list1)
list1.extend(('1','哈哈','这个'))
list1.insert(1,'zz')
print(list1)

"""
删除
"""
# del list1
# print(list1)
del list1[0]
print(list1)
a = list1.pop(0)
print(list1,a)
list1.remove('小红')
print(list1)
# list1.clear()
# print(list1)

"""
修改
"""
list1[0] = '珍珠'
print(list1)

"""
逆置
"""
list1.reverse()
print(list1)

res = reversed(list1)
print(list(res))

"""
排序
"""
# list1.sort()
print(list1)

res = sorted(list1,reverse=True)
print(res)

"""
复制
"""
a = list1.copy()
print(a)

# 深拷贝
b = copy.deepcopy(list1)
print(b)

