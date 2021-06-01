from QFSQL import QFSQL

# 创建qfsql对象
qf_sql = QFSQL(password='201314', database='mydb3')

# 插入数据
# n = qf_sql.insert('insert into tb_dept values (60, "人事部", "西部硅谷")')
# 删除数据
# n = qf_sql.delete('delete from tb_dept where dno = 60')
# 修改数据
# n = qf_sql.update('update tb_dept set dname="网络部" where dno=50')
# if n:
#     print('success')
# else:
#     print('fial')

# 查
# result = qf_sql.search('select * from tb_dept')
# print(result)

# 分页查询
# result = qf_sql.search_by_page("tb_emp", 1, 5)
# for row in result:
#     print(row['ename'])
