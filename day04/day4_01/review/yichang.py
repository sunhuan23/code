"""
"""
"""
try:
 可能发⽣错误的代码
except:
 如果出现异常执⾏的代码

"""
# try:
#     open('test.txt','r')
# except:
#     print('文件不存在')

"""
捕获异常
try:
 可能发⽣错误的代码
except 异常类型:
 如果捕获到该异常类型执⾏的代码
"""
# try:
#     open('test.txt','r')
# except FileNotFoundError:
#     print('文件不存在')
"""
捕获多个异常
"""
# try:
#     # open('test.txt','r')
#     print(a)
# except (FileNotFoundError,NameError):
#     print('文件/名字 不存在')
"""
捕获异常描述信息
"""
# try:
#     open('test.txt','r')
#     print(a)
# except (FileNotFoundError,NameError) as result:
#     print(result)
"""
捕获所有异常
"""
# try:
#     # open('test.txt','r')
#     print(a)
# except Exception as result:
#     print(result)

"""
异常的else，表示没有异常时执行的代码 
"""
# try:
#     print(1)
# except:
#     print("异常执行的代码")
# else:
#     print('没有异常执行的代码')

"""
异常的finally，表示有没有异常都会执行的代码
"""
# def func1():
#     try:
#         print(1)
#         return 1
#     except:
#         print('异常执行的代码')
#     finally:
#         print('有无异常都执行的代码')
#     print(1)
# func1()

"""
raise 异常类名()
"""

# try:
#     try:
#         1/0
#         # print(a)
#     except NameError as msg:
#         print(f'异常信息{msg}')
#         raise msg
# except Exception as msg:
#     print(f'异常信息{msg}')