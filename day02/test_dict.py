"""
1、字典为键值对格式
2、key只能是不可变类型

"""
# dict1 = {"name": "小明", "age": 18, "gender": "男"}
# # 新增/修改
# # key不存在就新增，存在就修改
# dict1["country"] = "中国"
# print(dict)
# dict1['gender'] = '女'
# print(dict1)
#
#
# # 删除
# # 不存在报错
# del dict1["age"]
# print(dict1)
# # del dict1
# # print(dict1)
# dict1.clear()
# print(dict1)

dict1 = {"name": "小明", "age": 18, "gender": "男"}
# 查找，找不到会报错
print(dict1['name'])
# get，查找，找不到会返沪None
print(dict1.get('age'))
# keys，查看所有的key,可以转成list
print(dict1.keys())
# value，查看所有的value
print(dict1.values())
# items,查看所有的键值对
print(dict1.items())
# 循环遍历所有的key
for i in dict1:
    print(f"k是{i}")
# 或者
for i in dict1.keys():
    print(f"k是{i}")
# 循环所有的value
for i in dict1.values():
    print(f"v是{i}")
# 循环所有的键值
for i in dict1.items():
    print(f"键值是{i}")

