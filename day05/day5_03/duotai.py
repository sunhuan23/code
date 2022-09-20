"""
子类重写父类，调用不同的子类的相同父类的方法可以产生不同的结果
"""
class Dog:
    def work(self):
        print('指哪打哪')
class ArmyDog(Dog):
    def work(self):
        print('追击敌人')
class DrupDog(Dog):
    def work(self):
        print('追击毒品')
class Person:
    def work_with_dog(self,dog):
        dog.work()


"""
类属性，实例属性
"""

if __name__ == '__main__':
    ad = ArmyDog()
    dd = DrupDog()
    daqiu = Person()
    daqiu.work_with_dog(ad)
    daqiu.work_with_dog(dd)