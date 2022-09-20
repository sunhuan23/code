"""
字典
"""
"""
查找
"""
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])
# 如果没有就返回19
print(dict1.get('a',19))

print(dict1.keys())
print(dict1.values())
print(dict1.items())
"""
增加，不存在就添加，存在就修改
"""
dict1['country'] = '中国'
print(dict1)
dict1['country'] = '国'
print(dict1)

"""
遍历
"""
dict2 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 打印key
for i in dict2:
    print(i)
# value
for i in dict2.values():
    print(i)
# k，v
for i in dict2.items():
    print(i)
for k,v in dict2.items():
    print(f'{k}={v}')

list1 = ['name', 'age','gender']
list2 = ['tom', 19, '男']
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)
dict2 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict2)

