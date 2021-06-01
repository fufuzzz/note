# Day01_MySQL基础

### 一、数据库简介

#### 1.数据库系统 

##### 1.1数据库

> DataBase【DB】，指的是长期保存到计算机上的数据，按照一定顺序组织，可以被各种用户或者应用共享的数据集合 
>
>  持久化存储 / 临时存储(缓存)
>
> 【用于存储数据的地方，可以视为存储数据的容器】

##### 1.2数据库管理系统

> DataBase Management System【DBMS】,能够管理和操作数据库的大型的软件 
>
> 数据库是CS模式: Client/Server  
>
> 用于建立、使用和维护数据库，对数据库进行统一的管理和控制，为了保证数据库的安全性和完整性，用户可以通过数据库管理系统访问数据库中的数据
>

##### 1.3数据库的应用

> 涉及到大量的数据需要长期存储，就可以使用数据库  
>
> 使用：增删改查的操作  
>
> 持久化： 数据持久化,  一般存在硬盘，MySQL   
>
> 缓存： 临时存储， 一般可以存在内存,  Redis

#### 2.常见数据库管理系统

> 1>Oracle（甲骨文）: 目前比较成功的关系型数据库管理系统，运行稳定，功能齐全，性能超群，技术领先，主要应用在大型的企业数据库领域, 收费.
>
> 2>DB2:  IBM（国际商业机器公司）的产品，伸缩性比较强
>
> 3>SQL Server:  Microsoft的产品，软件界面友好，易学易用，在操作性和交互性方面独树一帜 
>
> 4>MySQL: 免费的数据库系统，被广泛引用于中型应用系统，体积小，速度快，总体拥有成本低，开放源代码，2008年被SUN收购，2009年SUN被Oracle收购  

### 二.数据库的安装

#### 1.安装MySQL

> 严格按照按照步骤, 安装MySQL
>

#### 2.启动和停止mysql服务

windows系统：

> windows 开启mysql: `net start mysql57`
>
> windows 关闭mysql: `net stop mysql57 `

### 三、SQL概述

#### 1.SQL简介 

> Structure Query  Language，结构化查询语言

#### 2.数据库服务器、数据库和表之间的关系

> 表：为了保存应用实体中的数据，一般会给数据库中创建表，一个数据库可以同时管理多个表
>

#### 3.数据在SQL中的存储形式

> 数据库 => 表
>
> 表: 表格table
>
> 列：表示字段,  id， name, age
>
> 行：代表一条数据， 一条记录 或 一个实体
>
> | id   | name | age  |
> | ---- | ---- | ---- |
> | 1    | 马云   | 50   |
> | 2    | 马化腾  | 40   |
> | 3    | 马明哲  | 60   |

#### 4.SQL的分类

> DDL【Data   Definition Language】,数据定义语言，用户创建、修改、删除表结构
>
> DML【Data  Manipulation Language】,数据操作语言，用于对表数据进行增删改的操作
>
> DQL【Data  Query Language】,数据查询语言，用于负责表数据的查询工作
>
> DCL【Data Control Language】：数据控制语言，用来定义访问权限和安全级别

### 四、数据库操作

#### 1.DDL

> 使用关键字：CREATE    ALTER    DROP  
>
> 注意：一般情况下，mysql关键字是大写的，但是为了方便，一般小写

##### 1.1 create创建

