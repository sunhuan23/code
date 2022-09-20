# 4.士兵开枪
#     需求：
#     1）.士兵瑞恩有一把AK47
#     2）.士兵可以开火(士兵开火扣动的是扳机)
#     3）.枪 能够 发射子弹(把子弹发射出去)
#     4）.枪 能够 装填子弹 --增加子弹的数量

"""
定义一个枪类
    定义一个初始化方法
        属性：
        名称
        子弹数量
    定义一个开枪方法
        判断子弹大于0
            子弹减1

    定义一个装子弹的方法
        加10个子弹
定义一个人类
    定义一个初始化方法
        属性：
        名字
    定义一个开枪的方法
    定义一个装子弹的方法
    定义一个魔法方法
"""
class Gun:
    def __init__(self,name):
        self.name = name
        self.count = 0
    def open_fire(self):
        if self.count>0:
            print('biu～')
            self.count -= 1
        else:
            print('子弹不足')
    def add_bullet(self):
        self.count +=10

class Person:
    def __init__(self,name,gun):
        self.name = name
        self.gun = gun
    def open_fire(self):
        self.gun.open_fire()
    def add_bullet(self):
        self.gun.add_bullet()
    def __str__(self):
        return f'{self.name}有有一把{self.gun.name},还有{self.gun.count}发子弹'
if __name__ == '__main__':
    akm =  Gun('AK47')
    ruien = Person('瑞恩',akm)
    ruien.open_fire()
    ruien.add_bullet()
    ruien.open_fire()
    ruien.open_fire()
    ruien.open_fire()

    print(ruien)