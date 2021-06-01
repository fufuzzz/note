-- -- 部门表
-- create table dept(
-- 		deptno int primary key auto_increment, -- 部门编号
-- 		dname varchar(14) ,	  -- 部门名字
-- 		loc varchar(13)   -- 地址
-- ) ;
-- -- 员工表
-- create table emp(
-- 		empno int primary key auto_increment,-- 员工编号
-- 		ename varchar(10), -- 员工姓名										-
-- 		job varchar(9),	-- 岗位
-- 		mgr int,	 -- 直接领导编号
-- 		hiredate date, -- 雇佣日期，入职日期
-- 		sal int, -- 薪水/工资
-- 		comm int,  -- 提成
-- 		deptno int not null, -- 部门编号
-- 		foreign key (deptno) references dept(deptno)
-- );
-- 
-- insert into dept values(10,'财务部','北京');
-- insert into dept values(20,'研发部','上海');
-- insert into dept values(30,'销售部','广州');
-- insert into dept values(40,'行政部','深圳');
-- insert into emp values(7369,'刘一','职员',7902,'1980-12-17',800,null,20);
-- insert into emp values(7499,'陈二','推销员',7698,'1981-02-20',1600,300,30);
-- insert into emp values(7521,'张三','推销员',7698,'1981-02-22',1250,500,30);
-- insert into emp values(7566,'李四','经理',7839,'1981-04-02',2975,null,20);
-- insert into emp values(7654,'王五','推销员',7698,'1981-09-28',1250,1400,30);
-- insert into emp values(7698,'赵六','经理',7839,'1981-05-01',2850,null,30);
-- insert into emp values(7782,'孙七','经理',7839,'1981-06-09',2450,null,10);
-- insert into emp values(7788,'周八','分析师',7566,'1987-06-13',3000,null,20);
-- insert into emp values(7839,'吴九','总裁',null,'1981-11-17',5000,null,10);
-- insert into emp values(7844,'郑十','推销员',7698,'1981-09-08',1500,0,30);
-- insert into emp values(7876,'郭十一','职员',7788,'1987-06-13',1100,null,20);
-- insert into emp values(7900,'钱多多','职员',7698,'1981-12-03',950,null,30);
-- insert into emp values(7902,'大锦鲤','分析师',7566,'1981-12-03',3000,null,20);
-- insert into emp values(7934,'木有钱','职员',7782,'1983-01-23',1300,null,10);

select * from dept;
select * from emp;

-- 作业
-- 1．列出至少有一个员工的所有部门。
-- select deptno, count(*) from emp
-- group by deptno having count(*)>=1;

-- 2．列出薪金比"刘一"多的所有员工。
-- select * from emp 
-- where sal>(select sal from emp where ename='刘一');

-- *3．列出所有员工的姓名及其直接上级的姓名。(连接自己)
-- select e1.ename,e2.ename,e1.job from emp e1 
-- left join emp e2 on e1.mgr=e2.empno;

-- *4．列出受雇日期早于其直接上级的所有员工。(连接自己)
-- select * from emp e1 
-- left join emp e2 on e1.mgr=e2.empno
-- where e1.hiredate<e2.hiredate;

-- 5．列出部门名称和这些部门的员工信息，同时列出那些没有员工的部门。
-- select dname,e.* from dept d 
-- left join emp e 
-- on d.deptno=e.deptno;

-- 6．列出所有job为“职员”的姓名及其部门名称。
-- select ename,dname from dept d 
-- join emp e on d.deptno=e.deptno
-- where job='职员';

-- 7．列出最低薪金大于1500的各种工作。
-- select job from emp group by job having min(sal)>1500;

-- 8．列出在部门 "销售部" 工作的员工的姓名，假定不知道销售部的部门编号。
-- select ename from dept d join emp e on d.deptno=e.deptno
-- where dname='销售部';

-- 9．列出薪金高于公司平均薪金的所有员工。
-- select * from emp where sal>(select avg(sal) from emp);

-- 10．列出与"周八"从事相同工作的所有员工。
-- select * from emp where job=(select job from emp where ename='周八');

-- 11．列出薪金等于部门30中员工的薪金的所有员工的姓名和薪金。
-- select ename,sal from emp where sal in (select sal from emp where deptno=30);

-- 12．列出薪金高于在部门30工作的所有员工的薪金的员工姓名和薪金。
-- select ename,sal from emp where sal > (select max(sal) from emp where deptno=30);

-- 13．列出在每个部门工作的员工数量、平均工资。
-- select deptno,count(*),avg(sal) from emp group by deptno;

-- 14．列出所有员工的姓名、部门名称和工资。
-- select ename,dname,sal from dept d join emp e on d.deptno=e.deptno;

-- -- 15．列出各种工作的最低工资。
-- select job,min(sal) from emp group by job;

-- 16．列出各个部门的'经理'的最低薪金。
-- select deptno,min(sal) from emp where job='经理' group by deptno;

-- 17. 显示出薪水最高人的职位。
-- select job from emp where sal=(select max(sal) from emp);

-- 18. 查出emp表中薪水在3000以上（包括3000）的所有员工的员工号、姓名、薪水。
-- select empno,ename,sal from emp where sal>=3000;

-- 19. 查询出所有薪水在'陈二'之上的所有人员信息。
-- select * from emp where sal>(select sal from emp where ename='陈二');

-- 20.查询出emp表中部门编号为20，薪水在2000以上（不包括2000）的所有员工，
-- 显示他们的员工号，姓名以及薪水
-- select empno,ename,sal from emp where deptno=20 and sal>2000;


-- 21.查询出emp表中所有的工作种类（无重复）
-- select distinct job from emp;

-- 22.查询出所有奖金（comm）字段不为空的人员的所有信息。
-- select * from emp where comm is not null;

-- 23.查询出薪水在800到2500之间（闭区间）所有员工的信息。
--   （注：使用两种方式实现and以及between and）
-- select * from emp where sal>=800 and sal<=2500;
-- select * from emp where sal between 800 and 2500;

-- 24.查询出最早工作的那个人的名字、入职时间和薪水。
-- select ename,hiredate,sal from emp order by hiredate limit 1;

-- 25.查询出员工号为7521，7900，7782的所有员工的信息。
--  （注：使用两种方式实现，or以及in）
-- select * from emp where empno=7521 or empno=7900 or empno=7782;
-- select * from emp where empno in (7521,7900,7782);

-- 26.查询出名字中有“张”字符，并且薪水在1000以上（不包括1000）的所有员工信息。
-- select * from emp where ename like '%张%' and sal>1000;

-- 27.查询出名字第三个汉字是“多”的所有员工信息。
-- select * from emp where ename like '__多';

-- 28.将所有员工按薪水升序排序，薪水相同的按照入职时间降序排序。
-- select * from emp order by sal asc, hiredate asc;


