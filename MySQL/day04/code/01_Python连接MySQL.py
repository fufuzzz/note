import pymysql


# 1.连接MySQL(确保MySQL服务器已经启动)
# mysql -u root -p
#  表示本机: localhost, 127.0.0.1, ip
# db = pymysql.connect(host='localhost', port=3306, user='root', passwd='201314', database='mydb3', charset='utf8')

# 1.连接MySQL, db:MySQL的连接对象
db = pymysql.connect(user='root', passwd='201314', database='mydb3')
# print(db)
# <pymysql.connections.Connection object at 0x000001CD6C31E390>

#   游标: 执行SQL语句
cur = db.cursor()


# 2.查询数据
sql = 'select * from person'
#   执行sql
cur.execute(sql)
#   得到查询的数据
result = cur.fetchall()
print(result)

# 3.关闭数据库
cur.close()
db.close()
