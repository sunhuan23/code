import copy
# s = '123455'
# print(id(s))
# s1 = copy.copy(s)
# print(id(s1))

l1 = ['111',1,3,5,(1,2,3),[1,2,4]]
print(id(l1))
l2 = copy.deepcopy(l1)
print(l2)
print(id(l2))
l1[0] = '222'
l1[4] = 4
l1[-1][0] = 2
print(l1)
print(l2)
print(id(l1[-1]))
print(id(l2[-1]))