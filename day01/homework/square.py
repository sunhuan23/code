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

import random

l =[1,2,3,4,5,6,7,8]
l1 = [[],[],[]]
for i in range(len(l)):
    t = random.randint(0,2)
    l1[t].append(i)
print(l1)