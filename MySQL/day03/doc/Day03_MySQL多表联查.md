# Day03-MySQL多表联查

### 一、多表查询

#### 1.表与表之间的关系

> 一对一
>
> ​	通过嵌套的方式
>
> 一对多【多对一】
>
> ​	添加外键
>
> 多对多
>
> ​	单独创建一张新的表

#### 2.合并结果集

> 作用：将两个select语句的查询结果合并到一起
>
> 两种方式：
>
> ​	union：去除重复记录【并集】
>
> ​	union all；获取所有的结果
>
> 演示：
>
> ```mysql
> #创建表
> mysql> create table A(
>     	 name varchar(10),
>    	 	 score int
>       );
>
> mysql> create table B( 
>   		name varchar(10), 
>   		score int 
> 	  );
>
> #批量插入数据
> mysql> insert into A values('a',10),('b',20),('c',30);
> mysql> insert into B values('a',10),('d',40),('c',30);
>
> #查询结果
> mysql> select * from A;
> +------+-------+
> | name | score |
> +------+-------+
> | a    |    10 |
> | b    |    20 |
> | c    |    30 |
> +------+-------+
>
> mysql> select * from B;
> +------+-------+
> | name | score |
> +------+-------+
> | a    |    10 |
> | d    |    40 |
> | c    |    30 |
> +------+-------+
>
> #合并结果集
> mysql> select * from A
> -> union
>  -> select * from B;
>  +------+-------+
> | name | score |
> +------+-------+
> | a    |    10 |
> | b    |    20 |
> | c    |    30 |
> | d    |    40 |
> +------+-------+
>
> mysql> select * from A
> -> union all
>  -> select * from B;
>  +------+-------+
> | name | score |
> +------+-------+
> | a    |    10 |
> | b    |    20 |
> | c    |    30 |
> | a    |    10 |
> | d    |    40 |
> | c    |    30 |
> +------+-------+
>
> ```
>
> 注意：被合并的两个结果，列数、列类型必须相同
>
> 如果遇到列数不相同的情况，如下的解决办法：
>
> ```mysql
> mysql> insert into C values('a',10,29),('e',20,45),('c',30,10);
>
> mysql> select * from A
> -> union 
>  -> select name,score from C;
> +------+-------+
> | name | score |
> +------+-------+
> | a    |    10 |
> | b    |    20 |
> | c    |    30 |
> | e    |    20 |
> +------+-------+
>
> ```

#### 3.连接查询

> 作用：求出多个表的乘积，例如t1和t2，如果采用了连接查询，得到的结果是t1*t2
>
> 演示：
>
> ```mysql
> mysql> select * from student,score;
> +-------+----------+-------+-------+----------+
> | stuid | stuname  | stuid | score | courseid |
> +-------+----------+-------+-------+----------+
> | 1001  | zhangsan | 1001  |    98 |        1 |
> | 1002  | lisi     | 1001  |    98 |        1 |
> | 1003  | jack     | 1001  |    98 |        1 |
> | 1004  | tom      | 1001  |    98 |        1 |
> | 1001  | zhangsan | 1002  |    80 |        2 |
> | 1002  | lisi     | 1002  |    80 |        2 |
> | 1003  | jack     | 1002  |    80 |        2 |
> | 1004  | tom      | 1002  |    80 |        2 |
> | 1001  | zhangsan | 1003  |    70 |        1 |
> | 1002  | lisi     | 1003  |    70 |        1 |
> | 1003  | jack     | 1003  |    70 |        1 |
> | 1004  | tom      | 1003  |    70 |        1 |
> | 1001  | zhangsan | 1004  |    60 |        2 |
> | 1002  | lisi     | 1004  |    60 |        2 |
> | 1003  | jack     | 1004  |    60 |        2 |
> | 1004  | tom      | 1004  |    60 |        2 |
> | 1001  | zhangsan | 1002  |    75 |        3 |
> | 1002  | lisi     | 1002  |    75 |        3 |
> | 1003  | jack     | 1002  |    75 |        3 |
> | 1004  | tom      | 1002  |    75 |        3 |
> +-------+----------+-------+-------+----------+
> 20 rows in set (0.01 sec)
>
> #问题：进行连接查询，会产生笛卡尔积
> #笛卡尔积：两个集合相乘的结果
> #解释：假设集合A={a,b},集合B={0,1,2},则笛卡尔积的结果{(a,0),(a,1),(a,2),(b,0),(b,1),(b,2)}
>
> #解决办法：在实际应用中，需要去除重复记录，则需要通过条件进行过滤
> mysql> select s.stuid,s.stuname,c.score,c.courseid from student s,score c where s.stuid=c.stuid;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1003  | jack     |    70 |        1 |
> | 1004  | tom      |    60 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> ```

