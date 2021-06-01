from QFSQL import QFSQL
import random
import time

# 插入数据
def insert_data():
    qf_sql = QFSQL(password='201314', database='mydb5')

    for i in range(100001, 500001):
        name1 = f'ElonMask-{i}'
        name2 = name1
        age = random.randint(1, 100)
        sex = random.choice(['男', '女', '其他'])
        # sql
        sql = f'insert into person (name1, name2, age, sex)'\
              f'values ("{name1}", "{name2}", "{age}", "{sex}")'
        # 执行插入操作
        qf_sql.insert(sql)

    print('插入完成!')

# 查询数据
def query_data():
    qf_sql = QFSQL(password='201314', database='mydb5')

    sql1 = 'select * from person where name1="ElonMask-500000"'
    sql2 = 'select * from person where name2="ElonMask-500000"'

    # 统计时间
    start = time.time()

    # result = qf_sql.search(sql1)  # 所需检索时间: 0.2672615051269531
    result = qf_sql.search(sql2)  # 所需检索时间: 0.002027273178100586
    print(result)

    end = time.time()
    print('所需检索时间:', end-start)


if __name__ == '__main__':
    # insert_data()
    query_data()