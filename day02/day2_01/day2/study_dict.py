dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 添加,不存在添加，存在则修改
dict1['country'] = '中国'
print(dict1)

dict1['age'] = 19
print(dict1)

# 删除

# del
del dict1['gender']
print(dict1)
# del dict1['1']
# del dict1
# print(dict1)

# clear
# dict1.clear()
# print(dict1)

# 查
# 根据key进行查找
print(dict1['name'])
# print(dict1['id'])

# get
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))

# keys
res = dict1.keys()
print(res)

# values
print(dict1.values())

# items
print(dict1.items())

# 循环遍历
for key in dict1.keys():
    print(key)

for key in dict1.keys():
    print(dict1[key])

for value in dict1.values():
    print(value)

for i in dict1.items():
    print(i)

for k,v in dict1.items():
    print(k,v)

