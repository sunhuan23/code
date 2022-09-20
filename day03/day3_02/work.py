# 1.使用列表推导式生成能被5整除的数（100以内）
list1 = [i for i in range(100) if i % 5 == 0]
print(list1)
# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
list1 = ["小明","小红"]
list2 = [18,19]
# {"小明":18,"小红":19}
dict1 = {list1[i]:list2[i] for i in range(len(list1))}
print(dict1)
# 3.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
# ----------------
#
# *   1-新增用户
# *   2-查询单个用户信息
# *	3-查询全部用户信息
# *   4-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息
#
#
#
# 复习重点:
# 定义函数
# 调用函数
# 传参方式
#
# 敲之前所有学过的代码,课上代码+课下作业

def master():
    while True:
        print('-'*20)
        print("*    1-新增用户")
        print("*    2-查询单个用户信息")
        print("*    3-查询全部用户信息")
        print("*    4-删除用户")
        print('-'*20)
        num = int(input('请输入您的操作：'))
        if num == 1:
            add_student()
        elif num == 2:
            sel_info()
        elif num == 3:
            sel_all_info()
        elif num == 4:
            del_info()
        elif num == 5:
            break
        else:
            print('输入有误')
"""
1、定义一个添加学生信息的方法
    打开文件
    读取文件的所有信息并返回列表
    输入要增加的学生信息
    判断学生是否存在列表中
        是，提示已存在
    否
        将数据写入文件
"""

def sel_info():
    with open('info.log','r',encoding='utf-8') as f:
        info_list = f.readlines()
        name = input('请输入你要查询的学生名称：')
        for i in info_list:
            if name == eval(i)['name']:
                print(i)
                break
        else:
            print('学生信息不存在')
def sel_all_info():
    with open('info.log','r',encoding='utf-8') as f:
        info_list = f.readlines()
        for i in info_list:
            print(i)
        print('以上为所有的学生信息')
def del_info():
    with open('info.log','r',encoding='utf-8') as f:
        info_list = f.readlines()
        print(info_list)
        name = input('请输入你要删除的学生名称：')
        for i in info_list:
            if name == eval(i)['name']:
                info_list.remove(i)
                with open('info.log','w',encoding='utf-8') as f1:
                    for i in info_list:
                        f1.write(i)
                break
        else:
            print('学生信息不存在')


# 1、定义一个添加学生信息的方法
def add_student():
    # 打开文件
    with open('info.log','r+',encoding='utf-8') as f:
        # 读取文件的所有信息并返回列表
        info_list = f.readlines()
        info_dict = {}
        # 输入要增加的学生信息
        info_dict['name'] = input('请输入要增加的学生姓名：')
        info_dict['age'] = input('请输入学生的年龄：')
        # 循环读取的数据列表
        for i in info_list:
        # 判断学生是否存在列表中
            if eval(i)['name'] == info_dict['name']:
                # 是，提示已存在
                print(f'{info_dict["name"]}信息已存在')
                break
            # 否
        else:
            # 将数据写入文件
            f.write(str(info_dict)+'\n')


if __name__ == '__main__':
    master()


