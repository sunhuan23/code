"""
3.开发一个注册系统，
页面：
[{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
----------------

*   1-新增用户
*   2-查询单个用户信息
*	3-查询全部用户信息
*   4-删除用户
----------------
功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
功能2：查询学生信息
功能3：删除学生信息
"""
# 新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
def read_file():
    with open('info.txt','r+',encoding='utf-8') as f:
        info = f.readlines()
        return info

def add_student_inpfo():
    """
    添加学生信息
    """
    with open('info.txt', 'r+', encoding='utf-8') as f:

        dict1 = {}
        dict1['name'] = input("请输入学生姓名：")
        dict1['age'] = int(input('请输入学生年龄：'))
        info = f.readlines()
        for i in info:
            student_info = eval(i)
            if student_info['name'] == dict1['name']:
                print('学生已存在')
                return
        else:
            f.write(str(dict1)+'\n')

            print('新增用户成功')


def read_student_info(name):
    """
    1、查询某个学生的信息
    :param name: 查询的学生姓名
    """
    with open('info.txt','r+',encoding='utf-8') as f:
        info = f.readlines()
        for i in info:
            student_info = eval(i)
            if student_info['name'] == name:
                print(f'{name}的信息{i}')
                break
        else:
            print(f'没有{name}的信息')


def read_all_info():
    """
    1、查询所有的学生信息
    """
    with open('info.txt','r+',encoding='utf-8') as f:
        info = f.readlines()
        for i in info:
            print(i)
        print('以上为所有学生信息')


def del_student_info(name):
    """
    1、删除某个学生的信息
    :param name: 需要删除的学生姓名
    """
    student_info = read_file()
    for i in student_info:
        info = eval(i)
        if info['name'] == name:
            student_info.remove(i)
            print(f'{name}信息删除成功')
            with open('info.txt','w+',encoding='utf-8') as f:
                for i in student_info:
                    f.write(i)
            break
    else:
        print('学生信息不存在')


def register_system():
    while True:
        print('-------------')
        print('1-新增用户')
        print('2-查询单个用户信息')
        print('3-查询全部用户信息')
        print('4-删除用户')
        print('-------------')
        the_input = int(input('请输入您的操作（1-新增用户，2-查询单个用户信息，3-查询全部用户信息，4-删除用户）：'))
        if the_input == 1:
            add_student_inpfo()
        elif the_input == 2:
            name = input('请输入你要查询的学生姓名：')
            read_student_info(name)
        elif the_input == 3:
            read_all_info()
        elif the_input == 4:
            name = input('请输入你要删除的学生姓名：')
            del_student_info(name)
        elif the_input == 5:
            break
        else:
            print("您的输入有误，请重新输入")

register_system()