import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='201314', database='mydb3', charset='utf8')
cursor = conn.cursor()

sql = 'insert into person(id, name, age) values (5, "关羽", 33)'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()  # 插入数据
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()
