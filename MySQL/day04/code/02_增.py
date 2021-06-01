import pymysql

db = pymysql.connect(user='root', passwd='201314', database='mydb3')

# cur = db.cursor()

try:
    with db.cursor() as cur:
        # 插入一条语句
        # sql = 'insert into person values (7,"曹操",40)'
        # cur.execute(sql)

        # 插入多条数据
        for i in range(1,2):
            id = int(input('输入id'))
            name = input('输入姓名')
            age = int(input('输入年龄'))
            # sql = f'insert into person values ({id},"{name}",{age})'
            sql = 'insert into person values(%d,"%s",%d)' % (id, name, age)
            cur.execute(sql)
        # 提交
        db.commit()
except:
    db.rollback()
finally:
    db.close()
