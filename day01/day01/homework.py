
# 2.完成教程中未实现的作业:石头剪刀布
"""
用户和电脑比
石头-1 剪刀-2 布-3
需要定义的类：人类，电脑类

人类的属性：出拳数
人类的方法：出拳
"""
# import random
# class caiquan:
#     def __init__(self):
#         self.people_chuquan = int(input("请输入你要出拳的数字，石头-1 剪刀-2 布-3:"))
#         self.computer_chuquan = random.randint(1, 3)
#
#     def compare(self):
#
#         if (self.people_chuquan == 1 and self.computer_chuquan == 2) or (self.people_chuquan == 2 and self.computer_chuquan == 3) or (self.people_chuquan == 3 and self.computer_chuquan == 1):
#             print(f'玩家出拳：{self.people_chuquan},电脑出拳{self.computer_chuquan},玩家胜出')
#         elif (self.people_chuquan == 1 and self.computer_chuquan == 3) or (self.people_chuquan == 2 and self.computer_chuquan == 1) or (self.people_chuquan == 3 and self.computer_chuquan == 2):
#             print(f'玩家出拳：{self.people_chuquan},电脑出拳{self.computer_chuquan},电脑胜出')
#         elif self.computer_chuquan == self.people_chuquan:
#             print(f"玩家出拳：{self.people_chuquan},电脑出拳{self.computer_chuquan},平局")
#
#         else:
#             print('输入不合法，请输入石头-1 剪刀-2 布-3：')
# if __name__ == '__main__':
#     xiaom = caiquan()
#     xiaom.compare()
# 3.正方形,三角形,九九乘法表
"""
正方形
"""
# j = 1
# while j <=5:
#     i = 1
#     while i <=5:
#         print('*',end=' ')
#         i += 1
#     print()
#     j += 1

"""
三角形
"""
# j = 1
# while j <= 5:
#     i = 1
#     while i<=j:
#         print('*', end=' ')
#         i += 1
#     print()
#     j += 1
"""
右三角形
"""
# j = 1
# while j <= 5:
#     i = 5
#     while i > j :
#         print('#',end=' ')
#         i -= 1
#     l = 1
#     while l <= j:
#         print('*',end=' ')
#         l += 1
#     print()
#     j += 1

"""
等腰三角形
"""
# j = 1
# while j <= 5:
#     i = 5
#     while i > j:
#         print('#',end=' ')
#         i -= 1
#     l = 1
#     while l < j * 2:
#         print('*' ,end=' ')
#         l += 1
#     print()
#     j+=1

"""
九九乘法表
"""
j = 1
while j <= 9:
    i = 1
    while i<=j:
        print(f"{i} * {j} = {i * j}",end='\t')
        i += 1
    print()
    j += 1


# 4.三角形的不同样子（右对齐，等腰三角形）





















