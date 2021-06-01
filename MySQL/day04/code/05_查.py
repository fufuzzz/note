import pymysql

db = pymysql.connect(user='root', passwd='201314', database='mydb3')

with db.cursor() as cur:
    # 执行查询操作
    cur.execute('select * from person')

    # 获取数据
    # fetchall(): 获取所有数据
    # print(cur.fetchall())

    # fetchone(): 获取一条数据
    # print(cur.fetchone())
    # print(cur.fetchone())

    # fetchmany(3): 一次获取3条
    # print(cur.fetchmany(3))
    # print(cur.fetchmany(3))
    # print(cur.fetchmany(3))
    # print(cur.fetchmany(3))
    # print(cur.fetchmany(3))  # ()没有数据了

    while True:
        result = cur.fetchmany(3)
        print(result,type(result))
        if not result:
            break

    print('查询完成')

db.close()