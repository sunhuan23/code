# 运算符
"""
算数运算符：
    +  加    ：1 + 1输出结果为  2
    -  减    ：1 - 1输出结果为  0
    *  乘    ：2 * 2输出结果为  4
    /  除    ：10 / 2输出结果为 5
    // 取整  ：9 // 4输出结果为 2
    %  取余  ：9 % 4输出结果为  1
    ** 指数  ：2 ** 4输出结果为 16,即2 *2 * 2 *2
    () 小括号：小括号用来提高运算优先级,即(1 + 2) * 3 输出结果为 9
"""

a = 4
b = 9
c = 2
print(f"{a}+{b}={a+b}")  # 加
print(f"{a}-{b}={a-b}")  # 减
print(f"{a}*{b}={a*b}")  # 乘
print(f"{a}/{b}={a/b}")  # 除》--->2
print(f"{a}%{b}={a%b}")   # 取余  --->1
print(f"{c}**{a}={c**a}")  # 指数，相当于2的2次方
"""
赋值运算符：
    =  ： 将 = 右侧的结果赋值给等号左侧的变量
"""
a, b, c = 4, 5, 6
print(a)
print(c)

a = d = 10
print(d)


"""
复合赋值运算符：
    += 加法赋值运算符 ： c += a  等价于 c = c + a
    -= 减法赋值运算符 ： c -= a  等价于 c = c - a
    *= 乘法赋值运算符 ： c *= a  等价于 c = c * a
    /= 除法赋值运算符 ： c /= a  等价于 c = c / a
    //= 整除赋值运算符： c // a  等价于 c = c // a
    %= 取余赋值运算符 ： c % a   等价于 c = c % a
    **= 幂赋值运算符  ： c ** a  等价于 c = c ** a
"""
a = 4
a += 1
print(a)  # -->5


"""
比较运算符：
    == 判断相等 :  如果两个操作数的结果相等,则条件结果为真(True),否则条件结果为假(False)       
                  如a = 3,b = 3,则(a == b)为True,如a =1,b = 3，则(a == b)为False
    != 不等于   :  如果两个操作数的结果不相等,则条件为真(True),否则条件结果为假(False)         
                  如a = 3,b = 3,则(a != b)为False,如a =1,b = 3,则(a != b)为True
    >  大于     :  运算符左侧操作数结果是否大于右侧操作数结果,如果大于,则条件为真,否则为假       
                  如a = 7,b = 3,则(a > b)为 True, (b > a)为False
    <  小于：   :  运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为真，否则为假  
                  如a = 7,b = 3，则(a < b) 为 False ，（b < a）为True
    >= 大于等于  : 运算符左侧操作数结果是否大于等于右侧操作数结果，如果大于或等于，则条件为真，否则为假  
                  如a = 7,b = 3，则(a >= b)为 True,(b >= a) 为 False
                  如a = 7，b = 7，则(a >= b)为 True
    <= 小于等于  : 运算符左侧操作数结果是否小于等于右侧操作数结果，如果小于或等于，则条件为真，否则为假  
                  如a = 3,b = 3，则(a <= b) 为 True
"""
a = 3
b = 3
c = 6
print(f"{a}等于{b}:{a==b}")  # True
print(f"{a}等于{c}:{a==c}")  # False
print(f"{a}不等于{c}:{a!=c}")  # True
print(f"{a}不等于{b}:{a!=b}")  # False
print(f"{a}大于{c}:{a>c}")  # False
print(f"{c}大于{a}:{c>a}")  # True
print(f"{a}小于{c}:{a<c}")  # True
print(f"{c}小于{a}:{c<a}")  # False
print(f"{c}大于等于{a}:{c>=a}")  # True
print(f"{b}大于等于{a}:{b>=a}")  # True
print(f"{a}大于等于{c}:{a>=c}")  # False
print(f"{c}小于等于{a}:{c<=a}")  # False
print(f"{b}小于等于{a}:{b<=a}")  # True
print(f"{a}小于等于{c}:{a<=c}")  # True

"""
逻辑运算符：
    and  且 ：  x and y，同时满足(都为true)返回True，否则返回False
    or   或 ：  x or y，任意一方为true，返回True，否则返回false
    not  非 ：  not(x)，取反，x为True,返回False,x为False,返回True
    
"""
a = 3
b = 3
c = 6

print((a < c) and (a == b))  # and 是返回第一个假值，如果都为真，则返回最后一个真值
print((a > c) and (a == b))  # 返回第一个假值
print((a > c) or (a == b))  # 返回第一个真值，如果都为假，返回最后一个假值
print((a > c) or (a != b))  # 都不满足返回false
print(not(a != b))  # 取反返回true


