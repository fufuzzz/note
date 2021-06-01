import pymysql

db = pymysql.connect(user='root', passwd='201314', database='mydb3')

with db.cursor() as cur:
    # 修改操作
    sql = 'update person set age=30 where name like "曹%"'
    cur.execute(sql)

    db.commit()


db.close()