import copy

a = [1, 2, 3, [2, 3, 4]]
# 浅拷贝
b = a.copy()
c = copy.deepcopy(a)

print(a)
print(b)
# 两个列表的id是不同的
print(id(a))
print(id(b))
# 数字是不可变数字类型
print(id(a[0]))
print(id(b[0]))
a[0]=5
print(a)
print(b)
print(id(a))
print(id(b))
print(id(a[-1]))
print(id(b[-1]))
a[-1][0] = 5
print(a)
print(b)

print(c)
print(id(c))
print(id(c[-1]))