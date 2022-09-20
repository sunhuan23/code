"""
面向对象的继承指的是多个类中间的所属关系，即子类默认继承父类的属性和方法
"""
# class A:
#     def __init__(self):
#         self.num = 10
#     def sum(self):
#         print(self.num)
#
#
# class B(A):
#     pass
# if __name__ == '__main__':
#     b = B()
#     print(b.num)
#     b.sum()

"""
徒弟继承师傅的所有技术
"""
class Master:
    def __init__(self):
        self.gongfu  = '[五香配方]'
    def make_cake(self):
        print(f'运用{self.gongfu}制作了煎饼')

class Prentice(Master):
    pass

if __name__ == '__main__':
    xiaom = Master()
    print(xiaom.gongfu)
    xiaom.make_cake()
