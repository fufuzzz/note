#### 习题一:

有如下表和数据,查出num>=20 and num<=39的数字,并且,把num值处于[20,29]之间,显示为20。num值处于[30,39]之间的,显示30。（提示：使用floor函数，向下取整）

```sql
mian表
+------+
| num  |
+------+
|    3 |
|   12 |
|   15 |
|   25 |
|   23 |
|   29 |
|   34 |
|   37 |
|   32 |
|   45 |
|   48 |
|   52 |
+------+
```

导入数据

```sql
create table mian 
( 
	num int
)
insert into mian values 
(3),
(12),
(15),
(25),
(23),
(29),
(34),
(37),
(32);
```





#### 习题二：

有如下表及数据

```sql
+------+---------+-------+
| name | subject | score |
+------+---------+-------+
| 张三 | 数学    |    90 |
| 张三 | 语文    |    50 |
| 张三 | 地理    |    40 |
| 李四 | 语文    |    55 |
| 李四 | 政治    |    45 |
| 王五 | 政治    |    30 |
+------+---------+-------+
```

要求：查询出2门及2门以上不及格者的平均成绩



导入数据

```sql
CREATE TABLE `stu` (
  `name` varchar(20) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `score` tinyint(4) DEFAULT NULL
)CHARSET=utf8;


insert into stu
values
('张三','数学',90),
('张三','语文',50),
('张三','地理',40),
('李四','语文',55),
('李四','政治',45),
('王五','政治',30);
```







#### 习题三：

创建如下的两张表

```sql
mysql> select * from m;
+-----+------+------+------+------------+
| mid | hid  | gid  | mres | matime     |
+-----+------+------+------+------------+
|   1 |    1 |    2 | 2:0  | 2006-05-21 |
|   2 |    2 |    3 | 1:2  | 2006-06-21 |
|   3 |    3 |    1 | 2:5  | 2006-06-25 |
|   4 |    2 |    1 | 3:2  | 2006-07-21 |
+-----+------+------+------+------------+
4 rows in set (0.00 sec)

mysql> select * from t;
+------+----------+
| tid  | tname    |
+------+----------+
|    1 | 国安     |
|    2 | 申花     |
|    3 | 公益联队 |
+------+----------+
```

导入数据

```python
create table m(
     mid int, # 主键
     hid int, # 主队的ID
     gid int, # 客队的ID
     mres varchar(10), # 比赛结果，如（2:0）
     matime date  # 比赛开始时间
)charset utf8;

create table t (
     tid int, # 主键
     tname varchar(20)  # 队伍名称
)charset utf8;



insert into m
     values
     (1,1,2,'2:0','2006-05-21'),
     (2,2,3,'1:2','2006-06-21'),
     (3,3,1,'2:5','2006-06-25'),
     (4,2,1,'3:2','2006-07-21');

 
insert into t
     values
     (1,'国安'),
     (2,'申花'),
     (3,'布尔联队');
```

创建查询语句，使结果返回如下所示：

```sql
+------+----------+------+------+----------+------------+
| hid  | hname    | mres | gid  | gname    | matime     |
+------+----------+------+------+----------+------------+
|    1 | 国安     | 2:0  |    2 | 申花      | 2006-05-21 |
|    2 | 申花     | 1:2  |    3 | 公益联队   | 2006-06-21 |
|    3 | 公益联队  | 2:5  |    1 | 国安      | 2006-06-25 |
|    2 | 申花     | 3:2  |    1 | 国安      | 2006-07-21 |
+------+----------+------+------+----------+------------+
```





#### 习题四：

创建如下两张表

```sql
A表:
+------+------+
| id   | num  |
+------+------+
| a    |    5 |
| b    |   10 |
| c    |   15 |
| d    |   10 |
+------+------+

B表:
+------+------+
| id   | num  |
+------+------+
| b    |    5 |
| c    |   15 |
| d    |   20 |
| e    |   99 |
+------+------+
```

导入数据

```sql
create table a (
id char(1),
num int
)charset utf8;

insert into a values ('a',5),('b',10),('c',15),('d',10);

create table b (
id char(1),
num int
)charset utf8;

insert into b values ('b',5),('c',15),('d',20),('e',99);
```

创建查询语句，使结果如下所示（相同字段，num相加）

```sql
+------+----------+
| id   |    num   |
+------+----------+
| a    |        5 |
| b    |       15 |
| c    |       30 |
| d    |       30 |
| e    |       99 |
+------+----------+
```

