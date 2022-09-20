"""
字符串是Python中最常用的数据类型。我们一般使用引号来创建字符串
"""
str1 = "hello world"
print(str1)
print(type(str1))

myname = "tom"
# 输出'单引号可以使用转义符
print("i\'m tom")

# 字符串的输入
# name = input("请输入你的名字：")
# print(name)

"""
根据字符串的下标来获取数据，下标都是从0开始
"""
a = 'abcdefg'
print(a[0])
print(a[-1])
print(a[2])

"""
切片：a[开始位置：结束位置：步长]
    1. 不包含结束位置下标对应的数据,正负整数均可;
    2. 步长是选取间隔,正负整数均可,默认步长为1。
"""
a = 'abcdefg'

print(a[1:])  # --> bcdefg
print(a[:])   # --> abcdefg
print(a[:5])   # --> abcde
print(a[1: 4])  # -->bcd
print(a[1: 5: 2])  # --> bd
print(a[-1: 1])  # --> 无
print(a[::-1])  # --> 字符串反转
print(a[1:-2])  # --> bcde

"""
常用的操作方法：
"""
a = 'list duple Dict lIst setset aaa'
"""
查找（find）：检查某个子串是否在整个序列中，如果在返回子串所在的下标，如果不在返回-1
"""
print(a.find("list"))  # -->0,多个返回第一个
print(a.find("list", 1, 20))  # -->16, 进行某个区间查找
print(a.find("lista"))  # -->-1
# rfind:和find功能相同，从右往左找，返回的下标也一致
print(a.rfind("list"))  # -->16
print(a.rfind("list", 4, 20))  # -->16

"""
查找（index）：检查某个子串是否在整个序列中，如果在返回子串所在的下标，如果不在报错
"""
print(a.index("list"))  # -->0,多个返回第一个
print(a.index("lIst", 1, 20))  # -->16, 进行某个区间查找
# print(a.index("lista"))  # -->报错
# rindex: 和find功能相同，从右往左找，返回的下标也一致
print(a.rindex("list"))  # -->16
print(a.rindex("lIst", 4, 20))  # -->16

"""
count():返回某个子串在字符串中出现的次数,没有返回0
"""
print(a.count("l"))  # -->3
print(a.count("l", 0, 16))  # -->2

"""
修改（replace）：a.replace(旧子串,新子串,替换次数)，替换次数如果超出子串出现次数,则替换次数为该子串出现次数。

数据按照是否能直接修改分为可变类型和不可变类型两种。
字符串类型的数据修改的时候不能改变原有字符串,属于不能直接修改数据的类型即是不可变类型。

"""
print(a.replace("list", "int", 1))  # --> int duple dict list set
print(a.replace("d", "h", 5))  # -->list huple hict list set
print(a)  # --> list duple dict list set

"""
split():按照指定字符分割字符串，指定字符会被覆盖，返回一个列表
    a.split(分割字符,num),num指分割的次数
"""
print(a.split("i"))  # ['l', 'st duple d', 'ct l', 'st set ']
print(a.split("i", 1))  # ['l', 'st duple dict list set ']

"""
join():字符串中的每个字符都由_拼接合成一个新的字符串。
       '_'.join(a)
"""
print('_'.join(a))  # l_i_s_t_ _d_u_p_l_e_ _d_i_c_t_ _l_i_s_t_ _s_e_t_

# 将字符串第一个字母转为大写，其余字母都转为小写
print(a.capitalize())  # -->List duple dict list set

# 将字符串每个单词的首字母转为大写,非首字母的大写会转为小写
print(a.title())  # -->List Duple Dict List Setset Aaa

# 将字符串中大写转为小写
print(a.lower())  # -->list duple dict list setset aaa

# 将字符串中的小写转为大写
print(a.upper())  # -->LIST DUPLE DICT LIST SETSET AAA

# 去除字符串右侧的空格
a = '  哈 哈  '
print(a.rstrip())

# 去除左边的空格
print(a.lstrip())

# 去除左右两侧空格
print(a.strip())

a = '哈哈12'
# ljust():返回一个原字符串左对齐,并使用指定字符(默认空格)填充至对应长度的新字符串。
print(a.ljust(10, '_'))  # 哈哈________

# rjust():返回一个原字符串右对齐,并使用指定字符(默认空格)填充至对应长度的新字符串。
print(a.rjust(10, '_'))  # ________哈哈

#  center() 返回一个原字符串居中
print(a.center(10, '_'))

# startswith():检查字符串是否是以指定子串开头,是则返回True,否则返回False。如果设置开始和结 束位置下标,则在指定范围内检查。
print(a.startswith("哈"))
print(a.startswith("ha"))
print(a.startswith("哈", 1, 10))

# endswitch():检查字符串是否是以指定子串结尾,是则返回True,否则返回False。如果设置开始和结 束位置下标,则在指定范围内检查。
print(a.endswith("哈"))
print(a.endswith("ha"))
print(a.endswith("哈", 1, 10))

# isalpha():如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False
print(a.isalpha())
# isdigit():如果字符串只包含数字则返回True否则返回False
print(a.isdigit())
# isalnum():如果字符串至少有一个字符并且所有字符都是字母或数字则返回True,否则返回False
print(a.isalnum())
# isspace():如果字符串中只包含空白,则返回True,否则返回False
print(a.isspace())
