-- #创建表
-- create table A(
--   name varchar(10),
--   score int
-- );
-- 
-- create table B( 
--   name varchar(10), 
--   score int 
-- );
-- 
-- #批量插入数据
-- insert into A values('a',10),('b',20),('c',30);
-- insert into B values('a',10),('d',40),('c',30);

-- select * from A;
-- select * from B;
-- 
-- # union: 合并结果集,去除重复数据
-- select * from A union select * from B;
-- 
-- # union all: 合并结果集,没有去除重复数据
-- select * from A union all select * from B;

use mydb2;
select * from student;
select * from score;

-- 笛卡尔积
-- select * from student,score;

-- 获取2个表之间有关联的数据
-- select * from student,score where student.sno=score.sno;
-- select * from student s, score c where s.sno=c.sno;


-- 连接
-- 内连接: inner join on  => join on
select * from student s join score c on s.sno=c.sno;

-- 外链接
--   左外连接: LEFT OUTER JOIN ON => left join on
select * from student s left join score c on s.sno=c.sno;

--   右外连接: RIGHT OUTER JOIN ON => right join on
select * from score c right join student s on s.sno=c.sno;


select s.*, degree from score c right join student s on s.sno=c.sno;








