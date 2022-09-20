"""
一般将input接收的数据存储到变量
input接收的任何数据默认都是字符串数据类型
input会停下来等待和用户做交互,之后再执行下面的代码

语法：
    input("提示信息")
"""

password = input("请输入密码：")
print(password)
print(type(password))  # --->str

# 输入转为int类型
password = int(input("请输入密码："))
print(password)
print(type(password))  # --->int
