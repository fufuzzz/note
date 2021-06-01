import pymysql
from pymysql.cursors import DictCursor


class QFSQL:
    # 连接MySQL
    def __init__(self, host='localhost', port=3306, user='root', password='', database='', charset='utf8mb4'):
        self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database,
                                  charset=charset, autocommit=True)  # 自动提交

    # 关闭MySQL连接
    def __del__(self):
        self.db.close()

    # 增
    def insert(self, sql):
        self.__edit(sql)

    # 删
    def delete(self, sql):
        return self.__edit(sql)

    # 改
    def update(self, sql):
        return self.__edit(sql)

    # 封装: 增删改操作
    def __edit(self, sql):
        try:
            with self.db.cursor() as cur:
                cur.execute(sql)
            # self.db.commit()
        except Exception as e:
            print(f'操作失败: {e}')
            self.db.rollback()
        else:
            return True

    # 查
    def search(self, sql):
        try:
            with self.db.cursor(DictCursor) as cur:
                cur.execute(sql)
                return cur.fetchall()
        except Exception as e:
            print(f'查询失败:{e}')

    # 分页
    def search_by_page(self, table_name, page=1, per_page=5):
        try:
            with self.db.cursor(DictCursor) as cur:
                cur.execute(f'select * from {table_name} limit {(page - 1) * per_page}, {per_page}')
                return cur.fetchall()
        except Exception as e:
            print(f'查询失败:{e}')
