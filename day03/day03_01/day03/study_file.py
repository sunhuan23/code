import os

f = open('test01.txt', 'r+', encoding='utf-8')
print(f.tell())
# f.write('abcde')
f.seek(5)
f.write('udeuehdekd')
print(f.tell())
t = f.read(5)
print(t)
print(f.tell())

f.close()
# os.rename('test1.txt','test01.txt')
print(os.path.dirname(__file__))
# os.mkdir('sunhuan')
# os.rmdir('sunhuan')
