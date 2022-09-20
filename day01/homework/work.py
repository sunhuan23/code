# 2.完成教程中未实现的作业:石头剪刀布
"""
1、(1--石头，2--箭头，3--布,4,退出)
2、用户和电脑比
结果：玩家赢，电脑赢，平局
"""
# import random
# def guess():
#     while True:
#         num = int(input('请输入您的出拳(1--石头，2--箭头，3--布,4,退出)：'))
#         computer = random.randint(1,3)
#         print(f'电脑出{computer}')
#         if (num == 1 and computer == 2) or (num == 2 and computer == 3) or (num == 3 and computer == 1):
#             print('玩家赢')
#         elif (num == 1 and computer == 3) or (num == 2 and computer == 1) or (num == 3 and computer == 2):
#             print('电脑赢')
#         elif num == computer:
#             print('平局')
#         elif num == 4:
#             break
#         else:
#             print('请输入合法')
# guess()

# 3.正方形,三角形,九九乘法表

# 正方形
i = 0
while i < 5:
    j = 0
    while j < 5:
        print('*',end=' ')
        j += 1
    print()
    i += 1
# 三角形
i = 0
while i < 5:
    j = 0
    while j <= i:
        print('*',end=' ')
        j += 1
    print()
    i += 1
# 右三角形
i = 1
while i <= 5:
    j = 5
    while j >i:
        print('#',end=' ')
        j -=1
    else:
        print('* '*i,end='')

    print()
    i += 1

# 等腰三角形
i = 1
while i <= 5:
    j = 5
    while j > i:
        print('#',end=' ')
        j -= 1
    else:
        print('* '* (i*2-1) , end=' ')
    print()
    i += 1
# 九九乘法口诀
i = 1
while i <=9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {j*i}',end='\t')
        j += 1
    print()
    i += 1

# 4.三角形的不同样子（右对齐，等腰三角形）