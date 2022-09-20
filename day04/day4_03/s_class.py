class Washer:
    """
    __init__() ⽅法的作⽤：初始化对象。
    """
    def __init__(self):
        self.height = 50
        self.width = 100
    # def wash(self):
    #     print('我会洗衣服')
    #     print(f'haier的身高是{self.height}')
    # def __str__(self):
    #     return f'haier的身高是{self.width}'
    def __del__(self):
        print(f'{self}对象已被删除')
# haier = Washer()
# haier.height = 100
# haier.width = 200
# haier.wash()
hai1 = Washer()
del hai1
"""
5.1.1 需求
需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料
"""
"""
定义一个地瓜类
    定义一个初始化方法
        属性：
        被烤时间
        状态
        调料列表
    定义一个烤地瓜的方法
        0-3分钟：⽣的
        3-5分钟：半⽣不熟
        5-8分钟：熟的
        超过8分钟：烤糊了
    定义一个添加佐料的方法
        加入列表
    定义一个__str__方法
"""
# 定义一个地瓜类
class DiGua:
#     定义一个初始化方法
    def __init__(self):
#         属性：
#         被烤时间
        self.time = 0
#         状态
        self.status = '生的'
#         调料列表
        self.tiaoliao = []
#     定义一个烤地瓜的方法
    def make_digua(self,t):
        self.time += t
#         0-3分钟：⽣的
        if 0<self.time <=3:
            self.status = '生的'
#         3-5分钟：半⽣不熟
        elif 3<self.time <=5:
            self.status = '半生不熟'
#         5-8分钟：熟的
        elif 5 < self.time <= 8:
            self.status = '熟的'
#         超过8分钟：烤糊了
        elif self.time> 8:
            self.status = '烤糊了'
#     定义一个添加佐料的方法
    def add_tiaoliao(self,t):
        self.tiaoliao.extend(t)
#         加入列表
#     定义一个__str__方法
    def __str__(self):
        return f'地瓜烤了{self.time},{self.status},加了{self.tiaoliao}'

if __name__ == '__main__':
    tudou = DiGua()
    tudou.make_digua(2)
    tudou.make_digua(2)
    tudou.make_digua(2)
    tudou.make_digua(2)
    tudou.make_digua(2)
    tudou.add_tiaoliao(['盐','辣椒'])
    tudou.add_tiaoliao(['芥末','胡椒'])

    print(tudou)

