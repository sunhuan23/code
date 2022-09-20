# 文件中是有__all__时，其他文件只能导入列表重的方法
__all__ = ['func1']

def func1(a,b):
    print(a +b)

def func2(a,b):
    print(a *b)
