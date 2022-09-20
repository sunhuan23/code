"""
异常
"""
# 以r的方式打开一个不存在的文件
# open('test.txt','r')

"""
语法：
try：
    可能发生错误的代码
except：
    如果出现异常执行的代码
"""
try:
    open('test.txt','r')
except:
    open('test.txt','w')
"""
捕捉指定异常
语法：
try：
    可能发生错误的代码
except 异常类型：
    捕捉到该异常执行的代码
"""
try:
    print(name)
except NameError:
    print('name没有被定义')

"""
捕获多个指定异常
"""
try:
    print(name)
    print(1/0)
except (NameError,ZeroDivisionError):
    print('有错误')

"""
捕捉异常描述信息
"""
try:
    print(name)

    print(1/0)
except (NameError,ZeroDivisionError) as res:
    print(res)

"""
捕捉所有异常
"""
try:
    print(1/0)
    print(name)

except Exception as res:
    print(res)

"""
异常的else
"""
try:
    print("可能出现异常的代码")
except:
    print('遇到报错执行的代码')
else:
    print('没有异常执行的代码')

"""
异常的finally
"""
try:
    print("可能出现异常的代码")
except:
    print('遇到报错执行的代码')
else:
    print('没有异常执行的代码')
finally:
    print('有没有异常都会执行的代码')
def fun1():
    try:
        print("可能出现异常的代码")
        return '123'
    except:
        print('遇到报错执行的代码')

    finally:
        print('有没有异常都会执行的代码')


print(fun1())

"""
1. 尝试只读⽅式打开test.txt⽂件，如果⽂件存在则读取⽂件内容，⽂件不存在则提示⽤户即可。
2. 读取内容要求：尝试循环读取内容，读取过程中如果检测到⽤户意外终⽌程序，则 except 捕获异常
并提示⽤户
"""
import time
try:
    f =  open('test.txt','r')
    try:
        while True:
            con = f.readlines()
            if len(con) == 0:
                break
            time.sleep(2)
            print(con)
    except:
        print("意外中止")
    finally:
        f.close()

except:
    print('文件不存在')

"""
自定义异常
"""

try:
    print(1/0)
    print(name)

except Exception as res:
    raise res
