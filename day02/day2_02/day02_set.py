set1 = {7,1,2,4,'a',1,10,3,5}
print(set1)
set1.add('xiaom')
print(set1)
set1.update({'xiaoh','xiaom'})
print(set1)

# 数据不存在报错
set1.remove('xiaom')
print(set1)
# 数据不存在不会报错
set1.discard('xiaohei')
print(set1)
