"""
while 条件:
    条件成立重复执行的代码1
    条件成立重复执行的代码2 ......
"""
# 1-100的累加和,即1 + 2 + 3 + 4 +......,即前两个数字的相加结果 + 下一个数字(前一个数字 + 1)
i = 1
result = 0
while i <= 100:
    result += i
    i += 1
print(result)

# 计算1-100偶数累加和
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i += 1
print(result)

# 吃5个苹果
i = 1
while i <= 5:
    print(f"吃第{i}个苹果")
    i +=1

# 吃到第三个苹果吃饱了
i = 1
while i <= 5:
    if i == 3:
        print("吃饱了")
        break
    print(f"吃第{i}个苹果")
    i +=1

# 吃第三个苹果吃到了虫子，不过可以继续吃
i = 1
while i <= 5:
    if i == 3:
        print("有虫子")
        i += 1
        continue
    print(f"吃第{i}个苹果")
    i +=1
# 每天道歉三遍，道三天
i = 1
while i<=3:
    print(f"第{i}天")
    j = 1
    while j <= 3:
        print("我错了")
        j += 1
    i += 1
else:
    print("原谅我了")
# 使用break
i = 1
while i <= 3:
    print("我错了")
    if i == 2:
        print("第二遍不真诚，别说了")
        break
    i += 1
else:
    print("原谅我了")
# 使用continue
i = 1
while i <= 3:
    print("我错了")
    if i == 2:
        print("第二遍不真诚，再看看")
        i += 1
        continue
    i += 1
else:
    print("原谅我了")