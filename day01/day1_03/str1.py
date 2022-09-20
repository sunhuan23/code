"""
字符串输出
"""
name = "小明"
print(f"我的名字叫{name}")
print("我的名字叫%s" %name)

"""
字符串输入
"""
# name = input("请输入：")
# print(name)

"""
根据下标取值
"""
name = "abcdefeeedddvvv"
print(name[0])
print(name[-1])
"""
切片
语法：序列[开始位置下标:结束位置下标:步长]
"""

print(name[-3:-1])
print(name[1:-1:2])
print(name[-1:1:-1])
"""
查找
"""
print(name.find('c'))  # 找不到返回-1
print(name.find('g'))
print(name.rfind('e')) # 和find一样只不过从右侧开始找

print(name.index('a')) # 找不到报错
print(name.rindex('f')) # 和index一样，只不过从右侧开始找

print(name.count("e")) #返回数量

"""
修改
replace
"""
mystr = "hello world and supertest and chenghao and Python"

print(mystr.replace("and", "haode", 10))

"""
分割
split,分割后返回一个列表
"""
mystr = "hello world and supertest and chenghao and Python"

list1 = mystr.split(" ",2)
print(list1)

"""
合并
join,字符或子串.join(多字符串组成的序列)
"""
list1 = ['chao', 'ge', 'test', 'promotion']
print(''.join(list1))


"""
将字符串第一个字母转为大写
"""
mystr = "hello world and supertest and chenghao and Python"
print(mystr.capitalize())

"""
将字符串每个单词首字母准换成大写
"""
mystr = "hello world and supertest and chenghao and Python"
print(mystr.title())

"""
将字符串中大写转小写
"""
mystr ='Hello World And Supertest And Chenghao And Python'
print(mystr.lower())

"""
将字符串中小写转大写。
"""
mystr = 'Hello World And Supertest And Chenghao And Python'
print(mystr.upper())

"""
删除字符串左侧空白字符
"""
mystr = '          Hello World And Supertest And Chenghao And Python'
print(mystr.lstrip())

"""
删除字符串右侧空白字符
"""
mystr = 'Hello World And Supertest And Chenghao And Python          '
print(mystr.rstrip())

"""
删除字符串两侧空白字符
"""
mystr = '         Hello World And Supertest And Chenghao And Python          '
print(mystr.strip())

"""
返回一个原字符串左对齐,并使用指定字符(默认空格)填充至对应长度的新字符串
字符串序列.ljust(长度,填充字符)
"""
mystr = 'Hello World And Supertest And Chenghao And Python'
print(mystr.ljust(60,'#'))

"""
返回一个原字符串左对齐,并使用指定字符(默认空格)填充至对应长度的新字符串
"""
mystr = 'Hello World And Supertest And Chenghao And Python'
print(mystr.rjust(60,"&"))

"""
返回一个原字符居中,并使用指定字符(默认空格)填充至对应长度的新字符串
"""
mystr = 'Hello World And Supertest And Chenghao And Python'
print(mystr.center(100,"*"))

"""
判断字符串是否以指定子串开头，
"""
mystr = 'Hello World And Supertest And Chenghao And Python'
print(mystr.startswith('Hello'))
print(mystr.startswith('lo',3,9))

"""
判断字符串是否以指定子串结尾，
"""
mystr = 'Hello World And Supertest And Chenghao And Python'
print(mystr.endswith('on'))
print(mystr.endswith('on',10,30))

"""
如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False
"""
mystr = 'HelloWorldAndSupertestAndChenghaoAndPython'
print(mystr.isalpha())

"""
:如果字符串只包含数字则返回True否则返回False
"""
mystr = '12344a'
print(mystr.isdigit())

"""
:如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False
"""
mystr =  ' 12344a'
print(mystr.isalnum())

"""
如果字符串中只包含空白,则返回True,否则返回False
"""
mystr = ' '
print(mystr.isspace())