#
# 1. 利用封装和继承的特性完成如下操作：
# 	小学生：
# 		属性：
# 			姓名
# 			学号
# 			年龄
# 			性别
# 		行为：
# 			学习
# 			打架
# 	中学生：
# 		属性：
# 			姓名
# 			学号
# 			年龄
# 			性别
# 		行为：
# 			学习
# 			谈恋爱
# 	大学生：
# 		属性：
# 			姓名
# 			学号
# 			年龄
# 			性别
# 		行为：
# 			学习
# 			打游戏
#
# 	调用：
# 		创建小学生对象
# 			调用学习的方法
# 				打印内容为： xx 学习的内容为：语文 数学 英语
# 		创建中学生对象
# 			调用学习的方法
# 				打印内容为：xx 学习的内容为：语数外 生物化 史地政
# 		创建大学生对象
# 			调用学习的方法：
# 				打印内容为： 逃课中。。。


'''
class Student:
    def __init__(self, name, num, age, sex):
        self.name = name
        self.num = num
        self.age = age
        self.sex = sex

    def study(self, content):
        print('学习')


class Pupil(Student):
    def __init__(self, name, num, age, sex):
        Student.__init__(self, name, num, age, sex)

    def study(self, content):
        print(f'{self.name}学习的内容为:{content}')

    def fight(self):
        print(f'{self.name}打架')


class Middle(Student):
    def __init__(self, name, num, age, sex):
        Student.__init__(self, name, num, age, sex)

    def study(self, content):
        print(f'{self.name}学习的内容为:{content}')

    def love(self):
        print(f'{self.name}谈恋爱')


class College(Student):
    def __init__(self, name, num, age, sex):
        super().__init__(name, num, age, sex)

    def play(self):
        print(f'{self.name}打游戏')

    def study(self, content):
        print(content)


pupil = Pupil('游远东', '8787', '6', '男')
pupil.study('语文 数学 英语')

middle = Middle('游远东', '7878', '15', '男')
middle.study('语数外 生物化 史地政')

college = College('游远东', '7979', '19', '男')
college.study('逃课中...')

'''
# 2.主人杨夫人 向客人 李小姐介绍自己家的宠物狗和宠物猫
# 		宠物狗：
# 			昵称是：贝贝
# 			年龄是：2
# 			性别：雌
# 			会两条腿行走的才艺
# 		宠物猫:
# 			昵称是：花花
# 			年龄是 1
# 			性别是：雄
# 			会装死的才艺
'''
class Pets:
    def __init__(self, name, age, sex, skill):
        self.name = name
        self.age = age
        self.sex = sex
        self.skill = skill


class Dog(Pets):
    type = '宠物狗'

    def __init__(self, name, age, sex, skill):
        super().__init__(name, age, sex, skill)


class Cat(Pets):
    type = '宠物猫'

    def __init__(self, name, age, sex, skill):
        super().__init__(name, age, sex, skill)


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self, kname):
        print(f'主人{self.name}向客人{kname.name}介绍自己家的{Dog.type}和{Cat.type}')
        print(f'{Dog.type}:\n\t昵称是:{dog.name}\n\t年龄是:{dog.age}\n\t性别是:{dog.sex}会{dog.skill}的才艺')
        print(f'{Cat.type}:\n\t昵称是:{cat.name}\n\t年龄是:{cat.age}\n\t性别是:{cat.sex}会{cat.skill}的才艺')


dog = Dog('贝贝', '2', '雌', '两条腿行走')
cat = Cat('花花', '1', '雄', '装死')
yang = Person('杨夫人')
li = Person('李夫人')
yang.introduce(li)
'''

# 3.
# 	学生类：姓名、年龄、学号、成绩
# 	班级类：班级名称、学生列表
# 		显示所有学生(方法)
# 		根据学号查找学生(方法)
# 		添加一个学生(方法)
# 		删除一个学生（学生对象、学号）(方法)
# 		根据学号升序排序(方法)
# 		根据成绩降序排序(方法)
#

# 提示:
'''
class Student:
    def __init__(self, name, age, num, score):
        self.name = name
        self.age = age
        self.num = num
        self.score = score


class Class:
    def __init__(self, name, stu_list):
        self.name = name
        self.stu_list = stu_list

    def display(self):
        for n in self.stu_list:
            print(f'学生姓名:{n.name},年龄:{n.age},学号:{n.num},成绩:{n.score}')

    def serch_num(self, num):
        for n in self.stu_list:
            if num == n.num:
                print(f'{num}学号的学生姓名:{n.name},年龄:{n.age},成绩:{n.score}')

    def insert_stu(self, stu):
        self.stu_list.append(stu)
        print(f'增加了 {stu.name} 后的学生信息如下')
        self.display()

    def delete_stu(self, stu):  # 按照学生对象删除
        self.stu_list.remove(stu)
        print(f'删除 {stu.name} 后的学生信息如下:')
        self.display()

    def delete_stu_num(self, dnum):  # 按照学号删除
        for n in self.stu_list:
            if dnum == n.num:
                self.stu_list.remove(n)
        print(f'删除 学号是{dnum}的学生 后的学生信息如下:')
        self.display()

    def sort_num(self):
        self.stu_list.sort(key=lambda x: x.num)
        print(f'按照学号升序排序后')
        self.display()

    def sort_score(self):  # 方法一
        self.stu_list.sort(reverse=True, key=lambda x: x.score)
        print('方法一按照成绩降序排序后')
        self.display()

    def sort_score2(self):  # 方法二
        for i in range(len(self.stu_list) - 1):
            for j in range(i, len(self.stu_list) - 1 - i):
                if self.stu_list[j].score < self.stu_list[j + 1].score:
                    self.stu_list[j], self.stu_list[j + 1] = self.stu_list[j + 1], self.stu_list[j]

        return self.stu_list


stu1 = Student('游远东', '21', '2017101883', 100)
stu2 = Student('张三', '22', '2017101882', 60)
stu3 = Student('李四', '23', '2017101881', 40)
stu4 = Student('王五', '24', '2017101880', 90)
stu5 = Student('王陆', '20', '2017101884', 80)
stu6 = Student('大司马', '30', '2017101889', 0)
c = Class('三年一班', [stu1, stu2, stu3, stu4, stu5])
c.display()
print('-' * 60)
c.serch_num('2017101883')
print('-' * 60)
c.insert_stu(stu6)
print('-' * 60)
c.delete_stu(stu5)  # 按照学生对象删除
print('-' * 60)
c.delete_stu_num('2017101880')  # 按照学生学号删除
print('-' * 60)
c.sort_num()
print('-' * 60)
c.sort_score()  # 成绩排序方法一
print('-' * 60)
# c.sort_score2()  # 成绩排序方法二
# d = Class('三年一班', c.sort_score2())
# d.display()

'''

from grade import Class
from student import Student
import random

# 创建对象
# 创建学生
stu_list = []
for i in range(1, 11):
    name = f'杰伦{i}'
    age = random.randint(10, 40)
    stuno = random.randint(1, 100000)
    score = random.randint(10, 100)

    stu = Student(name, age, stuno, score)
    stu_list.append(stu)


print('*' * 60)
cls = Class('三年二班', stu_list)
cls.show_stu()
