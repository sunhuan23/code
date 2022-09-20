"""
需求主线：
1. 被烤的时间和对应的地⽠状态：
0-3分钟：⽣的
3-5分钟：半⽣不熟
5-8分钟：熟的
超过8分钟：烤糊了
2. 添加的调料：
⽤户可以按⾃⼰的意愿添加调料
"""

# class Digua:
#     def __init__(self,t=0,s='生的',l= []):
#         self.time = t
#         self.status = s
#         self.tiao = l
#
#     def kao(self):
#         self.time += self.time
#         if self.time >=0 and self.time<3:
#             return self.status
#         elif self.time>=3 and self.time<5:
#             self.status = '半生不熟'
#             return self.status
#         elif self.time>=5 and self.time<8:
#             self.status = '熟了'
#             return self.status
#         else:
#             self.status = '烤糊了'
#             return self.status
#
#     def tiaoliao(self):
#         self.tiao += self.tiao
#
#     def __str__(self):
#         return  f'加了{self.tiao}'
#
# # pep = Digua(2,l = ['yan','孜然'])
# # print(pep.kao())
# # print(pep.kao())
# pep1 = Digua(2,l = ['yan','孜然','香油'])
# print(pep1.kao())
# print(pep1.kao())
# pep1.tiaoliao()
# pep1.tiaoliao()
#
#
# # print(pep1.tiao)
# print(pep1)

class Sweet_P:
    def __init__(self):
        self.cooktime = 0
        self.status = '生的'
        self.seasoning = []
    def cook_time(self,t):
        self.cooktime += t
        if 0<=self.cooktime<=3:
            self.status = '生的'
        elif 3<self.cooktime<=5:
            self.status = '半生不熟'
        elif 5<self.cooktime<=8:
            self.status = '熟了'
        else:
            self.status = '糊了'
    def do_seasoning(self,*args):
        self.seasoning.extend(args)

    def __str__(self):
         return  f'烤了{self.cooktime}分钟，{self.status},加了{self.seasoning}'

if __name__ == '__main__':
    pep = Sweet_P()
    pep.cook_time(2)
    print(pep)
    pep.cook_time(2)
    print(pep)
    pep.do_seasoning('盐','芥末')
    pep.do_seasoning('油')
    print(pep)