> 语法：
>
> ```mysql
> #创建数据库
> CREATE DATABASE database_name charset=utf8;
>
> #创建表
> CREATE TABLE 表名 (
> 		字段1 字段类型[列级别约束条件][默认值]，
> 		字段2 字段类型[列级别约束条件][默认值]，
> 		….
> 		字段n 字段类型[列级别约束条件][默认值]
> 		[表级别约束条件]
> )
> # 创建user表
> create table students(
>   	id int primary key auto_increment, 
>   	name varchar(20), 
>   	age int
> );
>
> ```
>
> 演示：
>
> ```mysql
> #查询当前数据库服务器中的所有数据库
> mysql> show databases;			    
> +--------------------+	
> | Database           |
> +--------------------+
> | information_schema |
> | mydb1              |
> | mysql              |
> | performance_schema |
> | sys                |
> +--------------------+
> 5 rows in set (0.01 sec)
>
> #查看当前正在使用的数据库
> mysql> select database();
> +------------+
> | database() |
> +------------+
> | mydb1      |
> +------------+
> 1 row in set (0.00 sec)
>
> #切换数据库
> mysql> use mydb1;
> Database changed
>
> #退出数据库
> 演示命令：
> #方式一
> mysql> exit
> Bye
>
> #方式二
> mysql> quit
> Bye
>
> #注意：如要再次使用数据库，则需要重新登录
>
> ```
>

##### 1.2alter操作

