"""
for 临时变量 in 序列:
    重复执行的代码1
    重复执行的代码2

"""
str1 = "hello"
for i in str1:
    print(i)

# break
str1 = "hello"
for i in str1:
    if i == "l":
        print("遇到l不打印")
        break
    print(i)

# continue
str1 = "hello"
for i in str1:
    if i == "l":
        print("遇到l跳过")
        continue
    print(i)

