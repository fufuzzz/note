''''''

'''



3.操作
增删改:
try:
    with db.cursor() as cur:
        # 增:插入数据
        cur.execute('insert into tb_dept(dno,dname,dloc) values (80,"公关部","深圳")')
        # 删: 删除数据
        cur.execute('delete from tb_dept where dno=80')
        # 改: 修改数据
        cur.execute('update tb_dept set dloc='南山' where dno=80')
    
    # 提交
    db.commit()
except Exception as e:
    print(f'操作失败:{e}')
    # 回滚
    db.rollback()

# 查询
# DictCursor
with db.cursor(DictCursor) as cur:
    cur.execute('select * from tb_dept')
    print(cur.fetchall())
    print(cur.fetchone())
    print(cur.fetchmany())
'''