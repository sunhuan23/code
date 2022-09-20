import pymysql
from common.ReadConfig import ReadConfig
"""
1、连接数据库
2、创建游标，用来查询和写入
3、预备一个sql语句
4、执行sql
5、提交对数据库有改动的sql
5、关闭游标
6、关闭数据库
 
"""

# 1、连接数据库
conn = pymysql.connect(host='192.168.3.46',
                       user='root',
                       password='',
                       database='test')
# 2、创建游标，用来查询和写入
curs = conn.cursor()
# 3、预备一个sql语句
sql = "insert into user_info_yang values(%s,%s,%s,%s)"
# 4、执行sql
inser = curs.execute(sql,(77,'泡泡','20',''))
# 5、提交对数据库有改动的sql
conn.commit()
sql = 'select * from user_info_yang'
# 执行sql
sel = curs.execute(sql)
print(sel)
# 查询一条用例
print(curs.fetchone())
# 查询多条用例
print(curs.fetchmany(7))
# 查询全部用例
print(curs.fetchall())
# 6、关闭游标
curs.close()
# 7、关闭数据库
conn.close()