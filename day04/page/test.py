# 方式一：import 模块名
import my_module

# my_module.a_testA(2,1)

# 方式二：from 模块名 import 方法名
# from my_module import a_testA
# a_testA(3,1)

# 方式三：from 模块名 import *
# from my_module import *
# a_testA(3,1)
# a_testB(3,1)

# 重命名
# import my_module as my
# my.a_testA(3,0)
#
# from my_module import a_testA as a
# a(3,0)

# from my_module import *
# a_testA(3,1)
# # b_testB(3,1)

"""
包导入
"""

# 方式一：
# import my_packge.my_module1
# my_packge.my_module1.info_print1()

# 方式二：
# from my_packge import my_module1
# my_module1.info_print1()

# 方式三：
# from my_packge.my_module1 import *
# info_print1()

# __all__
from my_packge import *
my_module2.info_print1()

