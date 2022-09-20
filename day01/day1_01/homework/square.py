# 正方形
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# 一行输出5个星号,重复打印5行
row = 0
while row < 5:
    line = 0
    while line < 5:
        print("*",end=" ")
        line += 1
    print()

    row += 1