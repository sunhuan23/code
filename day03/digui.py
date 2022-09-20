"""
递归：
    1、自己调用自己
    2、要有出口

"""

def sum_num(num):

    if num ==1:
        return 1
    return num + sum_num(num-1)

res = sum_num(3)
print(res)

