import pymysql
conn = pymysql.connect(
        user='root',
        password="201314",
        host='127.0.0.1',
        database='mysql_high',
        # unix_socket=None,
        port=3306,
        autocommit=True  # 关闭事务,pymysql事务默认开启,设置为Ture表示关闭事务
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

username = input('用户名:')
password = input('密码:')

# 在用户表中, 判断用户名和密码是否正确
sql = f"select * from tb_user where username='{username}' and password='{password}'"
# select * from tb_user where username='' or 1=1 #' and password='111'
print(sql)
cursor.execute(sql)
res = cursor.fetchall()
print(res)
