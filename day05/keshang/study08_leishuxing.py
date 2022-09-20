class Dog:
    tooth = 10

    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    xiaohuang = Dog('xiaohuang')
    print(xiaohuang.tooth)
    print(Dog.tooth)
    xiaohei = Dog('xiaohei')
    xiaohei.tooth =8
    print(xiaohei.tooth)
    Dog.tooth =12
    print(Dog.tooth)
    print(xiaohei.tooth)
