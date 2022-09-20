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
    def __init__(self):
        self.gongfu = '[独创配方]'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.gongfu}制作了煎饼')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)

        School.make_cake(self)


if __name__ == '__main__':
    xiaomig = Prentice()
    print(xiaomig.gongfu)
    xiaomig.make_cake()
    xiaomig.make_master_cake()
    xiaomig.make_school_cake()
    xiaomig.make_cake()

