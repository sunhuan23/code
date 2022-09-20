"""
1、集合是无序的
2、集合自动去重
3、创建集合可以用set（）或{},但是创建空集合需要是set（）
"""

# s1 = {1, 3, 4, 5,"a" ,"b", "c",1}
# print(s1)
# # add  添加,add里的元素当作一个元素
# s1.add(2)
# print(s1)
# s1.add((1,2,3))
# print(s1)
# # update，可以将一个序列分别增加
# s1.update((9,0,4))
# print(s1)

"""
删除
"""
s1 = {1, 3, 4, 5,"a" ,"b", "c",1}
# 删除指定数据，数据不存在报错
s1.remove(1)
print(s1)
# discard，删除指定数据，数据不存在也不报错,不做任何操作
s1.discard(7)
print(s1)
# pop,随机删除,返回删除的数据
res = s1.pop()
print(res)
# 判断元素是否在容器中
print(8 in s1)
print(8 not in s1)

