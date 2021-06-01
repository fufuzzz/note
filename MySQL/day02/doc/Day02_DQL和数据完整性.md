# Day02-DQL和数据完整性

### 一、DQL

> 数据库执行DQL语言不会对数据库中的数据发生任何改变，而是让数据库发送查询结果到客户端
>
> 查询返回的结果其实是一张虚拟表
>
> 语法：
>
> ```mysql
> SELECT 列名 FROM 表名【WHERE --> GROUP BY -->HAVING--> ORDER BY】
> ```

##### 1 基础查询

> 演示：
>
> ```mysql
> #1.查询所有列
> mysql> select * from student;
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 1    | aaaa     |   19 | female |
> | 2    | bbbbbbbb |   20 | male   |
> | 3    | cc       |   15 | male   |
> | 4    | ddd      |   16 | female |
> | 5    | eee      |   20 | female |
> +------+----------+------+--------+
> 5 rows in set (0.00 sec)
>
>
> #2.查询指定列
> mysql> select id,name,gender from student;
> +------+----------+--------+
> | id   | name     | gender |
> +------+----------+--------+
> | 1    | aaaa     | female |
> | 2    | bbbbbbbb | male   |
> | 3    | cc       | male   |
> | 4    | ddd      | female |
> | 5    | eee      | female |
> +------+----------+--------+
> 5 rows in set (0.00 sec)
> ```

##### 2 条件查询

> 主要结合where的使用
>
> between...and: 介于..和..之间
>
> and：逻辑与
>
> or：逻辑或
>
> in / not in：类似于Python中的成员运算符
>
> is / is not: 类似于Python中的身份运算符 , 常用语判断null值， 如：name is null
>
> 演示：
>
> ```mysql
> #1.查询性别为女，并且年龄为20的记录
> mysql> select * from student where gender='female' and age=20;
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 5    | eee  |   20 | female |
> +------+------+------+--------+
> 1 row in set (0.00 sec)
>
> #2.查询编号为1或者姓名为ddd的记录
> mysql> select * from student where id='1' or name='ddd';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 1    | aaaa |   19 | female |
> | 4    | ddd  |   16 | female |
> +------+------+------+--------+
> 2 rows in set (0.00 sec)
>
> #3.查询编号分别为1,2,3的记录
> mysql> select * from student where id='1' or id='2' or id='3';
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 1    | aaaa     |   19 | female |
> | 2    | bbbbbbbb |   20 | male   |
> | 3    | cc       |   15 | male   |
> +------+----------+------+--------+
> 3 rows in set (0.00 sec)
> #简写形式
> mysql> select * from student where id in('1','2','3');
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 1    | aaaa     |   19 | female |
> | 2    | bbbbbbbb |   20 | male   |
> | 3    | cc       |   15 | male   |
> +------+----------+------+--------+
> 3 rows in set (0.00 sec)
>
> #4.查询编号不为1,2,3的记录
> mysql> select * from student where id not in('1','2','3');
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 4    | ddd  |   16 | female |
> | 5    | eee  |   20 | female |
> +------+------+------+--------+
> 2 rows in set (0.00 sec)
>
>
> #5.查询年龄为null的记录
> mysql> select * from student where age is null;
> Empty set (0.00 sec)
>
> #6.查询年龄在15~20之间的记录
> mysql> select * from student where age>=15 and age<=20;
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 1    | aaaa     |   19 | female |
> | 2    | bbbbbbbb |   20 | male   |
> | 3    | cc       |   15 | male   |
> | 4    | ddd      |   16 | female |
> | 5    | eee      |   20 | female |
> +------+----------+------+--------+
> 5 rows in set (0.00 sec)
> #简写形式
> mysql> select * from student where age between 15 and 20;
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 1    | aaaa     |   19 | female |
> | 2    | bbbbbbbb |   20 | male   |
> | 3    | cc       |   15 | male   |
> | 4    | ddd      |   16 | female |
> | 5    | eee      |   20 | female |
> +------+----------+------+--------+
> 5 rows in set (0.00 sec)
>
> #7.查询性别非男的记录
> #方式一
> mysql> select * from student where gender='female';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 1    | aaaa |   19 | female |
> | 4    | ddd  |   16 | female |
> | 5    | eee  |   20 | female |
> +------+------+------+--------+
> 3 rows in set (0.00 sec)
> #方式二
> mysql> select * from student where gender!='male';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 1    | aaaa |   19 | female |
> | 4    | ddd  |   16 | female |
> | 5    | eee  |   20 | female |
> +------+------+------+--------+
> 3 rows in set (0.00 sec)
> #方式三
> mysql> select * from student where gender<>'male';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 1    | aaaa |   19 | female |
> | 4    | ddd  |   16 | female |
> | 5    | eee  |   20 | female |
> +------+------+------+--------+
> 3 rows in set (0.00 sec)
> ```

