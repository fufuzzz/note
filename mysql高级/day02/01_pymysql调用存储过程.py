import pymysql

conn = pymysql.connect(
    user='root',
    passwd='201314',
    host='127.0.0.1',
    database='mysql_high',
    port=3306
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "call pro_test5"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
cursor.close()
conn.close()
