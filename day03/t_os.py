import os

# 修改文件名,找不到会报错
# os.rename('test.txt','test1.txt')

# 删除文件,找不到会报错
# os.remove('test1.txt')

# 新建文件夹,文件名已存在会报错
# os.mkdir('test1')

# 删除文件夹，文件不存在会报错
# os.rmdir('test1')

# 查看自己当前目录
print(os.getcwd())

# 改变默认目录
# os.chdir('/Users/sunhuan')
print(os.getcwd())

# 查看当文件夹下的内容
print(os.listdir())  # 返回一个列表

# 获取文件所在目录
print(os.path.dirname('/Users/sunhuan/chenghao/day03/t_os.py'))

# 获取当前文件的所在路径
print(os.path.dirname(__file__))

# 获取当前文件的绝对路径
print(os.path.abspath(__file__))




