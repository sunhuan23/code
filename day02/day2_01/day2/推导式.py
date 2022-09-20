list1 = [i for i in range(10)]
print(list1)

list1 =  [i for i in range(10) if i % 2 == 0]
print(list1)

list1 = [(i,j) for i in range(1,3) for j  in range(0,3)]
print(list1)

# 创建一个字典:字典key是1-5数字, value是这个数字的2次方。
dict1 = {}

for i in range(1,6):
    dict1[i] = i**2
print(dict1)

# 推导式
dict2 = {i : i **2 for i in range(1,6)}
print(dict2)
# 将两个列表合成一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] =list2[i]
print(dict1)
# 推导式
dict3 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict3)

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求:提取上述电脑数量大于等于200的字典数据
for k,v in counts.items():
    if v >= 200:
        print({k:v})
dict4 = {k:v for k,v in counts.items() if v>=200}
print(dict4)

# 集合推导式
list1=[1,1,2]
# 需求:创建一个集合,数据为下方列表的2次方。
s1 = set()
for i in list1:
    s1.add(i **2)
print(s1)

# 推导式
s1 = {i ** 2 for i in list1}
print(s1)
