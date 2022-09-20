# 定义一个类名
class Washer:

    def wash(self):
        print('我会洗衣服')
        # print(self)
    def info_print(self):
        print(f'我的高度{self.height},')
        print(f'我的宽度{self.weight},')

# 实例化
haier1 = Washer()
# 调用
# print(haier1)
# 类外部定义属性
haier1.height = 100
haier1.weight = 80
print(f'-----{haier1.height}')
print(f'-----{haier1.weight}')
haier1.info_print()


#
haier2 = Washer()
haier2.wash()
haier2.height = 200
haier2.weight = 90
print(f'-----{haier2.height}')
print(f'-----{haier2.weight}')
haier2.info_print()
# print(haier2)