##### 3. 模糊查询

> where 子句中=表示精准查询
>
> like：一般情况下结合where子句使用
>
> 通配符：
>
> ​	_ : 匹配任意一个字符
>
> ​	%：匹配0~n个字符【n大于等于1】
>
> 演示：
>
> ```mysql
> #1.查询姓名由4个字符组成的记录
> mysql> select * from student where name like '____';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 1    | aaaa |   19 | female |
> +------+------+------+--------+
> 1 row in set (0.00 sec)
>
> #2.查询姓名由3个字符组成的记录，并且最后一个字母为c的记录
> mysql> select * from student where name like '__c';
> Empty set (0.00 sec)
>
> #3.查询以a开头的记录
> mysql> select * from student where name like 'a%';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 1    | aaaa |   19 | female |
> +------+------+------+--------+
> 1 row in set (0.01 sec)
>
> #4.查询姓名中包含b的记录
> mysql> select * from student where name like '%b%';
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 2    | bbbbbbbb |   20 | male   |
> +------+----------+------+--------+
> 1 row in set (0.00 sec)
>
> #5.查询姓名中第2个字母为c的记录
> mysql> select * from student where name like '_c%';
> +------+------+------+--------+
> | id   | name | age  | gender |
> +------+------+------+--------+
> | 3    | cc   |   15 | male   |
> +------+------+------+--------+
> 1 row in set (0.00 sec)
> ```

##### 4. 字段控制查询

> as:  起别名，用法 ：select 字段 as 别名
>
> distinct: 去除重复记录
>
> 演示；
>
> ```mysql
> #1.去除重复记录
> mysql> select id from student;
> +------+
> | id   |
> +------+
> | 1    |
> | 2    |
> | 3    |
> | 4    |
> | 5    |
> | 1    |
> +------+
> 6 rows in set (0.00 sec)
>
> mysql> select distinct id from student;
> +------+
> | id   |
> +------+
> | 1    |
> | 2    |
> | 3    |
> | 4    |
> | 5    |
> +------+
> 5 rows in set (0.01 sec)
>
> #2.给列名起别名
> mysql> select name,gender  from student;
> +----------+--------+
> | name     | gender |
> +----------+--------+
> | aaaa     | female |
> | bbbbbbbb | male   |
> | cc       | male   |
> | ddd      | female |
> | eee      | female |
> | ffff     | male   |
> +----------+--------+
> 6 rows in set (0.00 sec)
>
>
> mysql> select name as 姓名,gender as 性别  from student;
> +----------+--------+
> | 姓名     | 性别   |
> +----------+--------+
> | aaaa     | female |
> | bbbbbbbb | male   |
> | cc       | male   |
> | ddd      | female |
> | eee      | female |
> | ffff     | male   |
> +----------+--------+
> 6 rows in set (0.00 sec)
>
> mysql> select name  姓名1,gender  性别1  from student;
> +----------+---------+
> | 姓名1    | 性别1   |
> +----------+---------+
> | aaaa     | female  |
> | bbbbbbbb | male    |
> | cc       | male    |
> | ddd      | female  |
> | eee      | female  |
> | ffff     | male    |
> +----------+---------+
> 6 rows in set (0.00 sec)
> ```

##### 5. 排序