> a.语法：
>
> ```mysql
> #1.修改表名
> 语法规则：ALTER TABLE old_table_name RENAME [TO] new_table_name
>
> #2.修改字段的数据类型
> 语法规则：ALTER TABLE table_name MODIFY 字段名 数据类型
> 修改完成之后可以查看DESC table_name检验结果
>
> #3.修改字段名
> 语法规则：ALTER TABLE table_name CHANGE 旧字段名 新字段名 数据类型
>
> #4.添加字段
> 语法规则：ALTER TABLE table_name ADD 新字段名 数据类型 [约束条件] [FIRST|AFTER 已经存在的字段名]
>
> #5.删除字段
> 语法规则：ALTER TABLE table_name DROP 字段名
>
> #6.修改字段的排列位置
> 语法规则：ALTER TABLE table_name MODIFY 字段1 数据类型 FIRST|AFTER 字段2
> 	first: 设置成第一个
> 	after 字段2： 在指定字段2的后面
> 	
> #7.删除表的外键约束
> 语法规则：ALTER TABLE table_name DROP FOREIGN KEY 外键约束名（不是字段名）
>
> #8.删除数据表
> #删除没有被关联的表
> 语法规则：DROP TABLE [IF EXISTS] 表1，表2...
> #删除被其他表关联的的表
> 直接删除会出现错误的，操作： 先解除关联 再进行删除
> ```
>
> b.常用数据类型
>
> ```
> 1.数字数据类型 
> int: 
> 	正常大小的整数，可以带符号。如果是有符号的，它允许的范围是从-2147483648到2147483647。如果是无符号，允许的范围是从0到4294967295。 可以指定多达11位的宽度。  int  => int(11)
> tinyint: 
> 	一个非常小的整数，可以带符号。如果是有符号，它允许的范围是从-128到127。如果是无符号，允许的范围是从0到255，可以指定多达4位数的宽度。 int(4)
> smallint:
> 	一个小的整数，可以带符号。如果有符号，允许范围为-32768至32767。如果无符号，允许的范围是从0到65535，可以指定最多5位的宽度。 int(5)
> mediumint:
> 	一个中等大小的整数，可以带符号。如果有符号，允许范围为-8388608至8388607。 如果无符号，允许的范围是从0到16777215，可以指定最多9位的宽度。int(9)
> bigint:
> 	一个大的整数，可以带符号。如果有符号，允许范围为-9223372036854775808到9223372036854775807。如果无符号，允许的范围是从0到18446744073709551615. 可以指定最多20位的宽度。 int(20)
> 	
> float(M,D): 
> 	不能使用无符号的浮点数字。可以定义显示长度(M)和小数位数(D)。这不是必需的，并且默认为10,2。其中2是小数的位数，10是数字(包括小数)的总数。小数精度可以到24个浮点。 float(10,2)
> double(M,D):
> 	不能使用无符号的双精度浮点数。可以定义显示长度(M)和小数位数(D)。 这不是必需的，默认为16,4，其中4是小数的位数。小数精度可以达到53位的DOUBLE。 REAL是DOUBLE同义词。 double(16,4)
> decimal(M,D):
> 	非压缩浮点数不能是无符号的。在解包小数，每个小数对应于一个字节。定义显示长度(M)和小数(D)的数量是必需的。 NUMERIC是DECIMAL的同义词。[decimal]
>
> 2.日期和时间类型
> date:
> 	以YYYY-MM-DD格式的日期，在1000-01-01和9999-12-31之间。 例如，1973年12月30日将被存储为1973-12-30。
> datetime:
> 	日期和时间组合以YYYY-MM-DD HH:MM:SS格式，在1000-01-01 00:00:00 到9999-12-31 23:59:59之间。例如，1973年12月30日下午3:30，会被存储为1973-12-30 15:30:00。
> timestamp:
> 	1970年1月1日午夜之间的时间戳，到1973的某个时候。这看起来像前面的DATETIME格式，无需只是数字之间的连字符; 1973年12月30日下午3点30分将被存储为19731230153000(YYYYMMDDHHMMSS)。
> time:
> 	存储时间在HH:MM:SS格式。
> year(M):
> 	以2位或4位数字格式来存储年份。如果长度指定为2(例如YEAR(2))，年份就可以为1970至2069(70〜69)。如果长度指定为4，年份范围是1901-2155，默认长度为4。
>
> 3.字符串类型
> 虽然数字和日期类型比较有意思，但存储大多数数据都可能是字符串格式。 下面列出了在MySQL中常见的字符串数据类型。
> char(20):
> 	固定长度的字符串是以长度为1到255之间个字符长度(例如：CHAR(5))，存储右空格填充到指定的长度。 限定长度不是必需的，它会默认为1。   name char(50) 
> varchar(M):
> 	可变长度的字符串是以长度为1到255之间字符数(高版本的MySQL超过255); 例如： VARCHAR(25). 创建VARCHAR类型字段时，必须定义长度。 [varchar]    name varchar(255)
> 	
> blob or text:
> 	字段的最大长度是65535个字符。 BLOB是“二进制大对象”，并用来存储大的二进制数据，如图像或其他类型的文件。定义为TEXT文本字段还持有大量的数据; 两者之间的区别是，排序和比较上存储的数据，BLOB大小写敏感，而TEXT字段不区分大小写。不用指定BLOB或TEXT的长度。
> tinyblob 或 tinytext:
> 	BLOB或TEXT列用255个字符的最大长度。不指定TINYBLOB或TINYTEXT的长度。
> mediumblob or mediumtext:
> 	BLOB或TEXT列具有16777215字符的最大长度。不指定MEDIUMBLOB或MEDIUMTEXT的长度。
> longblob 或 longtext:
> 	BLOB或TEXT列具有4294967295字符的最大长度。不指定LONGBLOB或LONGTEXT的长度。
> enum:
> 	枚举，这是一个奇特的术语列表。当定义一个ENUM，要创建它的值的列表，这些是必须用于选择的项(也可以是NULL)。例如，如果想要字段包含“A”或“B”或“C”，那么可以定义为ENUM为 ENUM(“A”，“B”，“C”)也只有这些值(或NULL)才能用来填充这个字段。
> ```

