# Day04-Python操作MySQL

#### 1.连接MySQL

```python
import pymysql

# 连接mysql
# 参数1：表示主机或ip地址
# 参数2：表示mysql的用户名
# 参数3：表示mysql的密码
# 参数4：表示mysql的数据库名
# conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
conn = pymysql.connect('10.36.132.6', 'root', 'root', 'mydb2')
# 创建游标对象: 可以执行sql语句
cursor = conn.cursor()

# sql语句
sql = 'select version()'

# 执行sql语句
cursor.execute(sql)

res = cursor.fetchone()
print(res)

# 关闭游标对象
cursor.close()
# 关闭mysql的连接
conn.close()

```

#### 2.插入数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
cursor = conn.cursor()

# 插入数据
sql = 'insert into person(name, age) values("aa", 20)'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()

```

#### 3. 删除数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
cursor = conn.cursor()

# 删除数据
sql = 'delete from person where id=18'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()

```

#### 4. 更新数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2')
cursor = conn.cursor()

# 更新数据
sql = 'update person set age=30 where id=20'

try:
    cursor.execute(sql)
    # 提交事务
    conn.commit()
except:
    # 回滚
    conn.rollback()

cursor.close()
conn.close()

```

#### 5.查询数据

```python
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'mydb2', charset='utf8')
cursor = conn.cursor()

# 查询数据
sql = 'select * from person'
# 执行sql
cursor.execute(sql)

# fetchone() : 每次查询下一条数据
# res = cursor.fetchone()
# print(res)
# res = cursor.fetchone()
# print(res)
# res = cursor.fetchone()
# print(res)

# fetchall() : 所有数据
res = cursor.fetchall()
# res = cursor.fetchmany(3)  # 前3条数据
for row in res:
    print(row)

print(cursor.rowcount)  # 总的数据条数

cursor.close()
conn.close()
```

 

### 练习: 使用Python操作MySQL数据库

#### 1. 创建表格, 并添加数据

```sql
create table tb_dept
(
	dno   int not null comment '编号',
	dname varchar(10) not null comment '名称',
	dloc  varchar(20) not null comment '所在地',
	primary key (dno)
);

insert into tb_dept values 
	(10, '会计部', '北京'),
	(20, '研发部', '成都'),
	(30, '销售部', '重庆'),
	(40, '运维部', '深圳');

create table tb_emp
(
	eno   int not null comment '员工编号',
	ename varchar(20) not null comment '员工姓名',
	job   varchar(20) not null comment '员工职位',
	mgr   int comment '主管编号',
	sal   int not null comment '员工月薪',
	comm  int comment '每月补贴',
	dno   int comment '所在部门编号',
	primary key (eno)
);

alter table tb_emp add constraint fk_emp_dno foreign key (dno) references tb_dept (dno);

insert into tb_emp values 
	(7800, '张三丰', '总裁', null, 9000, 1200, 20),
	(2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
	(3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
	(3211, '张无忌', '程序员', 2056, 3200, null, 20),
	(3233, '丘处机', '程序员', 2056, 3400, null, 20),
	(3251, '张翠山', '程序员', 2056, 4000, null, 20),
	(5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
	(5234, '郭靖', '出纳', 5566, 2000, null, 10),
	(3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
	(1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
	(4466, '苗人凤', '销售员', 3344, 2500, null, 30),
	(3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
	(3577, '杨过', '会计', 5566, 2200, null, 10),
	(3588, '朱九真', '会计', 5566, 2500, null, 10);

```

#### 2. 添加一个部门

```python
import pymysql

def main():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (no, name, loc)
            )
        if result == 1:
            print('添加成功!')
        # 4. 操作成功提交事务
        con.commit()
    except:
    	# 回滚
    	conn.rollback()

    finally:
        # 5. 关闭连接释放资源
        con.close()

if __name__ == '__main__':
    main()
```

#### 3. 删除一个部门

```python
import pymysql

def main():
    no = int(input('编号: '))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no, )
            )
        if result == 1:
            print('删除成功!')
    finally:
        con.close()

if __name__ == '__main__':
    main()
```

> 说明：如果不希望每次SQL操作之后手动提交或回滚事务，可以像上面的代码那样，在创建连接的时候多加一个名为autocommit的参数并将它的值设置为True，表示每次执行SQL之后自动提交。如果程序中不需要使用事务环境也不希望手动的提交或回滚就可以这么做。

#### 4. 更新一个部门

```python
import pymysql

def main():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'update tb_dept set dname=%s, dloc=%s where dno=%s',
                (name, loc, no)
            )
        if result == 1:
            print('更新成功!')
    finally:
        con.close()

if __name__ == '__main__':
    main()
```

#### 5. 查询所有部门

```python
import pymysql
from pymysql.cursors import DictCursor

def main():
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()

if __name__ == '__main__':
    main()
```

#### 6. 分页查询员工信息

```python
class Emp(object):

    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'


def main():
    page = int(input('页码: '))
    size = int(input('大小: '))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='yourname', password='yourpass')
    try:
        with con.cursor() as cursor:
            cursor.execute(
                'select eno, ename, job, sal from tb_emp limit %s,%s',
                ((page - 1) * size, size)
            )
            results = cursor.fetchall()
            for emp_tuple in results:
                emp = Emp(*emp_tuple)
                print(emp)
    finally:
        con.close()

if __name__ == '__main__':
    main()
```





