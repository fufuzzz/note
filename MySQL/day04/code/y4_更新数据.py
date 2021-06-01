import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='201314', database='mydb3', charset='utf8')

cursor = conn.cursor()

sql = 'update person set age=105 where id=4'

try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

cursor.close()
conn.close()