##### 3.1内连接-inner join on

> 内连接的特点：查询结果必须满足条件
>
> 演示：
>
> ```mysql
> #内连接
> mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s join score c on s.stuid=c.stuid;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1003  | jack     |    70 |        1 |
> | 1004  | tom      |    60 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> #等价写法
> mysql> select  s.stuid,s.stuname,c.score,c.courseid from student s,score c where s.stuid=c.stuid;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1003  | jack     |    70 |        1 |
> | 1004  | tom      |    60 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> #练习：查询成绩大于80的学生记录
> #方式一
> mysql> select  s.stuid,s.stuname,c.score,c.courseid from student s,score c where s.stuid=c.stuid and c.score>80;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> #方式二
> #也是内连接，只不过相当于是方言，join on相当于是普通话
> mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s join score c on s.stuid=c.stuid and score>70;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> #方式三
> mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s join score c on s.stuid=c.stuid where score>70;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> ```

##### 3.2外连接-outer join on

> 特点：以其中一个表作为参照连接另外一个表
>
> 分类：
>
> ​	左外连接：left join on
>
> ​	右外连接：right join on
>
> 演示：
>
> ```mysql
> #左外连接
> mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s left join score c on s.stuid=c.stuid;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1003  | jack     |    70 |        1 |
> | 1004  | tom      |    60 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> #内连接
> mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s join score c on s.stuid=c.stuid;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1003  | jack     |    70 |        1 |
> | 1004  | tom      |    60 |        2 |
> | 1002  | lisi     |    75 |        3 |
> +-------+----------+-------+----------+
>
> #右外连接
> #参照为c
> mysql> select s.stuid,s.stuname,c.score,c.courseid  from student s right join score c on s.stuid=c.stuid;
> +-------+----------+-------+----------+
> | stuid | stuname  | score | courseid |
> +-------+----------+-------+----------+
> | 1001  | zhangsan |    98 |        1 |
> | 1002  | lisi     |    80 |        2 |
> | 1002  | lisi     |    75 |        3 |
> | 1003  | jack     |    70 |        1 |
> | 1004  | tom      |    60 |        2 |
> +-------+----------+-------+----------+
>
> ```

#### 4.子查询

