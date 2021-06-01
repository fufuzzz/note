import pymysql
import re
# 主服务器连接

conn1 = pymysql.connect(
    user='root',
    passwd='123456',
    host='121.5.165.79',
    database='demo',
    port=3307,
)

cursor1 = conn1.cursor()

# 从服务器连接

conn2 = pymysql.connect(
    user='root',
    passwd='123456',
    host='121.5.165.79',
    database='demo',
    port=3308,
)

cursor2 = conn2.cursor()

def get_conn_cursor(sql):
    if re.match(r'select', sql.strip(), re.I):
        return conn2, cursor2
    else:
        return conn1, cursor1




# sql = "insert into user values (%s, %s)"
# new_conn, new_cursor = get_conn_cursor(sql)
# val = (None, 'ccccc')
# new_cursor.execute(sql, val)
# new_conn.commit()

sql2 = "select * from user"
new_conn, new_cursor = get_conn_cursor(sql2)
new_cursor.execute(sql2)
print(new_cursor.fetchall())
