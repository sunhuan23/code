"""
需求: 创建一个0-10的列表
"""
list1 = [ i for i in range(11)]
print(list1)

"""
需求: 创建0-10的偶数列表
"""
list1 = [ i for i in range(11) if i % 2==0]
print(list1)

"""
[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
"""
list1 = [(i,j) for i in range(1,3) for j in range(0,3) ]
print(list1)

"""
创建一个字典:字典key是1-5数字, value是这个数字的2次方。
"""
dict1 = {i:i**2 for i in range(1,6)}
dict2 ={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(dict2[2])
print(dict1)

"""
# 需求：提取上述电脑数量大于等于200的字典数据
"""
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
dict1 = { k:v for k,v in counts.items() if v >=200 }
print(dict1)

"""
需求:创建一个集合,数据为下方列表的2次方。
"""
list1 = [1, 1, 2]
s1 ={i ** 2 for i in list1 }
print(s1)