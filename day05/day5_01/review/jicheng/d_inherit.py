"""
徒弟继承师傅的所有技术
报班学习
"""
"""
多继承，优先找第一个父类，如果第一个父类没有，找第二个父类
"""
class Master:
    def __init__(self):
        self.gongfu  = '[五香配方]'
        self.name = 'xiaohong'
    def make_cake(self):
        print(f'运用{self.gongfu}制作了煎饼')
class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'
    def __make_cake(self):
        print(f'运用{self.gongfu}制作了煎饼')

class Prentice(School,Master):
    pass

if __name__ == '__main__':
    xiaom = Prentice()
    # print(xiaom.gongfu)
    # # print(xiaom.name)
    # xiaom.make_cake()
    print(xiaom.name)