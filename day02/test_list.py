"""
1、列表支持增删改查

"""
# name_list = ['tom', 'lily', 'rose', 'tom']
# # 根据下标查找
# print(name_list[0])
# print(name_list[1])
#
# # index返回数据的下标
# print(name_list.index('lily'))
#
# # count 返回数据在序列中的个数
# print(name_list.count('tom'))
#
# # 返回列表的长度
# print(len(name_list))
#
# # 数据是否在列表中，返回true或false
# print('tom' in name_list)
# print('tom' not in name_list)
# """
# 添加
# """
# # append，在列表后追加数据
# name_list.append('小明')
# print(name_list)
# new_name = ['小红', "小强"]
# name_list.append(new_name)
# print(name_list)
#
# # extend，追加序列，只支持容器
# name_list.extend(new_name)
# print(name_list)
#
# # 列表拼接
# name_list = name_list + new_name
# print(name_list)
#
# # 指定位置增加元素
# name_list.insert(0,'hhh')
# print(name_list)
"""

列表删除
"""
# name_list = ['tom', 'lily', 'rose', 'tom','小民']
# # del 删除指定下标的数据
# del name_list[2]
# print(name_list)
# # del name_list # 删除整个列表
#
# # pop 返回删除的数据，不输入下标删除最后一个数据
# res = name_list.pop()
# print(res)
# print(name_list)
#
# # remove 输入要删除的数据，不存在会报错，多个相同数据删除第一个
# name_list.remove('tom')
# print(name_list)
#
# # clear 清空列表中的数据，列表还存在，空列表
# name_list.clear()
# print(name_list)

"""
修改
"""
# name_list = ['tom', 'lily', 'rose', 'tom','小民']
#
# # 根据下标修改元素
# name_list[0] = '小明'
# print(name_list)
#
# num_list = [1, 2, 3,7, 4, 5]

# reverse列表逆转,会改变原始数据
# num_list.reverse()
# print(num_list)

# reversed：列表逆转，不会改变原始数据，返回一个对象，想要输出需要类型转换
# new_list = reversed(num_list)
# print(new_list)
# print(list(new_list))

# 排序：sort，会改变原始数据,默认升序
# num_list.sort()
# print(num_list)
#
# # 想要降叙排序
# num_list.sort(reverse=True)
# print(num_list)
#
# # sorted：不会改变原始数据，默认升序
# new_list = sorted(num_list)
# print(new_list)
#
# # 降叙
# new_list = sorted(num_list, reverse=True)
# print(new_list)

# num_list = [1,2,3]
# # 复制
# new_list = num_list.copy()
# print(new_list)

name_list = ['tom', 'lily', 'rose', 'tom','小民']

# while循环

# n = 0
#
# while n < len(name_list):
#     print(name_list[n])
#     n += 1

# for循环
# for i in name_list:
#     print(i)

# for循环遇到数据被删除，可能会丢失数据
for i in name_list:
    if i == 'lily':
        name_list.remove(i)
        continue
    print(i)   # tom,tom,小民


# 列表嵌套
name_list = [['tom', 'lily'], ['rose', 'tom'],['小民']]

# 取rose
print(name_list[1][0])
