class Dog:
    __name = 'wa'
    def __init__(self,age = 10):
        self.age =age
    def eat(self):
        print(f'我叫{self.__name},{self.age}')
    @classmethod
    def cls1(cls):

        return cls.__name,cls(11)
    @staticmethod
    def st(a, b):
        print(a +b)

if __name__ == '__main__':
    wangcai = Dog()
    print(wangcai.cls1())
    wangcai.eat()
    wangcai.st(1,2)
    Dog.st(3,5)
    # wangcai.age = 1
    # Dog.name = 'XIAOH'
    # print(wangcai.name)
    # a = Dog()
    # a.eat()
    # a.name = 'xiaom'
    # a.eat()