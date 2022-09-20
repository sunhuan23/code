# coding=utf-8
"""
变量：
    1、变量就是一个存储数据的时候当前数据所在的内存地址的名字而已
    2、命名规则：
        a、由字母、数字、下划线组成
        b、不能以数字开头
        c、不能使用内置关键字，例：class、False、True、None、、、、等
    3、命名习惯：
        a、见名知意
        b、大驼峰：MyName
        c、小驼峰：myName
        d、下划线：my_name
"""
# 变量使用
myName = 'Tom'
# 输出变量值
print(myName)
# 输出变量的内存地址
print(id(myName))
"""
    创建myName = 'Tom'时，相当于在内存地址中创建了一个对象'Tom'
    myName和itName 相当于引用Tom这个对象
    所以内存地址的输出时一样的
"""
itName = "Tom"
print(itName)
print(id(itName))
