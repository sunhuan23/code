# 创建一个0-10的列表。

list1 = [i for i in range(11)]
print(list1)

#  创建0-10的偶数列表
list1 = [i for i in range(11) if i %2 == 0]
print(list1)

# 多个for循环实现列表推导式
list1 = [(i,j) for i in range(1,3) for j in range(3)]
print(list1)

# 字典推导式
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict1)

# 创建一个字典:字典key是1-5数字, value是这个数字的2次方。
dict1 = {i :i**2 for i in range(1,6)}
print(dict1)

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求：提取上述电脑数量大于等于200的字典数据
dict1 = {k:v for k,v in counts.items() if v >=200}
print(dict1)
