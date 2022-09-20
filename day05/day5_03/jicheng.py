"""
单继承
"""
# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(Master):
#     pass

"""
多继承
"""
# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class School:
#     def __init__(self):
#         self.gongfu = '[香辣]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(School,Master):
#     pass

"""
子类重写父类同名属性和方法
默认使用子类
"""

# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class School:
#     def __init__(self):
#         self.gongfu = '[香辣]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(School,Master):
#     def __init__(self):
#         super().__init__()
#         self.gongfu = '[自制]'
#
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
"""
子类调用父类同名方法属性
"""
# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class School:
#     def __init__(self):
#         self.gongfu = '[香辣]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(School,Master):
#     def __init__(self):
#         super().__init__()
#         self.gongfu = '[自制]'
#
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#     def master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
"""
多层继承
"""
# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class School:
#     def __init__(self):
#         self.gongfu = '[香辣]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(School,Master):
#     def __init__(self):
#         super().__init__()
#         self.gongfu = '[自制]'
#
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#     def master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
# class Tusun(Prentice):
#     pass

"""
super()
"""
# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class School:
#     def __init__(self):
#         self.gongfu = '[香辣]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(School,Master):
#     def __init__(self):
#         super().__init__()
#         self.gongfu = '[自制]'
#
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#     def master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#     def make_old_cake(self):
#         super().__init__()
#         super().make_cake()
"""
私有属性和方法
"""
# class Master:
#     def __init__(self):
#         self.gongfu = '[五香]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class School:
#     def __init__(self):
#         self.gongfu = '[香辣]'
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#
# class Prentice(School,Master):
#     def __init__(self):
#         super().__init__()
#         self.gongfu = '[自制]'
#         self.__money = 200
#
#     def make_cake(self):
#         print(f'运行{self.gongfu}制作')
#     def master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#     def make_old_cake(self):
#         super().__init__()
#         super().make_cake()
# class Tusun(Prentice):
#     pass
"""
获取和设置私有属性
"""
class Master:
    def __init__(self):
        self.gongfu = '[五香]'
    def make_cake(self):
        print(f'运行{self.gongfu}制作')

class School:
    def __init__(self):
        self.gongfu = '[香辣]'
    def make_cake(self):
        print(f'运行{self.gongfu}制作')

class Prentice(School,Master):
    def __init__(self):
        super().__init__()
        self.gongfu = '[自制]'
        self.__money = 200
    def get_money(self):
        return self.__money
    def set_money(self):
        self.__money =100

    def make_cake(self):
        print(f'运行{self.gongfu}制作')
    def master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def school_cake(self):
        School.__init__(self)
        School.make_cake(self)
    def make_old_cake(self):
        super().__init__()
        super().make_cake()
class Tusun(Prentice):
    pass

if __name__ == '__main__':
    p = Prentice()
    print(p.gongfu)
    # print(p.__money)
    p.make_cake()
    p.master_cake()
    p.school_cake()
    p.make_old_cake()
    print(p.get_money())
