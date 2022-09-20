"""
1、元祖不支持修改，只支持查找
2、元祖中有列表，支持修改列表中元素
"""
tup = (1,3,2,4,5,6,6)

print(tup[0])
print(tup.index(5))
print(tup.count(6))
print(len(tup))

tup1 = (1,3,2,4,5,6,['小明',8])
tup1[6][0] = '七'
print(tup1)