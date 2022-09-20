# 前提：课上的所有内容复习一遍，检查哪些地方还未理解

# Python练习题：
# 提示：先去分析要定义的类，属性，方法，对象作为一个参数来传递，一定要先写逻辑分析，再写代码。
"""
1、打印小猫爱吃鱼，小猫要喝水
    定义猫类

"""
# class Cat:
#     def eat(self,food='鱼'):
#         print(f'小猫爱吃{food}')
#     def drink(self,yinliao = '水'):
#         print(f'小猫爱喝{yinliao}')
# tom = Cat()
# tom.eat('罐头')
# tom.drink('牛奶')


"""
2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤
需要定义的类：人类
人类的属性：
        名字  外界给
        体重  外界给
人类的方法：
        跑步
        吃东西    

"""

#
# class people:
#     def __init__(self,name,height):
#         self.name = name
#         self.weight = height
#     def run(self):
#         self.weight -= 0.5
#     def eat(self):
#         self.weight += 1
#     def __str__(self):
#         return f'{self.name}的体重是{self.weight}'
# xiaoming = people('小明',77.1)
# xiaoming.eat()
# print(xiaoming)
# xiaoming.run()
# print(xiaoming)

"""
3、摆放家具
    需求：
    1）.房子有户型，总面积和家具名称列表
       新房子没有任何的家具
    2）.家具有名字和占地面积，其中
       床：占4平米
       衣柜：占2平面
       餐桌：占1.5平米
    3）.将以上三件家具添加到房子中
    4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
    
需要定义的类：家具类
            房子类
家具类的属性：
        家具名称 外界给
        面积   外界给
           
家具类的方法：
         str
房子类的属性：
        户型     外界给
        总面积   外界给
        剩余面积  总面积
        家具列表  默认为空
房子类的方法：
        摆放家具
        str
"""
# class Jiaju:
#     # 家具类的属性：
#     def __init__(self,name,area):
#         # 家具名称
#         self.name = name
#         # 家具面积
#         self.area = area
#     def __str__(self):
#         return f'{self.name}的面积是{self.area}平'
#
# class Hous:
#     def __init__(self,model,all_area):
#         # 户型     外界给
#         self.model = model
#         # 总面积   外界给
#         self.all_area = all_area
#         # 剩余面积  总面积
#         self.f_area = all_area
#         # 家具列表  默认为空
#         self.j_list = []
#
#     #         摆放家具
#     def put_j(self,jiaju):
#         if jiaju.area < self.f_area:
#             self.f_area -= jiaju.area
#             self.j_list.append(jiaju.name)
#         else:
#             print('摆不下了')
#
#     #         str
#     def __str__(self):
#         return f'房子户型是{self.model}，总面积是{self.all_area},剩余面积是{self.f_area},摆放了{self.j_list}'
#
#
# if __name__ == '__main__':
#     chuang = Jiaju('床',2)
#     zhuoz = Jiaju('桌子',1114)
#     print(chuang)
#     home = Hous('三居',150)
#     home.put_j(zhuoz)
#     home.put_j(chuang)
#     print(home)


"""
4.士兵开枪
    需求：
    1）.士兵瑞恩有一把AK47
    2）.士兵可以开火(士兵开火扣动的是扳机)
    3）.枪 能够 发射子弹(把子弹发射出去)
    4）.枪 能够 装填子弹 --增加子弹的数量
需要定义的类：枪类
            士兵类
枪类的属性：
    name     外界给
    子弹数量  默认0
枪类的方法：
    发射子弹
    装子弹
士兵类的属性:
    name  外界给
士兵类的方法：
    开火
    装子弹
"""
class Gun:
    def __init__(self,name):
        #     name
        self.name = name
        #     子弹数量
        self.count = 0
    # 枪类的方法：
    #     发射子弹
    def hair_bullet(self):
        if self.count >0:
            print('biu')
            self.count -= 1
        else:
            print('没有子弹了')

    #     装子弹
    def add_bullet(self):
        self.count += 10
    def __str__(self):
        return f"我有一把{self.name},还有{self.count}发子弹"
class shibing:
    def __init__(self,name,gun):
        self.name = name
        self.gun =  gun
    def h_bullet(self):
        self.gun.hair_bullet()
    def a_bullet(self):
        self.gun.add_bullet()
    def __str__(self):
        return f'{self.name}有一把{self.gun.name},还有{self.gun.count}子弹'

if __name__ == '__main__':
    ak = Gun('AK47')
    ruirn = shibing('瑞恩',ak)
    ruirn.a_bullet()
    ruirn.h_bullet()

    print(ruirn)
