-- create table star( 
-- 	id int auto_increment, 
-- 	name varchar(50) not null, 
-- 	money float not null , 
-- 	province varchar(20) default null , 
-- 	age tinyint unsigned not null , 
-- 	sex tinyint not null , 
-- 	primary key (id) 
-- ) engine= InnoDB default charset=utf8;

-- insert into star(name,money,province,age,sex) values('刘一',100,"北京",10,1);
-- insert into star(name,money,province,age,sex) values('陈二',200,"北京",20,1);
-- insert into star(name,money,province,age,sex) values('张三',300,"北京",30,1);
-- insert into star(name,money,province,age,sex) values('李四',400,"深圳",40,1);
-- insert into star(name,money,province,age,sex) values('王五',500,"深圳",50,1);
-- insert into star(name,money,province,age,sex) values('赵六',100,"深圳",60,0);
-- insert into star(name,money,province,age,sex) values('孙七',100,"上海",70,0);
-- insert into star(name,money,province,age,sex) values('周八',100,"上海",80,0);
-- insert into star(name,money,province,age,sex) values('吴九',100,"上海",90,0);
-- insert into star(name,money,province,age,sex) values('郑十',100,"广州",100,0);
select * from star;

-- 要求：
-- 1, 根据表结构使用sql语句创建star表 
-- 2, 给star表随机插入多条数据 
-- 3, 在star表中找出年龄大于30的明星 
-- 4, 查出每个省份的明星个数(分组) 
-- 5, 找到明星个数大于1的省份 
-- 6, 找到明星个数第二多的省份及个数(没有重复个数） 
-- 7. 第6题考虑如有多个第1和第2多的省份。 
-- select province, count(*) from star 
-- group by province 
-- having count(*)=(select distinct count(*) from star group by province order by count(*) desc limit 1,1);






-- 插入数据 
-- INSERT INTO category(name) values('水果'),('零食'),('饮料'),('牛奶'),('饼干'),('生活用品'); 
-- INSERT INTO goods(name, price, categoryid) values('苹果', 2, 1),('香蕉', 3, 1),('梨子', 4.5, 1),('口 香糖', 5, 2),('泡泡堂', 3, 2),('可乐', 3, 3),('红牛', 6, 3),('娃哈哈', 3, 4),('特仑苏', 8, 4),('益力多', 2, 4);
select * from category;
select * from goods;

-- 要求：
-- 1, 使用sql语句创建category表和goods表,其中categoryid为外键 
-- 2, 找出所有分类 
-- 3, 找出价格>=5的商品名称有哪些 
-- 4, 找出分类名称为‘水果’的所有商品 
-- 5, 找出泡泡堂商品所属的分类名称 
-- 6, 找出每个分类的分类名称及分类的商品数量 
-- 7, 将所有商品按价格降序排列 
-- 8, 找出每个分类的名称及分类的商品数量，并按商品数量降序排列 
-- 9, 找出比'娃哈哈'价格低的商品 
-- 10, 找出比平均价格低的商品 
-- 11, 列出分类名称和这些分类的商品信息，同时也列出那些没有商品的分类







