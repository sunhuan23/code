#
# 3.正方形,三角形,九九乘法表

"""
正方形
"""
j = 0
while j < 5:
    i = 0
    while i < 5 :
        print('*',end=' ')
        i += 1
    print()
    j += 1

"""
三角形
"""
j = 0
while j < 5:
    i = 0
    while i <= j :
        print('*',end=' ')
        i += 1
    print()
    j += 1

"""
右三角形
"""
j = 1
while j <= 5:
    i = 5
    while i >j:
        print(" ",end=" ")
        i -= 1
    else:
        print("* " *j)
    j += 1

"""
等腰三角形
"""
j = 1
while j <= 5:
    i = 5
    while i > j:
        print("#",end=' ')
        i -= 1
    else:
        print("* "* (j*2-1))
    j += 1

"""
九九乘法表
"""
j = 1
while j <=9:
    i = 1
    while i <=j:
        print(f"{i} * {j} = {i * j}", end="\t")
        i += 1
    print()
    j+= 1
# 4.三角形的不同样子（右对齐，等腰三角形）
#