> 注意：主要了解 char 和 varchar 的区别
>
> char(M)是固定长度的字符串， 在定义时指定字符串列长。当保存数据时如果长度不够在右侧填充空格以达到指定的长度。M 表示列的长度，M 的取值范围是0-255个字符 name char(20)   
>
> varchar(M)是长度可变的字符串，M 表示最大的列长度。M 的取值范围是0-65535。varchar的最大实际长度是由最长的行的大小和使用的字符集确定的，而实际占用的空间为字符串的实际长度+1
>
> ​	name varchar(30)
>
> **主要使用的数据类型：**
>
> ​	**数字型数据类型：int    float**
>
> ​	**日期类：date  datetime time**
>
> ​	**字符串：varchar(num)   text【长字符串】**
>
> c.需求：创建一个员工表【图3】
>
> ![](imgs\图3-员工表.png)
>
> 演示：
>
> ```mysql
> #切换数据库
> mysql> use mydb1			
> Database changed
> #查看当前正在使用的数据库
> mysql> select database();	
> +------------+
> | database() |
> +------------+
> | mydb1      |
> +------------+
> 1 row in set (0.00 sec)
>
> #在当前数据库下创建新的表
> mysql> create table worker(			
>  -> id int(11) primary key,
>  -> name varchar(20),
>  -> gender varchar(10),
>  -> brithday date,
>  -> entry_date date,
>  -> job varchar(20),
>  -> salary double,
>  -> resume text
>  -> );
> Query OK, 0 rows affected (0.02 sec)
>
> #显示当前数据库中的所有表
> mysql> show tables;			
> +-----------------+
> | Tables_in_mydb1 |
> +-----------------+
> | worker          |
> +-----------------+
> 1 row in set (0.00 sec)
>
> #显示指定表中的所有字段
> mysql> desc worker;			
> +------------+-------------+------+-----+---------+-------+
> | Field      | Type        | Null | Key | Default | Extra |
> +------------+-------------+------+-----+---------+-------+
> | id         | int(11)     | YES  |     | NULL    |       |
> | name       | varchar(20) | YES  |     | NULL    |       |
> | gender     | varchar(10) | YES  |     | NULL    |       |
> | brithday   | date        | YES  |     | NULL    |       |
> | entry_date | date        | YES  |     | NULL    |       |
> | job        | varchar(20) | YES  |     | NULL    |       |
> | salary     | double      | YES  |     | NULL    |       |
> | resume     | blob        | YES  |     | NULL    |       |
> +------------+-------------+------+-----+---------+-------+
> 8 rows in set (0.01 sec)
>
> #增加字段image
> mysql> alter table worker add image blob;
> Query OK, 0 rows affected (0.04 sec)
> Records: 0  Duplicates: 0  Warnings: 0
>
> mysql> desc worker;
> +------------+-------------+------+-----+---------+-------+
> | Field      | Type        | Null | Key | Default | Extra |
> +------------+-------------+------+-----+---------+-------+
> | id         | int(11)     | YES  |     | NULL    |       |
> | name       | varchar(20) | YES  |     | NULL    |       |
> | gender     | varchar(10) | YES  |     | NULL    |       |
> | brithday   | date        | YES  |     | NULL    |       |
> | entry_date | date        | YES  |     | NULL    |       |
> | job        | varchar(20) | YES  |     | NULL    |       |
> | salary     | double      | YES  |     | NULL    |       |
> | resume     | blob        | YES  |     | NULL    |       |
> | image      | blob        | YES  |     | NULL    |       |
> +------------+-------------+------+-----+---------+-------+
> 9 rows in set (0.00 sec)
>
> #修改job的长度为60
> mysql> alter table worker modify job varchar(60);
> Query OK, 0 rows affected (0.00 sec)
> Records: 0  Duplicates: 0  Warnings: 0
>
> mysql> desc worker;
> +------------+-------------+------+-----+---------+-------+
> | Field      | Type        | Null | Key | Default | Extra |
> +------------+-------------+------+-----+---------+-------+
> | id         | int(11)     | YES  |     | NULL    |       |
> | name       | varchar(20) | YES  |     | NULL    |       |
> | gender     | varchar(10) | YES  |     | NULL    |       |
> | brithday   | date        | YES  |     | NULL    |       |
> | entry_date | date        | YES  |     | NULL    |       |
> | job        | varchar(60) | YES  |     | NULL    |       |
> | salary     | double      | YES  |     | NULL    |       |
> | resume     | blob        | YES  |     | NULL    |       |
> | image      | blob        | YES  |     | NULL    |       |
> +------------+-------------+------+-----+---------+-------+
> 9 rows in set (0.00 sec)
>
> #删除image字段
> mysql> alter table worker drop image;
> Query OK, 0 rows affected (0.01 sec)
> Records: 0  Duplicates: 0  Warnings: 0
>
> mysql> desc worker;
> +------------+-------------+------+-----+---------+-------+
> | Field      | Type        | Null | Key | Default | Extra |
> +------------+-------------+------+-----+---------+-------+
> | id         | int(11)     | YES  |     | NULL    |       |
> | name       | varchar(20) | YES  |     | NULL    |       |
> | gender     | varchar(10) | YES  |     | NULL    |       |
> | brithday   | date        | YES  |     | NULL    |       |
> | entry_date | date        | YES  |     | NULL    |       |
> | job        | varchar(60) | YES  |     | NULL    |       |
> | salary     | double      | YES  |     | NULL    |       |
> | resume     | blob        | YES  |     | NULL    |       |
> +------------+-------------+------+-----+---------+-------+
> 8 rows in set (0.00 sec)
>
> #对表名重新命名
> #方式一
> mysql> rename table worker to user;
> Query OK, 0 rows affected (0.00 sec)
> #方式二
> mysql> alter table  worker rename to user;
> Query OK, 0 rows affected (0.00 sec)
>
> #查看表的信息
> mysql> desc user;
> +------------+-------------+------+-----+---------+-------+
> | Field      | Type        | Null | Key | Default | Extra |
> +------------+-------------+------+-----+---------+-------+
> | id         | int(11)     | YES  |     | NULL    |       |
> | name       | varchar(20) | YES  |     | NULL    |       |
> | gender     | varchar(10) | YES  |     | NULL    |       |
> | brithday   | date        | YES  |     | NULL    |       |
> | entry_date | date        | YES  |     | NULL    |       |
> | job        | varchar(60) | YES  |     | NULL    |       |
> | salary     | double      | YES  |     | NULL    |       |
> | resume     | blob        | YES  |     | NULL    |       |
> +------------+-------------+------+-----+---------+-------+
> 8 rows in set (0.00 sec)
>
>
> #查看创建表的详细信息
> mysql> show create table user;
> | Table | Create Table                                                                                                   
> | user  | CREATE TABLE `user` (
> `id` int(11) DEFAULT NULL,
> `name` varchar(20) DEFAULT NULL,
> `gender` varchar(10) DEFAULT NULL,
> `brithday` date DEFAULT NULL,
> `entry_date` date DEFAULT NULL,
> `job` varchar(60) DEFAULT NULL,
> `salary` double DEFAULT NULL,
> `resume` blob
> ) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
>
> 1 row in set (0.00 sec)
>
>
> #修改表的字符集为gbk
> mysql> alter table user character set gbk;	
> Query OK, 0 rows affected (0.00 sec)
> Records: 0  Duplicates: 0  Warnings: 0
>
> mysql> show create table user;			#查看信息，已经改为gbk
>
> | Table | Create Table                                       
> | user  | CREATE TABLE `user` (
> `id` int(11) DEFAULT NULL,
> `name` varchar(20) CHARACTER SET latin1 DEFAULT NULL,
> `gender` varchar(10) CHARACTER SET latin1 DEFAULT NULL,
> `brithday` date DEFAULT NULL,
> `entry_date` date DEFAULT NULL,
> `job` varchar(60) CHARACTER SET latin1 DEFAULT NULL,
> `salary` double DEFAULT NULL,
> `resume` blob
> ) ENGINE=InnoDB DEFAULT CHARSET=gbk |
>
> 1 row in set (0.00 sec)
>
> #将列名name修改为username
> mysql> alter table user change name username varchar(100);
> Query OK, 0 rows affected (0.02 sec)
> Records: 0  Duplicates: 0  Warnings: 0
>
> mysql> desc user;
> +------------+--------------+------+-----+---------+-------+
> | Field      | Type         | Null | Key | Default | Extra |
> +------------+--------------+------+-----+---------+-------+
> | id         | int(11)      | YES  |     | NULL    |       |
> | username   | varchar(100) | YES  |     | NULL    |       |
> | gender     | varchar(10)  | YES  |     | NULL    |       |
> | brithday   | date         | YES  |     | NULL    |       |
> | entry_date | date         | YES  |     | NULL    |       |
> | job        | varchar(60)  | YES  |     | NULL    |       |
> | salary     | double       | YES  |     | NULL    |       |
> | resume     | blob         | YES  |     | NULL    |       |
> +------------+--------------+------+-----+---------+-------+
> 8 rows in set (0.00 sec)
>
> ```

