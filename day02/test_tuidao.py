# 创建0-10的列表

# while
# list1 = []
# i = 0
# while i <= 10:
#     list1.append(i)
#     i += 1
# print(list1)
#
# # for循环
# list2 = []
# for i in range(0,11):
#     list2.append(i)
# print(list2)
#
# # 推导样式,类似三目运算，for左边是结果
# list3 = [i for i in range(11)]
# print(list3)
#
# # 取偶数
# list3 = [i for i in range(11) if i % 2 == 0]
# print(list3)
#
# # [1,]
# list4 = []
# for i in range(1,3):
#     for j in range(3):
#         list4.append((i,j))
# print(list4)
#
# list5 = [(i,j) for i in range(1,3) for j in range(3)]
# print(list5)

# 字典推导式
# list1 = ["name", 'age', 'gender']
# list2 = ["小明", '10',"男"]
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)
# list3 = []
# for k in dict1.items():
#     print((k))
#     list3.append(k)
# print(list3)
# print(dict1['name'])

counts = {"A":1,"B":2,"C":200}
res1 = {}
for k,v in counts.items():
    if v > 100:
        res1[k] = v
print(res1)

res2 = {k : v for k,v in counts.items() if v > 100}
print(res2)

# 集合的推导
list1 = [1, 1, 2]
s1 = {i **2 for i in list1}
print(s1)