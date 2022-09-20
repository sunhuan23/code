"""
1、集合
2、可变数据类型
3、无序的
4、不可重复的
"""
s1 = {1,4,5,2,3,5,2,4,5}
print(s1)

# s1 = {} # 字典
s2 = set("djeijeif")
print(s2)

"""
增加
"""
s1.add(10)
print(s1)
s1.update([100,200])
print(s1)
"""
删除
"""
s1.remove(100)  #不存在会报错
print(s1)

s1.discard(300) #不存在不会报错
print(s1)

a = s1.pop() # 随机删
print(a)
print(s1)

print(200 in s1)