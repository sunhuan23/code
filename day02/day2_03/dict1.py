dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
"""
增加
存在修改，不存在添加
"""
dict1['country']="北京"
print(dict1)

"""
删除
"""
del dict1['name']
print(dict1)

"""
清空字典
"""
# dict1.clear()
# print(dict1)

"""
根据key查找
"""
print(dict1.get('name','小明'))

print(list(dict1.keys()))
print(list(dict1.values()))
print(list(dict1.items()))

"""
遍历字典的key
"""
for i in dict1.keys():
    print(i)
"""
遍历字典的value
"""
for i in dict1.values():
    print(i)
"""
遍历字典
"""
for k,v in dict1.items():
    print(f'{k}:{v}')
