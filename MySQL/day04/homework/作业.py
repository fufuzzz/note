from QFSQL import QFSQL

qf_sql = QFSQL(password='201314', database='mydb3')

# -- 作业:
# -- 1.查询所有学生信息
# print(qf_sql.search('select * from tb_student'))
#
# -- 2.查询所有课程名称及学分
# print(qf_sql.search('select couname "课程名",coucredit "学分" from tb_course'))

# -- 3.查询所有学生的姓名和性别
# print(qf_sql.search('select stuname,stusex from tb_student'))

# -- 4.查询所有女学生的姓名和出生日期
# print(qf_sql.search('select stuname,stubirth from tb_student where stusex = 0'))
#
# # -- 5.查询所有80后学生的姓名、性别和出生日期
# print(qf_sql.search('select stuname,stusex,stubirth from tb_student where stubirth like "__8%"'))

# -- 6.查询姓"杨"的学生姓名和性别
# print(qf_sql.search('select stuname,stusex from tb_student where stuname like "杨%"'))

# -- 7.查询姓"杨"名字两个字的学生姓名和性别
# print(qf_sql.search('select stuname,stusex from tb_student where stuname like "杨_"'))
#
# # -- 8.查询姓"杨"名字三个字的学生姓名和性别
# print(qf_sql.search('select stuname,stusex from tb_student where stuname like "杨__"'))
#
# # -- 9.查询名字中有"不"字或"嫣"字的学生的姓名
# print(qf_sql.search('select stuname from tb_student where stuname like "%不%" or stuname like "%嫣%"'))

# -- 10.查询没有录入家庭住址的学生姓名
# print(qf_sql.search('select stuname from tb_student where stuaddr is null'))
#
# # -- 11.查询录入了家庭住址的学生姓名
# print(qf_sql.search('select stuname from tb_student where stuaddr is not null'))
#
# # -- 12.查询学生选课的所有日期
# print(qf_sql.search('select seldate from tb_record'))
# # -- 13.查询学生的家庭住址
# print(qf_sql.search('select stuname,stuaddr from tb_student'))
# # -- 14.查询男学生的生日按年龄从大到小排列
# print(qf_sql.search('select * from tb_student where stusex=1 order by stubirth'))
#
# # -- 15.查询年龄最大的学生的出生日期
# print(qf_sql.search('select min(stubirth) from tb_student order by stubirth'))
#
# # -- 16.查询年龄最小的学生的出生日期
# print(qf_sql.search('select max(stubirth) from tb_student order by stubirth'))
#
# # -- 17.分别查询男学生和女学生的人数
# print(qf_sql.search('select stusex,count(*) from tb_student group by stusex'))
#
# # -- 18.查询课程编号为1111的课程的平均成绩
# print(qf_sql.search('select avg(score) from tb_record where cid=1111'))
#
# # -- 19.查询学号为1001的学生所有课程的平均分
# print(qf_sql.search('select avg(score) from tb_record where sid=1001'))
#
# # -- 20.查询每个学生的学号和平均成绩
# print(qf_sql.search('select sid,avg(score) from tb_record group by sid;'))
#
# # -- 21.查询平均成绩大于等于90分的学生的学号和平均成绩
# print(qf_sql.search('select sid,avg(score) from tb_record group by sid having avg(score)>=90;'))
#
# # -- 22.查询年龄最大的学生的姓名
# print(qf_sql.search('select stuname from tb_student where stubirth=(select min(stubirth) from tb_student)'))
#
# # -- 23.查询选了两门以上的课程的学生姓名
# print(qf_sql.search(
#     'select stuname from tb_student st join tb_record re on st.stuid=re.sid group by sid having count(*)>2;'))
#
# # -- 24.查询学生姓名、课程名称以及成绩
# print(qf_sql.search(
#     'select stuname,couname,score from tb_student st join tb_record re on st.stuid=re.sid join tb_course cou on re.cid=cou.couid'))
#
# # -- 25.查询学生姓名、课程名称以及成绩按成绩从高到低查询第11-15条记录
print(qf_sql.search('select stuname,couname,score from tb_student st '
                    'join tb_record re on st.stuid=re.sid '
                    'join tb_course cou on re.cid=cou.couid '
                    'order by score desc '
                    'limit 11,5;'))
# -- 26.查询每个学生的姓名和选课数量
print(qf_sql.search(
    'select stuname,count(*) from tb_student st join tb_record re on st.stuid=re.sid group by sid;'))
