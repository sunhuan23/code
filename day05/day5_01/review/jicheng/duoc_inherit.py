"""
多层继承
"""


class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
        self.name = 'xiao'
    def make_cake(self):
        print(f'运用{self.gongfu}制作出了煎饼')

class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'
        self.name = '11'
    def make_cake(self):
        print(f'运用{self.gongfu}制作出了煎饼')

class Prentice(Master,School):

    def __init__(self):
        self.gongfu = '[自制配方]'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.gongfu}制作出了煎饼')
    def master_make_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def school_make_cake(self):
        School.__init__(self)
        School.make_cake(self)
class A(Prentice):
    pass

if __name__ == '__main__':
    xiaom = A()
    xiaom.school_make_cake()