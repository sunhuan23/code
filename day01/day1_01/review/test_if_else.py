# 去网吧
# 输入年龄
# age = int(input("请输入你的年龄："))
# # 判断年龄是否>=18
# if age >= 18:
#     # 是，继续上网
#     print(f"你的年龄是{age},可以上网")
# # 不是回家写作业
# else:
#     print(f"你的年龄是{age},回家")

# 中国合法工作年龄为18-60岁,
# age = int(input("请输入你的年龄："))
# # 即如果年龄小于18的情况
# if age < 18 and age >0:
# #   为童工,不合法;
#     print(f"你的年龄是{age}岁,童工，不合法")
# #   如果年龄在18-60岁之间为
# elif age >=18 and age <= 60:
#     #   合法工龄;
#     print(f"你的年龄是{age}岁,合法工龄")
# elif age >60 :
#     #  大于60岁为法定退休年龄。
#     print(f"你的年龄是{age}岁，不符合合法工龄")
# else:
#     print("请输入合规")


# money = eval(input("请输入你的余额"))
# print(money)
# # 1.如果有钱,则可以上车
# if money > 0:
#     sit = int(input("请输入座位："))
#     # 2.上车后,如果有空座,可以坐下
#     if sit  > 0:
#         print("坐着去")
      # 如果没有空座,则站着等空座位
#     else:
#         print("站着去")
      # 上车后, 如果没钱,不能上车
# else:
#     print("腿着去")

# 三目运算符，条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
money = eval(input("请输入你的余额"))
print("可以上车") if money >0 else print("余额不足，不能上车")






