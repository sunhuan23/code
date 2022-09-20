# 三角形
"""
*
* *
* * *
* * * *
* * * * *
"""
row = 1
while row <= 5:
    line = 0
    while line < row:
        print("*",end=" ")
        line += 1
    print()
    row += 1
print("=============")
# 右三角形
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
# 行列都为5
row1 = 1  # row1控制行数
while row1 <= 5:
    # 第一个内循环控制空格的打印，空格的数量=5-row1
    line1 = 5
    while line1 > row1:
        print(" ",end=" ")
        line1 -= 1
    # 第二个内循环控制*号的打印，*的个数=row1当前行数
    long = 1
    while long <= row1:
        print("*", end= " ")
        long +=1
    print()
    row1 += 1

print("=============")

# 等腰三角形
"""
        *
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
# 行数5
row2 = 1 # row2控制行数及列数
while row2 <= 5:
    # 第一个内循环控制使用空格补齐的数量，5-row2
    line2 = 5
    while line2 > row2:
        print(" ", end=" ")
        line2 -= 1
    # 第二个内循环控制*号的数量,*号=row*2-1
    long2 = 1
    while long2 < row2 * 2:
        print("*", end=" ")
        long2 += 1
    print()
    row2 += 1



