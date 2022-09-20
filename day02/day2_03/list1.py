"""
查找
"""
"""
下标查找
"""
name_list = ['Tom','Lily','Rose','Tom']
print(name_list[0])

"""
index,找不到报错
"""
print(name_list.index("Tom"))

"""
count
"""
print(name_list.count('Tom'))

"""
len
"""
print(len(name_list))

"""
判断是否存在
"""
print('tom' in name_list)
print('tom' not in name_list)

"""
需求: 查找用户输入的名字是否已经存在
"""
# name = input('输入名字：')
# if name in name_list:
#     print('存在')
# else:
#     print("不存在")

"""
列表增加元素
"""
name_list = ['Tom','Lily','Rose','Tom']
name_list.append('小明')
print(name_list)

list1 = ["小刚","小黑"]
name_list.append(list1) # 将列表添加到name——list
print(name_list)

"""
将序列中的每个元素添加至列表中
"""
name_list = ['Tom','Lily','Rose','Tom']
list1 = ["小刚","小黑"]
name_list.extend(list1)
print(name_list)
name_list.extend(("小明","小刚"))
print(name_list)

"""
指定位置增加数据，insert
"""
name_list = ['Tom','Lily','Rose','Tom']
name_list.insert(0,'小明')
print(name_list)

"""
删除
"""
# name_list = ['Tom','Lily','Rose','Tom']
# del name_list[0]
# print(name_list)
# del name_list
# print(name_list)

"""
删除指定下标的数据(默认为最后一个),并返回该数据
"""
name_list = ['Tom','Lily','Rose','Tom']
name = name_list.pop(0)
print(name_list)
print(name)

"""
remove
"""
name_list = ['Tom','Lily','Rose','Tom']
name_list.remove('Lily')
print(name_list)

"""
clear 清空列表
"""
name_list.clear()
print(name_list)

"""
修改
"""
name_list = ['Tom','Lily','Rose','Tom']
name_list[0] = 'aa'
print(name_list)

"""
逆置
"""
name_list = [1,2,8,7,3,4,5,6,7]
name_list.reverse()
print(name_list)

"""
排序
"""
name_list = [1,2,8,7,3,4,5,6,7]
name_list.sort()
name_list.sort(reverse=True) #排序
print(name_list)

"""
逆置不改变原数据
"""
name_list = [1,2,8,7,3,4,5,6,7]
list1=reversed(name_list)
print(list(list1))

"""
不改变原数据的排序
"""
name_list1 = [1,2,8,7,3,4,5,6,7]
a = sorted(name_list1)
print(a)

"""
复制
"""
import copy
name_list1 = [1,2,8,7,3,4,5,6,7]
list1 = name_list.copy()
list2 = copy.deepcopy(list1)
print(list1)
print(list2)
"""
列表的循环
"""
name_list = ['Tom', 'Lily', 'Rose']

i = 0
while i <len(name_list):
    print(name_list[i])
    i += 1

for i in name_list:
    print(i)

"""
列表嵌套
"""
name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
print(name_list[0][1])

"""
赋值不改变内容地址
"""
list1 = [1,2,3]
list2 = list1
list1.append(4)
print(list1)
print(list2)
print(id(list1))
print(id(list2))

print('========')
"""
复制的改变内容地址
"""
list1 = [1,2,3]
list2 = list1.copy()
list1.append(4)
print(list1)
print(list2)
print(id(list1))
print(id(list2))