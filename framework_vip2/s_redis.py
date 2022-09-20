# 导入数据库操作包
import redis
"""
1、创建数据库连接对象
    host=redis服务器地址，port默认端口，db默认第一个数据库0，连接redis
    加上decode_responese = True,写入的键值对的value为str类型，不加这个参数，写入的则是字节类型
2、操作数据库语句
    添加，set（key，value）
3、查询数据库
"""
r = redis.Redis(host='127.0.0.1', port=6379,db=0, decode_responses=True)
r.set('name','张三')
print(r.get('name'))