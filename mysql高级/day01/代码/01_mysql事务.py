# 流程
# 接收到要买的商品信息
# 先 生产总订单
# 循环买的商品, 判断每件商品买的库存够不够
# 如果库存不足,中断执行代码, 提示用户当前商品库存不足
# 库存足,减库存加销量
# 生成子订单

import datetime
import pymysql
conn = pymysql.connect(
        user='root',
        password="201314",
        host='127.0.0.1',
        database='mysql_high',
        unix_socket=None,
        port=3306,
        # autocommit=True  # 关闭事务,pymysql事务默认开启,设置为Ture表示关闭事务
)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 用字典表示, 买了哪些商品
# data = {'商品id': '商品数量'}
data = {'1': 1, '2': 1}
uid = 1
# 把数据插入到总订单列表中
# sql注入
sql = "insert into tb_order values (%s, %s, %s, %s, %s, %s)"


# 订单号采用当前日期格式 20210412095650 +uid
order_code = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(uid)

val = (None, uid, order_code, sum(data.values()), 0, 1)

cursor.execute(sql, val)
# 获取新增数据的自增id
auto_id = cursor.lastrowid

# 循环商品
totalPrice = 0
for gid, num in data.items():
    # 通过商品id获取当前商品的库存
    sql = "select * from tb_goods where id =%s"
    val = (gid,)
    cursor.execute(sql, val)
    res = cursor.fetchone()
    # print(res['store'],type(res['store']))
    # print()
    # 判断库存够不够
    if res['store'] < num:
        print('库存不足')
        # 回滚事务
        conn.rollback()
        exit()  # 中断代码执行

    # 库存足, 减库存加销量
    sql = "update tb_goods set store=store-%s, num=num+%s where id = %s"
    val = (num, num, gid)
    cursor.execute(sql, val)

    # 生成子订单
    sql = "insert into tb_order_detail values (%s, %s, %s, %s, %s, %s)"
    val = (None, uid, order_code, gid, num, res['price'])
    cursor.execute(sql, val)

    totalPrice += res['price'] * num

# 把循环计算的总金额赋值给之前增加的总订单的总金额
sql = "update tb_order set total_price = %s where id= %s"
val = (totalPrice, auto_id)
cursor.execute(sql, val)
# 执行事务
conn.commit()

# 关闭游标和数据库句柄
cursor.close()
conn.close()