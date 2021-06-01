import pymysql

db = pymysql.connect(user='root', passwd='201314', database='mydb3')

with db.cursor() as cur:
    # 删除操作
    sql = 'delete from person where id>=13'
    res = cur.execute(sql)
    if res:
        print('删除成功')
    else:
        print('删除失败')
    # 提交
    db.commit()

db.close()
