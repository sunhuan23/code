n = (1,2,3)
m = (4,5,6)
# 拼接
res = m + n
print(res)
# 复制
res2 = n * 5
print(res2)
print(3 in n)

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 判断key是不是在字典中
print('Tom' in dict1.values())
# 个数
print(len(dict1))
n = {'b','a','c'}
print(f"最大值{max(n)}")
print(f"最小值{min(n)}")


# range：范围
for i in range(3,9,2):
    print(i)
res = tuple(range(10))
print(res)

# enumerate,返回下标和对应的元素
a = [1,2,2,4,5]
for i in enumerate(a):
    print(i)

for i in enumerate(a, start = 2):
    print(i)