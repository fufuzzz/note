
-- 主键约束 PRIMARY KEY

-- create table stu1(
-- 	id int primary key,
-- 	name varchar(20)
-- );
-- desc stu1;

-- create table stu2(
-- 	id int,
-- 	name varchar(20),
-- 	primary key(id, name)
-- );
-- desc stu2;

-- insert into stu2 values(1,'a'),(1,'b');
-- select * from stu2;

-- 不推荐
-- create table stu3(
-- 	id int,
-- 	name varchar(20)
-- );
-- desc stu3;
-- alter table stu3 add constraint stu3_id primary key(id);
-- 

-- 唯一约束 unique
-- 主键: primary key
-- 自动增长: auto_increment
-- 默认值: default
-- 非空: not null 
-- 注释: comment
-- create table if not exists user(
-- 	id int primary key auto_increment comment 'ID',
-- 	name varchar(20) unique comment '姓名',
-- 	age int default 18 comment '年龄',
-- 	sex varchar(10) not null comment '性别',
-- 	height float comment '身高'
-- );
-- desc user;
-- 
-- insert into user(name, sex) values('张三', '女');
-- select * from user;


-- 外键约束
-- #创建表
-- #学生表
-- create table student2(
-- 		stuid varchar(10) primary key,
--  	stuname varchar(50)
-- );
-- 
-- #成绩表
-- create table score2(
-- 	stuid varchar(10),
-- 	score int,
-- 	courseid int
-- );
--    
-- #插入数据
-- insert into student2 values('1001','zhangsan');
-- insert into student2 values('1002','xiaoming');
-- insert into student2 values('1003','jack');
-- insert into student2 values('1004','tom');
-- 
-- insert into score2 values('1001',98,1);
-- insert into score2 values('1002',95,1);
-- insert into score2 values('1003',67,2);
-- insert into score2 values('1004',83,2);
-- insert into score2 values('1004',70,1);


-- select * from student2;
-- select * from score2;
-- 
-- -- insert into score2 values(1005, 100, 1);
-- 
-- -- 添加外键约束foreign key
-- -- 先删除上面添加的1005的数据,再运行
-- alter table score2 add constraint score2_student2_stuid foreign key(stuid) references student2(stuid);
-- insert into score2 values(1006, 100, 1);


# 学生表
create table student3(
	stuid varchar(10) primary key,
 	stuname varchar(50)
);

# 成绩表
create table score3(
	stuid varchar(10),
	score int,
	courseid int,
	foreign key(stuid) references student3(stuid)
);







