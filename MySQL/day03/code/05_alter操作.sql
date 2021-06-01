-- 创建表
-- create table person(
-- 	id int auto_increment,
-- 	name varchar(20),
-- 	age int,
-- 	sex varchar(10),
-- 	primary key(id)
-- );

-- desc person;

-- alter操作
-- 1.修改表名
-- alter table person rename person2;
-- show tables;

-- 2.修改字段的数据类型
-- alter table person2 modify sex tinyint;
-- desc person2;

-- 3.修改字段名
-- alter table person2 change sex gender int;
-- desc person2;

-- 4.添加字段
-- alter table person2 add qq varchar(20);
-- alter table person2 add address varchar(200) first;
-- alter table person2 add wechat varchar(200) after name;
-- desc person2;

-- 5.删除字段
-- alter table person2 drop address;
-- desc person2;

-- 6.修改字段的位置
-- alter table person2 modify wechat varchar(200) after gender;
-- desc person2;

-- 7.删除表的外键约束
-- alter table person2 drop foreign key dept_fk_1;
-- desc person2;

-- 8.删除数据表
-- drop table person2;















