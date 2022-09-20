# targt=7
# l=[1,2,2,2,3,7,0,7,9,4,5]
# l1 = [1,1,2,3,4,4,4,5,6,6]
#
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i] + l[j] == targt:
#             print(i,j)
#
# for i in range(len(l1)-1,-1,-1):
#     if l1[i] == l1[i-1]:
#         l1.remove(l1[i])
# print(l1)

import re
# str1 = '2018-10-12'
# # res = re.findall('^(\d{4})-(\d{2})-(\d{2})$',str1)
# res = re.search('^(\d{4})-(\d{2})-(\d{2})$',str1)
# print(res.group())
# print(res.group(1))

# 使用compile编译正则表达式
# kk = re.compile(r'\d')
# # 通过表达式的对象抵用findall
# result = kk.findall('aa1bbcc2hh3')
# # 使用re调用findall
# result1 = re.findall(kk,'aa1bbcc2hh3')
#
# print(result1)

str1 = """
2. <body>
3. <div>
4. <span class="c-text c-text-hot opr-toplist1-label">橙好牛逼</span>
5. </div>
6. </body>
7.
8. """
res = re.compile('>(\w+)<')
res1 = re.findall(res,str1)
print(res1)