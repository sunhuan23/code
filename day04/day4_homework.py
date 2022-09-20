# 1、打印小猫爱吃鱼，小猫要喝水
# 	定义猫类
class cat:
    def eat(self):
        print('小猫爱吃鱼')
    def drink(self):
        print('小猫要喝水')
tom = cat()
tom.eat()
tom.drink()
# 2、小明爱跑步，爱吃东西。
#     1）小明体重75.0公斤
#     2）每次跑步会减肥0.5公斤
#     3）每次吃东西体重会增加1公斤
#     4）小美的体重是45.0公斤
class per:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight +=1
    def __str__(self):
        return f'{self.name}的体重是{self.weight}'
xiaom = per('小明',75.1)
xiaom.run()
xiaom.eat()
print(xiaom)
# 3、摆放家具
#     需求：
#     1）.房子有户型，总面积和家具名称列表
#        新房子没有任何的家具
#     2）.家具有名字和占地面积，其中
#        床：占4平米
#        衣柜：占2平面
#        餐桌：占1.5平米
#     3）.将以上三件家具添加到房子中
#     4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
class furniture:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return f'{self.name}的面积是{self.area}'
class Hous:
    def __init__(self,mou,all_area):
        self.mou = mou
        self.all_area = all_area
        self.r_area = all_area
        self.f_list = []
    def add_f(self,f):
        if f.area > self.r_area:
            print('摆不下了')
        else:
            self.r_area -= f.area
            self.f_list.append(f.name)
    def __str__(self):
        return f'户型{self.mou}总面积{self.all_area}剩余面积{self.r_area}摆放了{self.f_list}'
zhuozi = furniture("桌子",10)
yizi = furniture("椅子",10)

h = Hous('三居室',120)
h.add_f(zhuozi)
h.add_f(yizi)
print(h)

# 4.士兵开枪
#     需求：
#     1）.士兵瑞恩有一把AK47
#     2）.士兵可以开火(士兵开火扣动的是扳机)
#     3）.枪 能够 发射子弹(把子弹发射出去)
#     4）.枪 能够 装填子弹 --增加子弹的数量
class gun:
    def __init__(self,name):
        self.name = name
        self.count = 0
    def send_bullet(self):
        if self.count <1:
            print('子弹不足')
        else:
            print('biu~')
            self.count-=1
    def add_bullet(self):
        self.count += 10
class per:
    def __init__(self,name,gun):
        self.name= name
        self.gun = gun
    def s_bul(self):
        self.gun.send_bullet()
    def add_bul(self):
        self.gun.add_bullet()
    def __str__(self):
        return f'{self.name}有一把{self.gun.name},还有{self.gun.count}发子弹'
g = gun('AK47')
ruien = per('瑞恩',g)
ruien.s_bul()
ruien.s_bul()
ruien.add_bul()
ruien.add_bul()
ruien.s_bul()

print(ruien)

