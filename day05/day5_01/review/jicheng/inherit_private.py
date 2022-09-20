"""
私有属性、方法
在属性、方法前加两个下划线__
私有属性不会被子类继承
"""


class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
        self.__name = 123
    def __make_cake(self):
        print(f'运用{self.gongfu}制作出了煎饼')
    def get_name(self):
        print(self.__name)
    def set_name(self):
        self.__name += 1
        print(self.__name)
    def get_make(self):
        self.__make_cake()



class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'
        self.name = '小猫'
    def make_cake(self):
        print(f'运用{self.gongfu}制作出了煎饼')
        print('123234')

class Prentice(Master,School):

    def __init__(self):
        super().__init__()
        self.gongfu = '[自制配方]'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.gongfu}制作出了煎饼')
    # def master_make_cake(self):
    #     Master.__init__(self)
    #     # Master.make_cake(self)
    #     Master.get_make(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)
    def super_make_cake(self):
        super().__init__()
        super().make_cake()
if __name__ == '__main__':
    xiaom = Prentice()
    # xiaom.master_make_cake()
    xiaom.super_make_cake()
    xiaom.get_name()
    xiaom.set_name()
