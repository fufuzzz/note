import pymysql

# 使用类封装
#    属性
#
#    方法:
#       增: 添加一个部门,自己扩展写一个添加一个员工的方法
#       删: 删除一个部门,自己扩展写一个删除一个员工的方法
#       改: 修改一个部门,自己扩展写一个更新一个员工的方法
#       查: 查询所有部门,自己扩展写一个查询员工的方法
#       分页查询: limt
from pymysql.cursors import DictCursor


class Employee:
    # 初始化方法
    def __init__(self, host='localhost', port=3306, user='root', password='', database='', charset='utf8mb4'):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)


    # 析构函数
    def __del__(self):
        # 关闭连接
        self.db.close()

    # 增: 添加一个部门
    def add_dept(self, dno, dname, dloc):
        try:
            with self.db.cursor() as cur:
                # sql: 添加一个部门
                sql = f'insert into tb_dept values({dno}, "{dname}", "{dloc}")'
                cur.execute(sql)
            # 提交
            self.db.commit()
        except Exception as e:
            print(f'插入失败: {e}')
            self.db.rollback() # 回滚

    # 删: 删除一个部门
    def del_dept(self, dno):
        try:
            with self.db.cursor() as cur:
                cur.execute(f'delete from tb_dept where dno={dno}')
            self.db.commit()
        except Exception as e:
            print(f'删除失败: {e}')
            self.db.rollback()

    # 改: 修改一个部门
    def update_dept(self, dno, dname, dloc):
        try:
            with self.db.cursor() as cur:
                cur.execute(f'update tb_dept set dname="{dname}", dloc="{dloc}" where dno={dno}')
            self.db.commit()
        except Exception as e:
            print(f'修改失败: {e}')
            self.db.rollback()

    # 查: 获取一个部门
    def get_dept_one(self, dno):
        with self.db.cursor() as cur:
            cur.execute(f'select * from tb_dept where dno={dno}')
            return cur.fetchone()

    # 查: 获取所有部门
    def get_dept_all(self):
        with self.db.cursor(DictCursor) as cur:  # DictCursor 字典
            cur.execute(f'select * from tb_dept')
            return cur.fetchall()
    # 查: 分页查询
    def get_emp_page(self, page=1, per_page=5):
        '''
        :param page:  页码, 默认获取第一页
        :param per_page:  每一页的数据量, 默认每页5条数据
        :return: 返回指定页码的数据
        '''
        with self.db.cursor(DictCursor) as cur:
            cur.execute(f'select * from tb_emp limit {(page-1)*per_page}, {per_page} ')
            return cur.fetchall()


if __name__ == '__main__':
    # 创建对象
    emp = Employee(password='201314', database='mydb3')

    # emp.add_dept(60, '网络部', '深圳')  # 添加一个部门
    # emp.del_dept(60)
    # emp.update_dept(50, '财务部', '上海')
    # print(emp.get_dept_one(10))
    # print(emp.get_dept_all())
    page = int(input('输入想查找的第几页:'))
    list1 = emp.get_emp_page(page)
    # list2 = emp.get_emp_page(2)
    for row in list1:
        print(row['ename'], end=' ')