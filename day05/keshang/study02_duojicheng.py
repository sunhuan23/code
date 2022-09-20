class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'

    def make_cake(self):
        print(f'运用{self.gongfu}制作了煎饼')

class School:
    def __init__(self):
        self.gongfu = '[香辣配方]'

    def make_cake(self):
        print(f'运用{self.gongfu}制作了煎饼')

# 多继承执行顺序，先从第一个类找
class Prentice(School,Master):
    pass

if __name__ == '__main__':
    xiaomig = Prentice()
    print(xiaomig.gongfu)
    xiaomig.make_cake()