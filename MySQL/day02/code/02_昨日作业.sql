-- # 建学生信息表student
-- create table student(
-- 	sno varchar(20) primary key,
-- 	sname varchar(20),
-- 	ssex varchar(20),
-- 	sbirthday datetime,	
-- 	class varchar(20)
-- );
-- #建立成绩表
-- create table score
-- (
-- 	sno varchar(20),
-- 	cno varchar(20),
-- 	degree decimal
-- );
-- #添加学生信息
-- insert into student values('108','曾华','男','1977-09-01','95033');
-- insert into student values('105','匡明','男','1975-10-02','95031');
-- insert into student values('107','王丽','女','1976-01-23','95033');
-- insert into student values('101','李军','男','1976-02-20','95033');
-- insert into student values('109','王芳','女','1975-02-10','95031');
-- insert into student values('103','陆君','男','1974-06-03','95031');
-- #添加成绩表
-- insert into score values('103','3-245','86');
-- insert into score values('105','3-245','75');
-- insert into score values('109','3-245','68');
-- insert into score values('103','3-105','92');
-- insert into score values('105','3-105','88');
-- insert into score values('109','3-105','76');
-- insert into score values('103','3-105','64');
-- insert into score values('105','3-105','91');
-- insert into score values('109','3-105','78');
-- insert into score values('103','6-166','85');
-- insert into score values('105','6-166','79');
-- insert into score values('109','6-166','81');

#1、 查询Student表中的所有记录的Sname、Ssex和Class列
#2、 查询学生的生日，不重复的sbirthday列
#3、 查询Student表的所有记录
#4、 查询Score表中成绩在60到80之间的所有记录
#5、 查询Score表中成绩为85，86或88的记录
#6、 查询Student表中“95031”班或性别为“女”的同学记录
#7、 以Class降序查询Student表的所有记录
#8、 以Cno升序、Degree降序查询Score表的所有记录
#9、 查询分数大于70，小于90的Sno列

#10、查询“95031”班的学生人数
-- select count(*) from student where class='95031';

#11、查询Score表中的最高分的学生学号和课程号(子查询)
-- select max(degree) from score;  -- 92
-- select sno, cno from score where degree=92;
select sno, cno from score where degree=(select max(degree) from score);


#12、查询每门课的平均成绩（分组）
select cno, avg(degree) from score group by cno;
-- select cno, avg(degree) from score group by cno having avg(degree)>80;

#13、查询Score表中至少有5名学生选修的并以3开头的课程的平均分数 （分组）
select cno, avg(degree) from score where cno like '3%' group by cno having count(*)>=5;

	
	