# 无参数
fn1 = lambda : 100
print(fn1())

# 两个参数
fn1 = lambda a,b : a + b
print(fn1(1,3))

# 默认参数
fn1 = lambda a,b =10:a + b
print(fn1(1))

# 可变参数（位置传递）
fn1 = lambda *args : args
print(fn1(1,2))
list1 = [1,2,3]
print(fn1(*list1))

# 可变参数（关键字传递）
fn1 = lambda **kwargs : kwargs
print(fn1(name='tom',age = 19))
dict1 = {'name': 'tom', 'age': 19}
print(fn1(**dict1))

# 带判断的匿名函数
fn1 = lambda a,b :a if a > b else b
print(fn1(100, 200))

student = [
    {'name':'tom',"age":18},
    {"name":"gom",'age':10},
    {'name':'aom','age':10}
]
student.sort(key=lambda x : x['age'] )
print(student)
