-- 注释

-- 启动数据库: net start mysql57;
-- 关闭数据库: net stop mysql57;
-- 连接数据库: mysql -u root -p

-- 创建数据库: create DATABASE mydb2_2 charset=utf8;
-- 删除数据库: drop database mydb2_2;
-- 查看数据库: show databases;
-- 进入数据库: use mydb2_2;
-- 查看当前使用的数据库: select database();

-- 创建表: create table person(id...)
-- 删除表: drop table person;
-- 查看表: show tables;
-- 清空表: truncate table person;

-- 增: insert into person(name,age) values()
-- 删: delete from person where id=1;
-- 改: update person set age=11 where id=1;
-- 查: 
-- select * from person;
-- select id,name from person;
-- select * from person where id>2;
-- select * from person where id>2 and id<4;
-- select * from person where id between 2 and 4;
-- select * from person where id in (1,2,3,4);
-- select * from person where id is null;
-- select * from person where name like '_刘%'
-- select * from person as p;
-- select distinct name from person;
-- select * from person order by age desc;
-- select count(*) from person;
-- select deptno,count(*) from emp group by deptno;
-- select deptno,count(*) from emp group by deptno having count(*)>2;
-- select * from person limit 3,3;