> order by: 指定数据返回的顺序
>
> ​	asc：ascending,升序
>
> ​	desc:  descending，降序
>
> 用法：select from  表 order by  xxx
>
> 演示：
>
> ```mysql
> #1.查询所有的记录，按照年龄升序排序
> mysql> select * from student order by age asc;
> +------+----------+------+--------+
> | id   | name     | age  | gender |
> +------+----------+------+--------+
> | 3    | cc       |   15 | male   |
> | 4    | ddd      |   16 | female |
> | 1    | aaaa     |   19 | female |
> | 2    | bbbbbbbb |   20 | male   |
> | 5    | eee      |   20 | female |
> | 1    | ffff     |   30 | male   |
> +------+----------+------+--------+
> 6 rows in set (0.00 sec)
>
> #2.查询所有学生记录，按照年龄降序排序，如果年龄相等，则按照编号进行升序排序 
> mysql> select * from student order by age desc,id asc; 
> +------+----------+------+--------+ 
> | id   | name     | age  | gender | 
> +------+----------+------+--------+ 
> | 1    | ffff     |   30 | male   | 
> | 2    | bbbbbbbb |   20 | male   | 
> | 5    | eee      |   20 | female | 
> | 1    | aaaa     |   19 | female | 
> | 4    | ddd      |   16 | female | 
> | 3    | cc       |   15 | male   | 
> +------+----------+------+--------+ 
> 6 rows in set (0.00 sec) 
> ```

##### 6 聚合函数 

> 聚合函数主要用来做纵向运算 
>
> count(): 统计指定列不为null的记录行数
>
> ```mysql
> #1.查询年龄大于20的人数
> mysql> select count(*)  from student where age>20;
> +----------+
> | count(*) |
> +----------+
> |        1 |
> +----------+
> 1 row in set (0.00 sec)
>
> ```
>
> sum():计算指定列的数值和
>
> ```mysql
> #1.查询所有学生的年龄和
> mysql> select sum(age) from student;
> +----------+
> | sum(age) |
> +----------+
> |      120 |
> +----------+
> 1 row in set (0.01 sec)
>
> #2.查询所有学生的年龄和，以及所有学生的编号和
> mysql> select sum(age),sum(id) from student;
> +----------+---------+
> | sum(age) | sum(id) |
> +----------+---------+
> |      120 |      16 |
> +----------+---------+
> 1 row in set (0.00 sec)
> ```
>
> 求指定列中的最大值和最小值
>
> max():
>
> min():
>
> ```mysql
> #求最大年龄和最小年龄
> mysql> select max(age),min(age) from student;
> +----------+----------+
> | max(age) | min(age) |
> +----------+----------+
> |       30 |       15 |
> +----------+----------+
> 1 row in set (0.00 sec)
> ```
>
> avg()
>
> average:平均数，
>
> ```
> #查询所有学生的平均年龄
> mysql> select avg(age) from student;
> +----------+
> | avg(age) |
> +----------+
> |  20.0000 |
> +----------+
> 1 row in set (0.00 sec)
> ```
>
> 总结：
>
> 查询关键字的书写顺序：select 聚合函数  from where order by

##### 7.分组查询

> group by：分组查询
>
> having：有...,表示条件，类似于where的用法
>
> 演示：
>
> ```mysql
> #在当前数据库下创建新的表
> mysql> create table emp(			
>  -> empno int primary key,
>  -> enname varchar(20),
>  -> job varchar(20),
>  -> mgr int,
>  -> hiredate date,
>  -> sal double,
>  -> comm double,
>  -> deptno int
>  -> );
>
> #1.查询各个部门的人数
> mysql> select count(*) from emp group by deptno;
> +----------+
> | count(*) |
> +----------+
> |        2 |
> |        2 |
> |        4 |
> +----------+
> 3 rows in set (0.00 sec)
>
> #2.查询每个部门的部门编号和每个部门的工资和
> mysql> select deptno,sum(sal) from emp group by deptno;
> +--------+----------+
> | deptno | sum(sal) |
> +--------+----------+
> |     10 |  7450.00 |
> |     20 |  3800.00 |
> |     30 |  8675.00 |
> +--------+----------+
> 3 rows in set (0.00 sec)
>
>
> #3.查询每个部门的部门编号和每个部门的人数
> mysql> select deptno,count(*) from emp group by deptno;
> +--------+----------+
> | deptno | count(*) |
> +--------+----------+
> |     10 |        2 |
> |     20 |        2 |
> |     30 |        4 |
> +--------+----------+
> 3 rows in set (0.00 sec)
>
>
> #4.查询每个部门的部门编号和每个部门工资大于1500的人数
> mysql> select deptno,count(*) from emp where sal>1500 group by deptno;
> +--------+----------+
> | deptno | count(*) |
> +--------+----------+
> |     10 |        2 |
> |     20 |        1 |
> |     30 |        3 |
> +--------+----------+
> 3 rows in set (0.01 sec)
>
>
> #5.查询工资总和大于7000的部门编号以及工资和
> mysql> select deptno,sum(sal) from emp group by deptno having sum(sal)>7000;
> +--------+----------+
> | deptno | sum(sal) |
> +--------+----------+
> |     10 |  7450.00 |
> |     30 |  8675.00 |
> +--------+----------+
> 2 rows in set (0.00 sec)
> ```
>
> 总结：
>
> ​	having和where的区别
>
> ​	a.二者都表示对数据执行条件
>
> ​	b. having是在分组之后对数据进行过滤
>
> ​	    where是在分组之前对数据进行过滤
>
> ​	c.  having后面可以使用聚合函数
>
> ​            where后面不可以使用聚合函数
>
> 演示：
>
> ```mysql
> #查询工资大于1500，工资总和大于6000的部门编号和工资和
> mysql> select deptno,sum(sal) from emp where sal>1500 group by deptno having sum(sal)>6000;
> +--------+----------+
> | deptno | sum(sal) |
> +--------+----------+
> |     10 |  7450.00 |
> |     30 |  7425.00 |
> +--------+----------+
> 2 rows in set (0.00 sec)
> ```

