import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='201314', database='mydb3', charset='utf8')

cursor = conn.cursor()

sql = 'select * from person'
cursor.execute(sql)

# fetchone(): 每次查询下一条数据
# res = cursor.fetchone()
# print(res)
# res = cursor.fetchone()
# print(res)

# fetchall() : 所有数据
res = cursor.fetchall()
print(res)
# res = cursor.fetchmany(3)  # 前3条数据
# print(res)
for row in res:
    print(row)

print(cursor.rowcount)  # 总的数据条数

cursor.close()
conn.close()