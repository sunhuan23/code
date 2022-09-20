""""""
"""
类外部添加对象属性
"""
# class Washer:
#     def wash(self):
#         print('我会洗衣服')
#     def __str__(self):
#         return f'我的身高是{haier1.height}'
#
# haier1 = Washer()
# haier1.wash()
# haier1.height = 10
# print(haier1)

"""
类里获取对象属性
使用魔法方法 __init__
"""
# class Washer:
#     def __init__(self):
#         self.height = 100
#         self.weight = 90
#     def wash(self):
#         print(f'高度是{self.height},重量{self.weight}')
# haier = Washer()
# haier.wash()

"""
有参数的__init__
"""
# class Washer:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#     def wash(self):
#         print(f'高度是{self.height},重量{self.weight}')
# haier = Washer(100,10)
# haier.wash()

"""
__del__,当删除对象时，python解释器也会默认调⽤ __del__() ⽅法
"""
# class Washer:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#     def wash(self):
#         print(f'高度是{self.height},重量{self.weight}')
#     def __del__(self):
#         print(f'{self}对象已被删除')
# haier = Washer(100,10)
# del haier

"""
需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了

2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料

需要定义的类：地瓜类
地瓜类的属性有：
        时间  int 默认值0
        状态  str 默认值生的
        调料  列表  
    地方类的方法：
    烤地瓜
    添加调料

"""
class tudou:
    def __init__(self):
        self.time = 0
        self.status = '生的'
        self.tiaoliao = []
    def kaodigua(self,time):
        self.time += time
        if 0<self.time<=3:
            self.status = '生的'
        elif 3<self.time<=5:
            self.status = '半生不熟'
        elif 5<self.time<=8:
            self.status = '熟了'
        else:
            self.status = '糊了'
    def jiatiaoliao(self,*args):
        self.tiaoliao.extend(args)
    def __str__(self):
        return f'土豆烤了{self.time}分钟，{self.status},加了{self.tiaoliao}'
if __name__ == '__main__':
    tudou1 = tudou()
    tudou1.kaodigua(2)
    tudou1.kaodigua(10)
    tudou1.jiatiaoliao('盐','芥末')
    print(tudou1)
