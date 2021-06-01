-- create table students (
-- 	sno varchar(3) not null, 
-- 	sname varchar(4) not null, 
-- 	ssex varchar(2) not null, 
-- 	sbirthday datetime,
-- 	class varchar(5)
-- );
-- 
-- create table courses (
-- 	cno varchar(5) not null, 
-- 	cname varchar(10) not null, 
-- 	tno varchar(10) not null
-- );
-- create table scores (
-- 	sno varchar(3) not null, 
-- 	cno varchar(5) not null, 
-- 	degree int not null
-- );
-- create table teachers (
-- 	tno varchar(3) not null,
-- 	tname varchar(4) not null, 
-- 	tsex varchar(2) not null, 
-- 	tbirthday datetime not null, 
-- 	prof varchar(6), 
-- 	depart varchar(10) not null
-- );
-- 
-- insert into students(sno,sname,ssex,sbirthday, class) values (108 ,'曾华' ,'男' ,'1977-09-01',95033);
-- insert into students(sno,sname,ssex,sbirthday, class) values (105 ,'匡明' ,'男' ,'1975-10-02',95031);
-- insert into students(sno,sname,ssex,sbirthday, class) values (107 ,'王丽' ,'女' ,'1976-01-23',95033);
-- insert into students(sno,sname,ssex,sbirthday, class) values (101 ,'李军' ,'男' ,'1976-02-20',95033);
-- insert into students(sno,sname,ssex,sbirthday, class) values (109 ,'王芳' ,'女' ,'1975-02-10',95031);
-- insert into students(sno,sname,ssex,sbirthday, class) values (103 ,'陆君' ,'男' ,'1974-06-03',95031);
-- 
-- insert into  courses(cno,cname,tno) values('3-105' ,'计算机导论',825); 
-- insert into  courses(cno,cname,tno) values('3-245' ,'操作系统' ,804); 
-- insert into  courses(cno,cname,tno) values('6-166' ,'数据电路' ,856); 
-- insert into  courses(cno,cname,tno) values('9-888' ,'高等数学' ,100);
-- 
-- insert into  scores(sno,cno,degree) values(103,'3-245',86); 
-- insert into  scores(sno,cno,degree) values(105,'3-245',75); 
-- insert into  scores(sno,cno,degree) values(109,'3-245',68); 
-- insert into  scores(sno,cno,degree) values(103,'3-105',92); 
-- insert into  scores(sno,cno,degree) values(105,'3-105',88); 
-- insert into  scores(sno,cno,degree) values(109,'3-105',76); 
-- insert into  scores(sno,cno,degree) values(101,'3-105',64); 
-- insert into  scores(sno,cno,degree) values(107,'3-105',91); 
-- insert into  scores(sno,cno,degree) values(108,'3-105',78); 
-- insert into  scores(sno,cno,degree) values(101,'6-166',85); 
-- insert into  scores(sno,cno,degree) values(107,'6-106',79); 
-- insert into  scores(sno,cno,degree) values(108,'6-166',81);
-- 
-- insert into  teachers (tno,tname,tsex,tbirthday, prof,depart) values(804,'李诚','男','1958-12-02','副教授','计算机系');
-- insert into  teachers (tno,tname,tsex,tbirthday, prof,depart) values(856,'张旭','男','1969-03-12','讲师','电子工程系');
-- insert into  teachers (tno,tname,tsex,tbirthday, prof,depart) values(825,'王萍','女','1972-05-05','助教','计算机系');
-- insert into  teachers (tno,tname,tsex,tbirthday, prof,depart) values(831,'刘冰','女','1977-08-14','助教','电子工程系');
-- 

-- 简单难度:
-- 1、 查询 students 表中的所有记录的 sname、ssex 和 class 列。
-- select sname,ssex,class from students;

-- 2、 查询教师所有的单位即不重复的 depart 列。
-- select distinct depart from teachers;

-- 3、 查询 students 表的所有记录。
-- select * from students;

-- 4、 查询scores 表中成绩在 60 到 80 之间的所有记录。
-- select * from scores where degree between 60 and 80;

-- 5、 查询 scores  表中成绩为 85，86 或 88 的记录。
-- select * from scores where degree in (85,86,88);

-- 6、 查询students 表中“95031”班或性别为“女”的同学记录。
-- select * from students where class='95031' or ssex='女';

-- 7、 以 class 降序查询students  表的所有记录。
-- select * from students order by class desc;

-- 8、 以  cno 升序、  degree   降序查询 scores表的所有记录。
-- select * from scores order by cno asc,degree desc;

-- 9、 查询“95031”班的学生人数。
-- select count(*) from students where class='95031';

