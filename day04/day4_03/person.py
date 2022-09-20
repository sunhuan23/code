"""
2、小明爱跑步，爱吃东西。
    1）小明体重75.0公斤
    2）每次跑步会减肥0.5公斤
    3）每次吃东西体重会增加1公斤
    4）小美的体重是45.0公斤
"""
class Person:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1
    def __str__(self):
        return f'{self.name}的体重是{self.weight}'
if __name__ == '__main__':
    xiaom = Person('小明',70)
    xiaom.run()
    xiaom.eat()
    print(xiaom)