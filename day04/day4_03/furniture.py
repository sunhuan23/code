
# 3、摆放家具
#     需求：
#     1）.房子有户型，总面积和家具名称列表
#        新房子没有任何的家具
#     2）.家具有名字和占地面积，其中
#        床：占4平米
#        衣柜：占2平面
#        餐桌：占1.5平米
#     3）.将以上三件家具添加到房子中
#     4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
定义一个家具类
    定义一个初始化，家具的名字，面积

定义一个房子的类
    定义一个初始化方法
        属性
        户型
        总面积
        家具列表
        剩余面积


    定义一个房子的方法
        摆放家具，判断家具的面积是否大于剩余面积

    定义一个__str__

"""
class Furniture:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return f'{self.name}的占地面积是{self.area}'

class Hous:
    def __init__(self,modle,area):
        self.modle = modle
        self.all_area = area
        self.r_area = area
        self.f_list = []
    def add_furniture(self,f):
        if f.area < self.r_area:
            self.r_area -= f.area
            self.f_list.append(f.name)
        else:
            print('摆不下了')
    def __str__(self):
        return f'房子的户型是{self.modle},总面积{self.all_area},剩余面试{self.r_area},摆放的{self.f_list}'
if __name__ == '__main__':
    table = Furniture('桌子',10)
    bed = Furniture('床',30)
    print(table)
    home = Hous('三居室',220)
    home.add_furniture(table)
    home.add_furniture(bed)
    print(home)


