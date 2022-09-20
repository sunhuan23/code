class Dog:
    def work(self):
        print('指哪咬哪')

class Adog(Dog):
    def work(self):
        print('追击坏人')

class Bdog(Dog):
    def work(self):
        print('追击毒品')

class p:
    def w(self,dog):
        dog.work(self)
if __name__ == '__main__':
    d1 = Dog
    d2 = Adog
    d3 = Bdog
    xiaom = p()
    xiaom.w(d1)
