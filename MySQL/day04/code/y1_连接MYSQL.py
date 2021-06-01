import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='201314', database='mydb3', charset='utf8')

# 创建游标对象: 可以执行sql语句
cursor = conn.cursor()

# sql语句
sql = 'select version()'

# 执行sql语句
cursor.execute(sql)

res = cursor.fetchone()
print(res)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()