##### 1.3drop删除

> 语法：
>
> ```mysql
> # 删除数据库
> DROP DATABASE database_name
> ```
>
> 演示：
>
> ```mysql
> # 删除表
> drop table user;
> ```

#### 2.DML: 增删改

##### 2.1 insert 插入

> 语法：
>
> ```mysql
> #单行插入
> INSERT INTO table_name (field1, field2,...fieldN) VALUES(value1, value2,...valueN);
>                        
> #多行插入[批量插入]
> INSERT INTO table_name (field1, field2,...fieldN)
>                        VALUES
>                        (value1, value2,...valueN),
>                        (value12, value22,...valueNN)...;
>                        
> 注意：
> 	a.列名和列值的类型、个数以及顺序一一对应
> 	b.可以把列名当做Python中的形参，把列值当做实参
> 	c.值不能超出列定义的长度
> 	d.如果插入的是空值，写Null/null
> 	e.插入的是日期，和字符串一样，使用引号括起来  "1988-11-22 10:11:12"
> ```
>

> 演示：
>
> ```mysql
> mysql> use mydb1;
> Database changed
> mysql> show tables;
> Empty set (0.00 sec)
>
> mysql> create table worker(
>     -> id int(11),
>     -> name varchar(20),
>     -> gender varchar(10),
>     -> salary double
>     -> );
> Query OK, 0 rows affected (0.01 sec)
>
> mysql> show tables;                                                             +-----------------+
> | Tables_in_mydb1 |
> +-----------------+
> | worker          |
> +-----------------+
> 1 row in set (0.00 sec)
>
> mysql> desc worker;
> +--------+-------------+------+-----+---------+-------+
> | Field  | Type        | Null | Key | Default | Extra |
> +--------+-------------+------+-----+---------+-------+
> | id     | int(11)     | YES  |     | NULL    |       |
> | name   | varchar(20) | YES  |     | NULL    |       |
> | gender | varchar(10) | YES  |     | NULL    |       |
> | salary | double      | YES  |     | NULL    |       |
> +--------+-------------+------+-----+---------+-------+
> 4 rows in set (0.00 sec)
>
> #插入单条数据
> mysql> insert into worker(id,name,gender,salary) values(1,'tom','b',4000);
> Query OK, 1 row affected (0.02 sec)
>
> mysql> insert into worker(id,name,gender,salary) values(2,'jack','b',6000);
> Query OK, 1 row affected (0.01 sec)
>
> #如果给每个字段都赋值，就可以省略掉字段的书写
> mysql> insert into worker values(3,'rose','g',6000);
> Query OK, 1 row affected (0.01 sec)
>
> mysql> desc worker;
> +--------+-------------+------+-----+---------+-------+
> | Field  | Type        | Null | Key | Default | Extra |
> +--------+-------------+------+-----+---------+-------+
> | id     | int(11)     | YES  |     | NULL    |       |
> | name   | varchar(20) | YES  |     | NULL    |       |
> | gender | varchar(10) | YES  |     | NULL    |       |
> | salary | double      | YES  |     | NULL    |       |
> +--------+-------------+------+-----+---------+-------+
> 4 rows in set (0.00 sec)
>
> mysql> select * from worker;
> +------+------+--------+--------+
> | id   | name | gender | salary |
> +------+------+--------+--------+
> |    1 | tom  | b      |   4000 |
> |    2 | jack | b      |   6000 |
> |    3 | rose | g      |   6000 |
> +------+------+--------+--------+
> 3 rows in set (0.00 sec)
>
> #一次性插入多条数据【批量插入】
> mysql> insert into worker(id,name,gender,salary) values(4,'bob','b',1500),(5,'hello','g',5500),(6,'abc','b',6600);
> Query OK, 3 rows affected (0.01 sec)
> Records: 3  Duplicates: 0  Warnings: 0
>
> mysql> select * from worker;                                                   
> +------+-------+--------+--------+
> | id   | name  | gender | salary |
> +------+-------+--------+--------+
> |    1 | tom   | b      |   4000 |
> |    2 | jack  | b      |   6000 |
> |    3 | rose  | g      |   6000 |
> |    4 | bob   | b      |   1500 |
> |    5 | hello | g      |   5500 |
> |    6 | abc   | b      |   6600 |
> +------+-------+--------+--------+
> 6 rows in set (0.00 sec)
> ```

