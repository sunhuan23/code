class Master:
    def __init__(self):
        self.gongfu = '[五香配方]'
        # 私有属性只能在类内部调用
        self.__money = 200

    def make_cake(self):
        print(f'运用{self.gongfu}制作了煎饼')

    # 私有方法只能在类内部调用
    def __print_money(self):
        print(self.__money)

    def print1(self):
        self.__money +=1
        self.__print_money()

    def get_money(self):
        self.__print_money()

    def set_money(self):
        self.__money += 1

class Prentice(Master):
    pass

if __name__ == '__main__':
    xiaomig = Prentice()
    print(xiaomig.gongfu)
    xiaomig.get_money()
    xiaomig.set_money()
    xiaomig.get_money()
    xiaomig.print1()