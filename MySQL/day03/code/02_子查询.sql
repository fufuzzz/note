-- # 员工表
-- create table emp2(empno int primary key, enname varchar(20), job varchar(20), mgr int, hiredate date, sal double, comm double, deptno int);
-- 
-- # 添加数据
-- insert into emp2 values(7369,'smith','clark',7902,'1980-12-17',800,null,20);
-- insert into emp2 values(7499,'allen','salesman',7698,'1981-02-20',1600,300,30);
-- insert into emp2 values(7521,'ward','salesman',7698,'1981-02-22',1250,500,30);
-- insert into emp2 values(7566,'jones','managen',7839,'1981-04-02',2975,null,30);
-- insert into emp2 values(7654,'martin','salesman',7698,'1981-09-28',1250,1400,30);
-- insert into emp2 values(7698,'blake','manager',7839,'1981-05-01',2850,null,30);
-- insert into emp2 values(7782,'clark','manageer',7839,'1980-06-17',2450,null,10);
-- insert into emp2 values(7788,'scott','analyst',7566,'1987-02-20',3000,null,20);
-- insert into emp2 values(7839,'king','president',null,'1987-02-20',5000,null,10);

select * from emp2;

# 1.查询和scott在同一个部门的员工
select * from emp2 
where deptno=(select deptno from emp2 where enname='scott')
and enname!='scott';

# 2.查询工资高于jones的员工信息
select * from emp2
where sal>(select sal from emp2 where enname='jones');

# 3.查询工资高于30号部门所有人的员工信息
select * from emp2
where sal>(select max(sal) from emp2 where deptno=30);

# 4.查询工作类型和工资与martin完全相同的员工信息
select * from emp2
where (job,sal)=(select job,sal from emp2 where enname='martin')
and enname!='martin';