##### 8 分页查询

> limit：用来限定查询的起始行，以及总行数
>
> 演示：
>
> ```mysql
> #1.查询4行记录，起始行从0开始
> mysql> select * from emp limit 0,4;
> +-------+--------+----------+------+------------+---------+---------+--------+
> | empno | enname | job      | mgr  | hiredate   | sal     | comm    | deptno |
> +-------+--------+----------+------+------------+---------+---------+--------+
> |  7369 | smith  | clark    | 7902 | 1980-12-17 |  800.00 |    NULL |     20 |
> |  7499 | allen  | salesman | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
> |  7566 | jones  | managen  | 7839 | 1981-04-02 | 2975.00 |    NULL |     30 |
> |  7654 | martin | salesman | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
> +-------+--------+----------+------+------------+---------+---------+--------+
> 4 rows in set (0.00 sec)
>
> mysql> select * from emp limit 2,3;
> +-------+--------+----------+------+------------+---------+---------+--------+
> | empno | enname | job      | mgr  | hiredate   | sal     | comm    | deptno |
> +-------+--------+----------+------+------------+---------+---------+--------+
> |  7566 | jones  | managen  | 7839 | 1981-04-02 | 2975.00 |    NULL |     30 |
> |  7654 | martin | salesman | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
> |  7698 | blake  | manager  | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
> +-------+--------+----------+------+------------+---------+---------+--------+
> 3 rows in set (0.01 sec)
> ```
>
> 总结：
>
> `mysql> select deptno,sum(sal) from emp where sal>1500  group by deptno having sum(sal)>5000 order by sum(sal) asc limit 4; `
>
> ​	查询语句书写顺序：select----》from---》where---》group by-----》having-----》order by----->limit
>
> ​	查询语句执行顺序：from----》where-----》group by----》having----》order by ----》select-----》limit



### 二、数据的完整性

> 作用：保证用户输入的数据保存到数据库中是正确的
>
> 实质：创建表的时候给表中的字段添加约束

#### 1. 实体完整性

> 实体：表中的一行或者一条记录代表一个实体
>
> 实体完整性的作用：标识每一行数据不重复
>
> 约束类型：
>
> ​	主键约束【primary key】
>
> ​	唯一约束【unique】
>
> ​	自动增长列【auto_increment】

##### 1.1主键约束【primary key】

> 特点：数据唯一，且不能为null
>
> 主关键字可以是表中的一个字段或者多个字段，它的值用来唯一标识表中的某一条记录
>
> 场景：在多个表的关联关系中
>
> 演示：
>
> ```mysql
> mysql> create table stu1(
>     	-> 		id int primary key,
>     	-> 		name varchar(50) 
>     	-> );
>
> mysql> create table stu2(
>  	    -> 		id int ,
>     	-> 		name varchar(50),
>     	-> 		primary key(id，name)
>     	-> );
>    
> mysql> create table stu3(
> 		-> 		id int,
>  		-> 		name varchar(50),
>     	-> );
>    mysql> alter table stu3 add constraint stu3_id primary key(id);
>    
> ```

