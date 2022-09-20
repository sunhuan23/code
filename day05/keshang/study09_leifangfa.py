class Dog:
    tooth = 10

    def __init__(self,name):
        self.name = name
    # 类方法
    @classmethod
    def get_tooth(cls):
        return cls.tooth
    # 静态方法
    @staticmethod
    def a(a,b):
        print(a + b)

if __name__ == '__main__':
    xiaohuang = Dog('xiaohuang')
    print(xiaohuang.get_tooth())
    print(xiaohuang.tooth)
    xiaohei = Dog('小黑')
    xiaohei.tooth =8
    print(xiaohei.tooth)
    print(xiaohei.get_tooth())

    xiaohei.a(1,2)

    # print(Dog.tooth)
    # xiaohei = Dog('xiaohei')
    # xiaohei.tooth =8
    # print(xiaohei.tooth)
    # Dog.tooth =12
    # print(Dog.tooth)
    # print(xiaohei.tooth)
