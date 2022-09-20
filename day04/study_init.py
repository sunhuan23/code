# class Washer():
#     # 初始化方法，实例化自动调用
#     def __init__(self):
#         print('start')
#         self.height = 100
#         self.weight = 200
#         print('end')
#     def wash(self):
#         print('会洗衣服')
#     def print_info(self):
#         print(f'高度{self.height}')
#         print(f'宽度{self.weight}')
# haier1 = Washer()
# print(f"高度{haier1.height}")
"""
带参数
"""

class Washer():
    # 初始化方法，实例化自动调用
    def __init__(self,h,w):
        print('start')
        self.height = h
        self.weight = w
        print('end')
    def wash(self):
        print('会洗衣服')
    def print_info(self):
        print(f'高度{self.height}')
        print(f'宽度{self.weight}')

    def __str__(self):
        return f"我的高度{self.height},我的宽度{self.weight}"

    def __del__(self):
        print('我被删除了')

haier1 = Washer(10,20)
print(haier1)

haier2= Washer(12,22)

del haier1
# print(f"我的高度{haier1.height}")
# print(f"我的宽度{haier1.weight}")
# haier1.print_info()
#
# haier2 = Washer(1,2)
# print(f"我的高度{haier2.height}")
# print(f"我的宽度{haier2.weight}")
# haier2.print_info()
