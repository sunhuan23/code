"""
公共操作
"""
"""
运算符
"""
"""
+ ：合并
支持字符串、列表、元组
"""
list1 = [1,2,4]
list2= [3,4,5]
list3 = list1 + list2
print(list3)

str1 = '123'
str2 = '456'
str3 = str1+str2
print(str3)

t1 = (1,2,4)
t2 =(4,5,6)
print(t1+t2)
"""
* : 复制
支持字符串、列表、元组
"""
list1 = [1,2,4]
list2= list1*4
print(list2)

str1 = '123'
print(str1*4)

t1 = (1,2,4)
print(t1*4)

"""
max（）
"""
list1 = [1,2,4]
print(max(list1))
print((min(list1)))

"""
enumerate()
"""
list1 = [1,2,4]
for i in enumerate(list1,start=1):
    print(i)
