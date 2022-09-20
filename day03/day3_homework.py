# 1.使用列表推导式生成能被5整除的数（100以内）
# list1 = [i for i in range(100) if i % 5 == 0]
# print(list1)
# # 2.有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄
# list1 = ["小明","小红"]
# list2 = [18,19]
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)

# {"小明":18,"小红":19}
# 3.开发一个注册系统，
# 页面：
# [,{name:xxx,age:xxx},{name:xxx,age:xxx}]
# ----------------
#
# *   1-新增用户
# *   2-查询单个用户信息
# *	  3-查询全部用户信息
# *   4-删除用户
# ----------------
# 功能1：新增学生信息（姓名和年龄）通过键盘，如果学生已经存在提示用户已存在
# 功能2：查询学生信息
# 功能3：删除学生信息

def master():
    while True:

        print('-'*20)
        print('* 1 - 新增用户')
        print('* 2 - 查询单个用户信息')
        print('* 3 - 查询全部用户信息')
        print('* 4 - 删除用户')
        print('* 5 - 退出系统')
        print('-'*20)
        num = int(input('请输入您的操作：'))
        if num ==1:
            add_info()
        if num ==2:
            only_info()
        if num ==3:
            select_info()
        if num ==4:
            del_info()
        if num ==5:
            break

def add_info():
    with open('info.txt','r+',encoding='utf-8') as f:
        infolist = f.readlines()
        dict1 = {}
        dict1['name'] = input('请输入学生名称')
        dict1['age'] = input('请输入年龄')
        for i in infolist:
            print(i)
            if dict1['name'] == eval(i)['name']:
                print(f'{dict1["name"]}信息已存在')
                break
        else:
            f.write(str(dict1)+'\n')
def select_info():
    with open('info.txt','r',encoding='utf-8') as f:
        infolist = f.readlines()
        for i in infolist:
            print(i)
        print('以上为所以学生信息')
def only_info():
    with open('info.txt','r',encoding='utf-8') as f:
        infolist = f.readlines()
        name = input('请输入你要查询的名字：')
        for i in infolist:
            if name == eval(i)['name']:
                print(i)
                break
        else:
            print(f'没有{name}的信息')
def del_info():
    with open('info.txt','r',encoding='utf-8') as f:
        infolist = f.readlines()
        name = input('请输入你要删除的名字：')
        for i in infolist:
            if name == eval(i)['name']:
                infolist.remove(i)
                print(f'{name}信息删除成功')
                break
        else:
            print(f'没有{name}的信息')
        with open('info.txt','w',encoding='utf-8') as f1:
            for j in infolist:
                f1.write(j)

master()