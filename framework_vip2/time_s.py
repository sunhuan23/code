import pymysql
# import time
# # 睡眠
# time.sleep(1)
# print(5)
#
# # 获取当前时间的时间戳
# print(time.time())
#
# # 获取当前时间对象
# print(time.localtime())
#
# # 获取当前格林威治时间对象
# print(time.gmtime())
#
# # 把时间对象转化为时间戳
# print(time.mktime(time.localtime()))
#
# # 将对象转为外国常用的格式固定输出,接收秒，不穿默认当前时间
# print(time.asctime())
#
# # 将时间戳按照外国常见格式输出,接收秒，不穿默认当前时间
# print(time.ctime())
#
# # 将时间对象按照自己定义的格式输出
# print(time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime()))
#
# import unittest
# from HTMLTestRunner import HTMLTestReportCN
#
# a = ' '
# print(a.lower())
conn = pymysql.connect(host='192.168.3.46',
                       user='root',
                       password='',
                       database='test')
# 获取游标，用来查询写入
curs= conn.cursor()
# 增删改查
sql = "insert into user_info_yang values(%s,%s,%s,%s)"
# insr = curs.execute(sql,(40,'孙欢',18,''))
# conn.commit()
# print(insr)
# 增加多条数据
insr = curs.executemany(sql,[(41,'孙欢',18,''),(42,'孙欢1',18,'')])
# 提交
conn.commit()
print(insr)

sql = 'select * from user_info_yang'
# 查询sql
curs.execute(sql)
# 查询一条数据
# print(curs.fetchone())
# # 查询多条数据
# print(curs.fetchmany(3))
# # 查询全部数据
# print(curs.fetchall())
# # 关闭游标
# curs.close()
# # 关闭数据库
# conn.close()


