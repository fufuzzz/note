import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='201314', database='mydb3', charset='utf8')

cursor = conn.cursor()

# 删除数据
sql = 'delete from person where id=5'

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

cursor.close()
conn.close()