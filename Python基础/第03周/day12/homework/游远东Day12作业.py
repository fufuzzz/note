''''''

''' 基础题 '''


# 利用面向对象的思想写下面的程序：直接赋值
# 1.小美在朝阳公园溜旺财【注：旺财是狗】
class Person1:
    def __init__(self, name):
        self.name = name

    def walk_dog(self, place, dog):
        print(f'{self.name}在{place}溜{dog}')


xm = Person1('小美')
xm.walk_dog("朝阳公园", '旺财')


# 2.小明穿着白色的特步运动鞋在奥林匹克公园跑步
class Person2:
    def __init__(self, name, shoes):
        self.name = name
        self.shoes = shoes

    def run_park(self, run):
        print(f'{self.name}穿着{self.shoes}在奥利匹克公园{run}')


ming = Person2('小明', '白色的特步运动鞋')
ming.run_park('跑步')


# 3.赵老师在讲台上讲课，小刚认真的听课做笔记
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach_platform(self, teach):
        print(f'{self.name}在讲台上{teach}')


class Student:
    def __init__(self, name):
        self.name = name

    def listen_serious(self, work):
        print(f'{self.name}认真的{work}')


zhao = Teacher('赵老师')
zhao.teach_platform('讲课')

gang = Student('小刚')
gang.listen_serious('听课做笔记')


# 4.张阿姨和李阿姨在物美超市买红富士
# 提示: 写一个阿姨类,创建2个阿姨对象
class Aunt:
    def __init__(self, name):
        self.name = name

    def shop_supermarket(self, shop):
        print(f'{self.name}在物美超市{shop}')


zhang = Aunt('张阿姨')
li = Aunt('李阿姨')
zhang.shop_supermarket('买红富士')
li.shop_supermarket('买红富士')

''' 进阶题 '''


# 1.李晓在家里开party，向朋友介绍家中的黄色的宠物狗【彩彩】具有两条腿走路的特异功能。
class Person11:
    def __init__(self, name):
        self.name = name

    def party_home(self, party):
        return f'{self.name}在家{party}'

    def introduce_dog(self, dog):
        return f'向朋友介绍家中的{dog.color}的{dog.sort}{dog.name}具有{dog.function}的特异功能'


class Dog:
    def __init__(self, name, color, sort, function):
        self.name = name
        self.color = color
        self.sort = sort
        self.function = function


lixiao = Person11('李晓')
caicai = Dog('彩彩', '黄色', '宠物狗', '两条腿走路')
print(lixiao.party_home('开party') + ',' + lixiao.introduce_dog(caicai))


# 2.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
class Person22:
    def __init__(self, name, pig):
        self.name = name
        self.pig = pig

    def find_pig(self, mood):
        print(f'{self.name}的{self.pig.sort}{self.pig.name}跑丢了,她{mood}贴寻猪启示')


class Pig:
    def __init__(self, sort, name):
        self.name = name
        self.sort = sort


benben = Pig('荷兰宠物猪', '笨笨')
wang = Person22('王阿姨', benben)
wang.find_pig('哭着')


# 3.富二代张三向女朋友李四介绍自己的新跑车：白色的宾利
class Rich2:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def introduce_car_girl(self, gname):
        return f'富二代{self.name}向女朋友{gname}介绍自己的新跑车:{self.car.color}的{self.car.brand}'


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


car1 = Car('宾利', '白色')
zsan = Rich2('张三', car1)

print(zsan.introduce_car_girl('李四'))

''' 挑战题 '''

# 使用构造函数的方式写下面的程序
# 1.定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
# 圆:
#   属性: 半径,圆心
#   方法: 周长,面积
# 点:
#   属性: x,y

import math


class Circle:
    def __init__(self, r, center):
        self.r = r
        self.center = center

    def circumference(self):
        return 2 * self.r * math.pi

    def area(self):
        return math.pi * (self.r ** 2)

    def judge(self, point):
        if (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 == self.r ** 2:
            print(f'({point.x},{point.y})在圆上')
        elif (point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2 < self.r ** 2:
            print(f'({point.x},{point.y})在圆内')
        else:
            print(f'({point.x},{point.y})在圆外')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


center2 = Point(2, 2)
point = Point(2, 2)
circle1 = Circle(2, center2)
print('圆的周长是:', circle1.circumference())
print('圆的面积是:', circle1.area())

circle1.judge(point)