##### 2.2 update更新

> 语法：
>
> ```mysql
> UPDATE table_name SET field1=new-value1, field2=new-value2  [WHERE Clause]
>
> 注意：
> 	a.完全可以更新一个字段或者多个字段
> 	b.where相当于Python中的if语句
> 	c.可以指定任何条件到where子句中
> 	d.如果没有where子句，则默认所有的行都被同时更新为指定的操作[慎用！一般要结合where使用]
>
> ```
>
> 演示：
>
> ```mysql
> #1.将所有员工的薪水修改为5000
> mysql> update worker set salary=5000;
> Query OK, 6 rows affected (0.01 sec)
> Rows matched: 6  Changed: 6  Warnings: 0
>
> mysql> select * from worker;
> +------+-------+--------+--------+
> | id   | name  | gender | salary |
> +------+-------+--------+--------+
> |    1 | tom   | b      |   5000 |
> |    2 | jack  | b      |   5000 |
> |    3 | rose  | g      |   5000 |
> |    4 | bob   | b      |   5000 |
> |    5 | hello | g      |   5000 |
> |    6 | abc   | b      |   5000 |
> +------+-------+--------+--------+
> 6 rows in set (0.00 sec)
>
> #2.将tom的薪水改为3000元
> mysql> update worker set salary=3000 where name='tom';
> Query OK, 1 row affected (0.01 sec)
> Rows matched: 1  Changed: 1  Warnings: 0
>
> mysql> select * from worker;
> +------+-------+--------+--------+
> | id   | name  | gender | salary |
> +------+-------+--------+--------+
> |    1 | tom   | b      |   3000 |
> |    2 | jack  | b      |   5000 |
> |    3 | rose  | g      |   5000 |
> |    4 | bob   | b      |   5000 |
> |    5 | hello | g      |   5000 |
> |    6 | abc   | b      |   5000 |
> +------+-------+--------+--------+
> 6 rows in set (0.00 sec)
>
> #3.将jack的薪水改为10000，并将性别改为g
> mysql> update worker set salary=10000,gender='g' where name='jack';
> Query OK, 1 row affected (0.01 sec)
> Rows matched: 1  Changed: 1  Warnings: 0
>
> mysql> select * from worker;
> +------+-------+--------+--------+
> | id   | name  | gender | salary |
> +------+-------+--------+--------+
> |    1 | tom   | b      |   3000 |
> |    2 | jack  | g      |  10000 |
> |    3 | rose  | g      |   5000 |
> |    4 | bob   | b      |   5000 |
> |    5 | hello | g      |   5000 |
> |    6 | abc   | b      |   5000 |
> +------+-------+--------+--------+
> 6 rows in set (0.00 sec)
>
> #4.将rose的薪水在原来的基础上增加1000
> mysql> update worker set salary=salary+1000 where name='rose';
> Query OK, 1 row affected (0.01 sec)
> Rows matched: 1  Changed: 1  Warnings: 0
>
> mysql> select * from worker;
> +------+-------+--------+--------+
> | id   | name  | gender | salary |
> +------+-------+--------+--------+
> |    1 | tom   | b      |   3000 |
> |    2 | jack  | g      |  10000 |
> |    3 | rose  | g      |   6000 |
> |    4 | bob   | b      |   5000 |
> |    5 | hello | g      |   5000 |
> |    6 | abc   | b      |   5000 |
> +------+-------+--------+--------+
> 6 rows in set (0.01 sec)
>
> #5.将abc的薪水改为6000
> update worker set salary=6000 where name='abc';
> #6.将bob的性别改为b
> update worker set gender='b' where name='bob';
> ```

