def fun(num):
    return 100
l = lambda a,b :a+b
print(l(100,200))

# 无参表达式
func = lambda :100
print(func())

# 一个参数
func1 = lambda a : a
print(func1(10))

# 多个参数
func2 = lambda a,b:a+b
print(func2(10,2))

# 默认参数
func3 = lambda a, b, c = 100:a+b+c
print(func3(1,3))

# 可变参数*args
func4 = lambda *args : args
list1 = [1,3,5,7,8]
print(func4(1,2,3))
print(func4(*list1))

# 可变参数: **kwargs
func5 = lambda **kwargs:kwargs
print(func5(name = 'xiaom'))

# 带判断的lambda
func6 = lambda a, b:a if a>b else b
print(func6(2,4))

students = [ {'name': 'TOM', 'age': 20}, {'name': 'ROSE', 'age': 19}, {'name': 'Jack', 'age': 22}]
# 按字典key进行排序
students.sort(key=lambda key : key['name'])
print(students)