> 在一个select语句中包含另外一个完整的select语句【select语句的嵌套】
>
> 注意：
>
> ​	a.子查询出现的位置：
>
> ​		from后
>
> ​		where子句的后面，作为条件的一部分被查询
>
> ​	b。当子查询出现在where后面作为条件时，可以使用关键字：any、all
>
> ​	c.子查询结果集的形式
>
> ​		单行单列
>
> ​		单行多列
>
> ​		多行多列
>
> ​		多行单列
>
> 演示：
>
> ```mysql
> #1.查询和scott在同一个部门的员工
> #思路：先查询scott所在的部门，然后根据部门查找所有的信息
> mysql> select deptno from emp where enname='scott';
> +--------+
> | deptno |
> +--------+
> |     20 |
> +--------+
>
> mysql> select * from emp where deptno=(select deptno from emp where enname='scott');
> +-------+--------+---------+------+------------+---------+------+--------+
> | empno | enname | job     | mgr  | hiredate   | sal     | comm | deptno |
> +-------+--------+---------+------+------------+---------+------+--------+
> |  7369 | smith  | clark   | 7902 | 1980-12-17 |  800.00 | NULL |     20 |
> |  7788 | scott  | analyst | 7566 | 1987-02-20 | 3000.00 | NULL |     20 |
> +-------+--------+---------+------+------------+---------+------+--------+
>
> #2.查询工资高于joens的员工信息
> #思路：先查询jones的工资，然后根据jones查询其他的员工信息
> mysql> select * from emp where sal>(select sal from emp where enname='jones');
> +-------+--------+-----------+------+------------+---------+------+--------+
> | empno | enname | job       | mgr  | hiredate   | sal     | comm | deptno |
> +-------+--------+-----------+------+------------+---------+------+--------+
> |  7788 | scott  | analyst   | 7566 | 1987-02-20 | 3000.00 | NULL |     20 |
> |  7839 | king   | president | NULL | 1987-02-20 | 5000.00 | NULL |     10 |
> +-------+--------+-----------+------+------------+---------+------+--------+
>
> #3.查询工资高于30号部门所有人的员工信息
> #思路：先查询30号部门中的最高工资，根据最高工资查询其他的员工信息
> mysql> select * from emp where deptno=30;
> +-------+--------+----------+------+------------+---------+---------+--------+
> | empno | enname | job      | mgr  | hiredate   | sal     | comm    | deptno |
> +-------+--------+----------+------+------------+---------+---------+--------+
> |  7499 | allen  | salesman | 7698 | 1981-02-20 | 1600.00 |  300.00 |     30 |
> |  7566 | jones  | managen  | 7839 | 1981-04-02 | 2975.00 |    NULL |     30 |
> |  7654 | martin | salesman | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
> |  7698 | blake  | manager  | 7839 | 1981-05-01 | 2850.00 |    NULL |     30 |
> +-------+--------+----------+------+------------+---------+---------+--------+
>
> mysql> select max(sal) from emp where deptno=30;
> +----------+
> | max(sal) |
> +----------+
> |  2975.00 |
> +----------+
>
> mysql> select * from emp where sal>(select max(sal) from emp where deptno=30);
> +-------+--------+-----------+------+------------+---------+------+--------+
> | empno | enname | job       | mgr  | hiredate   | sal     | comm | deptno |
> +-------+--------+-----------+------+------------+---------+------+--------+
> |  7788 | scott  | analyst   | 7566 | 1987-02-20 | 3000.00 | NULL |     20 |
> |  7839 | king   | president | NULL | 1987-02-20 | 5000.00 | NULL |     10 |
> +-------+--------+-----------+------+------------+---------+------+--------+
>
> #4.查询工作类型和工资与martin完全相同的员工信息
> #思路：先查询martin的工作类型和工资，然后再查询其他的员工信息
> mysql> select * from emp where (job,sal) in(select job,sal from emp where enname='martin');
> +-------+--------+----------+------+------------+---------+---------+--------+
> | empno | enname | job      | mgr  | hiredate   | sal     | comm    | deptno |
> +-------+--------+----------+------+------------+---------+---------+--------+
> |  7654 | martin | salesman | 7698 | 1981-09-28 | 1250.00 | 1400.00 |     30 |
> +-------+--------+----------+------+------------+---------+---------+--------+
>
> ```



### 二、数据库的备份和恢复

#### 1.备份

> 生成SQL脚本，导出数据
>
> 命令：mysqldump -u root -p  数据库名>生成sql脚本的路径
>
> 注意：
>
> ​		可以不需要登录数据库
>
> ​		windows系统: 使用管理员权限打开CMD
>
> 演示：
>
> ```mysql
> C:\Users\ijeff> mysqldump -u root -p mydb1 > C:/Users/ijeff/Desktop/mydb1.sql
> Enter password: 
>
>
> ```

#### 2.恢复

> 执行sql脚本，恢复数据
>
> 前提：必须先创建数据库【空的】
>
> 注意：需要先登录数据库，然后进入指定的数据库，执行sql脚本
>
> 演示：
>
> ```mysql
> C:\Users\ijeff> mysql -u root -p
> Enter password: 
>
> mysql> create database test;
>
> mysql> use test;
> mysql> show tables;
>
> mysql> source C:/Users/ijeff/Desktop/mydb1.sql;
> ```

