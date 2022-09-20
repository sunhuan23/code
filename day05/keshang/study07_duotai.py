class Dog:
    def work(self):
        print('指哪打哪')

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追击毒品')

class Rebot:
    def work(self):
        print('下棋')

class person:
    def work_with(self,dog):
        dog.work()

if __name__ == '__main__':
    d1 = Dog()
    d2 = ArmyDog()
    d3 = DrugDog()
    d4 = Rebot()
    p1 = person()
    p1.work_with(d4)
