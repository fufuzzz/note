
# 	班级类：班级名称、学生列表
# 		显示所有学生(方法)
# 		根据学号查找学生(方法)
# 		添加一个学生(方法)
# 		删除一个学生（学生对象、学号）(方法)
# 		根据学号升序排序(方法)
# 		根据成绩降序排序(方法)

class Class:
    def __init__(self, name, stu_list):
        self.name = name
        self.stu_list = stu_list

    # 显示所有学生(方法)
    def show_stu(self):
        for stu in self.stu_list:
            print(stu.__dict__)

    # 根据学号查找学生(方法)
    def find_by_sno(self, sno):
        for stu in self.stu_list:
            if stu.stuno == sno:
                print(stu.__dict__)
                return stu

    # 添加一个学生(方法)
    def add_stu(self, stu):
        self.stu_list.append(stu)

    # 删除一个学生（学生对象、学号）(方法)
    def del_stu(self, sno):
        for stu in self.stu_list:
            if stu.stuno == sno:
                self.stu_list.remove(stu)
                break

    # 根据学号升序排序(方法)
    def dsc_stu(self, sno):
        self.stu_list.sort(key=lambda x: x.stuno)

    # 根据成绩降序排序(方法)
    def nec_stu(self, score):
        self.stu_list.sort(key=lambda x: x.score)