##### where子句

> 语法：
>
> 注意：where子句其实就是一个操作符，类似于Python中的if语句，可以做数据的筛选
>
> | 操作符              | 说明            |
> | ---------------- | ------------- |
> | =                | 相等            |
> | <> /  !=         | 不相等           |
> | <                | 小于            |
> | <=               | 小于等于          |
> | >                | 大于            |
> | >=               | 大于等于          |
> | in (A，B)         | A 和 B 中间的一个   |
> | between A  and B | 位于两值之间        |
> | AND              | 连接多个表达式 并且的关系 |
>

##### 2.3delete删除

> 语法：
>
> ```mysql
> DELETE FROM table_name [WHERE Clause] 
>
> 注意：
> 	a.如果where子句没有指定，则默认将表中的数据全部删除【慎用！】
> 	b.可以指定任何条件在where子句中
> ```
>

> 演示：
>
> ```mysql
> #1.删除表中tom的全部数据
> mysql> delete from worker where name='tom';
> Query OK, 1 row affected (0.01 sec)
>
> mysql> select * from worker;
> +------+-------+--------+--------+
> | id   | name  | gender | salary |
> +------+-------+--------+--------+
> |    2 | jack  | g      |  10000 |
> |    3 | rose  | g      |   6000 |
> |    4 | bob   | b      |   5000 |
> |    5 | hello | g      |   5000 |
> |    6 | abc   | b      |   5000 |
> +------+-------+--------+--------+
> 5 rows in set (0.00 sec)
>
> #2.删除表中的所有数据
> mysql> delete from worker;
> Query OK, 5 rows affected (0.01 sec)
>
> mysql> select * from worker;
> Empty set (0.00 sec)
>
> # 删除表中的数据的方法有delete,truncate, 其中TRUNCATE TABLE用于删除表中的所有行，而不记录单个行删除操作。TRUNCATE TABLE 与没有 WHERE 子句的 DELETE 语句类似；但是，TRUNCATE TABLE 速度更快，使用的系统资源和事务日志资源更少
> # Truncate是一个能够快速清空资料表内所有资料的SQL语法。并且能针对具有自动递增值的字段，做计数重置归零重新计算的作用。
> mysql> truncate table worker;
> Query OK, 0 rows affected (0.02 sec)
>
> #3.删除表
> mysql> drop table worker;
> Query OK, 0 rows affected (0.01 sec)
>
> mysql> show tables;
> Empty set (0.00 sec)
>
> 注意：
> delete:删除表中的指定数据，表结构还在，删除之后的数据可以找回，对自动增加的字段无影响
> truncate：清空表中的数据，删除的数据是不能找回的，执行速度比delete快，自动增加的字段会重新计数
> drop: 删除表，数据和表结构都删除
> ```

> 