##### 1.2唯一约束

> 作用：在非主键列中不能输入重复的值
>
> 演示：
>
> ```mysql
> mysql> create table stu4(
>     -> 		id int primary key,
>     -> 		name varchar(50) unique
>     -> );
>
>
> # primary key和unique之间的区别
> a.二者都强调的是唯一性
> b.在同一个表中，一般只出现一个primary key，可以出现多个unique
> c.primary key不允许为null，但是unique是允许的
> ```

##### 1.3自动增长列

> 给主键添加添加自动增长性，列只能是整数类型
>
> 场景：一般添加给主键
>
> 演示：
>
> ```mysql
> mysql> create table stu5(
>     -> id int primary key auto_increment,
>     -> name varchar(50) unique
>     -> );
>
> ```

#### 2.域完整性

> 作用：限制单元格数据的正确性，
>
> ​	    域代表当前单元格
>
> 约束类型：
>
> ​	数据类型
>
> ​	非空约束【not null】
>
> ​	默认值约束【default】	

##### 2.1数据类型

> 数字类型：int  float  double 
>
> 日期类型：date datetime
>
> 字符串类型：varchar(20)

##### 2.2非空约束【not null】

> 演示：
>
> ```mysql
> mysql> create table stu6( 
>     	id int primary key auto_increment, 
>     	name varchar(50) unique not null,
>     );
>
> #注意：name被约束为not null，插入数据的时候，name坚决不能为null，如果为null，数据库立马报错
> ```

##### 2.3默认值约束

> 演示：
>
> ```mysql
> mysql> create table stu7(
>     -> id int primary key auto_increment,
>     -> name varchar(50) unique not null,
>     -> address varchar(50) default "beijing"
>     -> );
>
> mysql> insert into stu7 (id,name,address) values(1,'aaa','fff');
> mysql> insert into stu7 (id,name,address) values(2,'bbb',default);
>
> mysql> select * from stu7;
> +----+------+---------+
> | id | name | address |
> +----+------+---------+
> |  1 | aaa  | fff     |
> |  2 | bbb  | beijing |
> +----+------+---------+
>
> ```

#### 3.外键约束

> 添加外键约束：foreign key 
>
> 注意：添加外键必须先有主键，主键和外键的类型必须保持一致
>
> 举例：学生表，成绩表
>
> 作用：将两个甚至多个表产生联系
>
> 演示：
>
> ```mysql
> #创建表
> #学生表
> mysql> create table student(
>     	-> 		stuid varchar(10) primary key,
>     	-> 		stuname varchar(50)
>     	-> );
>
> #成绩表
> mysql> create table score(
>  	-> 		stuid varchar(10),
>     	-> 		score int,
>     	-> 		courseid int
>     	-> );
>    
> #插入数据
> insert into student values('1001','zhangsan');
> insert into student values('1002','xiaoming');
> insert into student values('1003','jack');
> insert into student values('1004','tom');
>
> insert into score values('1001',98,1);
> insert into score values('1002',95,1);
> insert into score values('1003',67,2);
> insert into score values('1004',83,2);
> insert into score values('1004',70,1);
>
> #查询
> mysql> select * from student;
> +-------+----------+
> | stuid | stuname  | 
> +-------+----------+
> | 1001  | zhangsan |
> | 1002  | lisi     |
> | 1003  | jack     |
> | 1004  | tom      |
> +-------+----------+
>
> mysql> select * from score;
> +-------+-------+----------+
> | stuid | score | courseid | 
> +-------+-------+----------+
> | 1001  |    98 |        1 |
> | 1002  |    80 |        2 |
> | 1003  |    70 |        1 |
> | 1004  |    60 |        2 |
> | 1002  |    75 |        3 |
> +-------+-------+----------+
>
>
> #方式一
> mysql> create table score1( score int, courseid int,stuid varchar(10), constraint stu_sco_id foreign key(stuid) references student(stuid) );
> #注意：stu_sco_id是给约束起的名字，可以自定义
>
> #方式二
> mysql> create table score2(
>  	-> 		score int,
>  	-> 		courseid int,
> 	-> 		stuid varchar(10)
>  	-> );
>
>    mysql> alter table score2 add constraint stu_sco_id2 foreign key(stuid) references student(stuid);
>    
>    #注意：主键和外键的类型必须保持一致
> ```



