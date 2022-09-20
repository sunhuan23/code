
# r，打开文件，文件不存在报错
# w,打开文件，文件不存在则创建文件
f = open('test.txt','r+',encoding='utf-8')
# f.write('aaa')
# f.writelines(['\n123','456'])
# # 修改光标的位置，0文件开头，1当前位置，2文件结尾
# f.seek(0,0)
# print(f.read(5))
# 读取当前光标后所在行的内容
print(f.readlines())
# 读取光标后的所有行
# f.write('qq')
# f.write('qq')
print(f.tell())













f.close()