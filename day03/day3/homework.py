# 1.使用列表推导式生成能被5整除的数（100以内）
list1 = [i for i in range(100) if i % 5 == 0]
print(list1)
# 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
list1 = ["小明","小红"]
list2 = [18,19]
dict1 = {}
for i in range(len(list1)):
    dict1[list1[i]] = list2[i]
print(dict1)
# {"小明":18,"小红":19}
# 3.开发一个注册系统，
# 页面：
# [{name:xxx,age:xxx},{name:xxx,age:xxx},{name:xxx,age:xxx}]
# ----------------
#
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
def add_info():
    with open('info.txt','r+',encoding="utf-8")  as f:
        s_info = f.readlines()
        print(s_info)
        dict1 = {}
        dict1['name'] = input('请输入您要添加的学生姓名：')
        dict1['age'] = input('请输入您要添加的学生年龄：')
        for i in s_info:
            if i != '\n':
                if dict1['name'] == eval(i)['name']:
                    print(f'学生{dict1["name"]}已存在')
                    break
        else:
            f.write(str(dict1))
            f.write('\n')
            print(f'{dict1["name"]}的信息添加成功')

# 功能2：查询学生信息
def view_info():
    with open('info.txt','r',encoding='utf-8') as f:
        s_info = f.readlines()
        name = input('请输入您要查询的学生姓名：')
        for i in s_info:
            if i != '\n':
                if name == eval(i)['name']:
                    print(i)
                    break
        else:
            print('您要查询的学生信息不存在')


def all_info():
    with open('info.txt','r',encoding='utf-8') as f:
        s_info = f.readlines()
        for i in s_info:
            print(i)

def del_info():
    with open('info.txt','r',encoding='utf-8') as f:
        s_info = f.readlines()
    name = input('请输入您要删除的名字：')
    for i in s_info:
        if name == eval(i)['name']:
            s_info.remove(i)
            with open('info.txt', 'w+', encoding='utf-8') as f1:
                for j in s_info:
                    f1.write(j)
                print(f'{name}的信息已删除')
            break
    else:
        print(f'{name}的信息不存在')


def master():
    while True:
        print('-'*20)
        print("*    1 - 新增用户")
        print("*    2 - 查询单个用户信息")
        print("*    3 - 查询全部用户信息")
        print("*    4 - 删除用户")
        print('-'*20)
        opaeration = int(input('请输入您的操作：'))

        if opaeration == 1:
            add_info()
        elif opaeration == 2:
            view_info()
        elif opaeration == 3:
            all_info
        elif opaeration == 4:
            pass
        elif opaeration == 5:
            break
del_info()



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