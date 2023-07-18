#!/usr/bin/python3

import pymysql.connections

# 打开数据库连接
db = pymysql.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="seckill"
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * FROM seckill")

# 使用 fetchall() 方法获取s所有数据
data = cursor.fetchall()

print(data)

# version = cursor.fetchone()

# 关闭数据库连接
db.close()