-- 10、查询 scores 表中的最高分的学生学号和课程号。
-- select sno,cno from scores 
-- where degree=(select max(degree) from scores);

-- 11、查询‘3-105’号课程的平均分。
-- select avg(degree) from scores where cno='3-105';

-- 12、查询 students  表中不姓“王”的同学记录。 
-- select * from students where sname not like '王%';

-- 13、查询 students 表中最大和最小的 sbirthday 日期值。
-- select max(sbirthday),min(sbirthday) from students;

-- 14、以班号和年龄从大到小的顺序查询 students 表中的全部记录。
-- select * from students order by class desc, sbirthday asc;

-- 中等难度:
-- 15、查询至少有 2名男生的班号。
-- select class from students 
-- where ssex='男' 
-- group by class having count(*)>=2;

-- 16、查询 scores 表中至少有 5 名学生选修的
--     并以 3 开头的课程的平均分数。
-- select cno,avg(degree) from scores
-- where cno like '3%'
-- group by cno having count(*)>=5;

-- 17、查询最低分大于70，最高分小于90 的 sno列。
-- select sno from scores
-- group by sno having min(degree)>70 and max(degree)<90;

-- 18、查询所有学生的sname、cno 和degree列。
-- select sname,cno,degree from students s
-- join scores sc on s.sno=sc.sno;

-- 19、查询所有学生的 sno 、cname 和degree 列。
-- select sno,cname,degree from courses c
-- join scores sc on c.cno=sc.cno;

-- 20、查询95033班所选课程的平均分。
-- select class,cno,avg(degree) from students s
-- join scores sc on s.sno=sc.sno
-- where class='95033' 
-- group by cno;

-- 子查询
-- select cno,avg(degree) from scores 
-- where sno in (select sno from students where class='95033')
-- group by cno;

-- 21、查询95033班和 95031 班全体学生的记录。
-- select * from students where class in (95033,95031);

-- 22、查询存在有 85分以上成绩的课程cno.
-- select distinct cno from scores where degree>85;

-- 23、查询“男”教师及其所上的课程。
-- select tsex, tname, cname from teachers t
-- join courses c on t.tno=c.tno
-- where tsex='男';

-- 24、查询最高分同学的sno、cno和degree列。
-- select * from scores 
-- where degree=(select max(degree) from scores);

-- 25、查询和“李军”同性别的所有同学的sname.
-- select sname from students
-- where ssex=(select ssex from students where sname='李军');

-- 26、查询和“李军”同性别并同班的同学sname.
-- select sname from students
-- where (ssex,class)=(select ssex,class from students where sname='李军');

-- 27、查询所有任课教师的tname和depart. (没代课的不统计)
-- select tname,depart from teachers t
-- join courses c on t.tno=c.tno;

-- 28、查询所有未讲课的教师的tname和depart.
-- select tname,depart from teachers t
-- left join courses c on t.tno=c.tno
-- where cno is null;


-- 高等难度:
-- 29、查询“李诚“教师任课的学生成绩。
-- select tname, sno, cname, degree from teachers t
-- join courses c on t.tno=c.tno
-- join scores sc on sc.cno=c.cno
-- where tname='李诚';

-- 30、查询选修某课程的同学人数多于 5 人的教师姓名。
-- select tname,c.cno,count(*) from teachers t
-- join courses c on t.tno=c.tno
-- join scores sc on sc.cno=c.cno
-- group by cno having count(*)>5;

-- 31、查询出“计算机系“教师所教课程的成绩表。
-- select depart,tname,sc.* from teachers t
-- join courses c on t.tno=c.tno
-- join scores sc on sc.cno=c.cno
-- where depart='计算机系';

-- 32、查询所有教师和同学的name、sex 和 birthday. (使用 union    )
-- select tname,tsex,tbirthday from teachers
-- UNION
-- select sname,ssex,sbirthday from students;

-- 33、查询所有“女”教师和“女”同学的 name 、sex 和 birthday. . (使用 union        )
-- select tname,tsex,tbirthday from teachers where tsex='女'
-- UNION
-- select sname,ssex,sbirthday from students where ssex='女';

-- 34、查询所有学生的 sname  、 cname   和  degree   列。
-- select sname,cname,degree from students s
-- join scores sc on sc.sno=s.sno
-- join courses c on c.cno=sc.cno;

-- *35、查询 scores 中选学一门以上课程的同学中分数为非最高分成绩的记录。
-- select sno,max(degree),count(*) from scores group by sno having count(*)>1;

select * from scores 
where (sno, degree) not in
(select sno,max(degree) from scores group by sno 
having count(*)>1);





