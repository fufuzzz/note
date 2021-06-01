# 类: 用来创建对象
#   属性: 变量, 表示特征,静态的,比如:身高,体重,姓名,性别等..
#   方法: 函数, 表示功能, 动态的, 比如: 吃饭,睡觉,跑步等

# 类
# object: Python提供的类, 基类/父类, 超类/根类
# class Person(object):
class Person:
    # 类属性
    # name = '华晨宇'
    # age = 31

    # 对象属性: 成员属性
    # __init__(): 初始化方法/构造方法, 魔法方法/魔术方法
    #   1.在创建对象时会被自动调用
    #   2.作用: 用来初始化属性
    def __init__(self, name, age):
        # print(f'__init__(): {id(self)}')
        # 对象属性
        # 左边的name是属性名
        self.name = name
        self.age = age

    # 方法
    # self:
    #   1.self不是关键字,但是建议写成self
    #   2.不用给self传值
    #   3.self是指向当前类的对象: 谁调用当前函数,self就是谁
    #   4.作用: 用来调用类当中的其他方法或类中的属性

    def sing(self, song):
        print(f'sing(): {id(self)}')
        print(f'{self.name}正在唱:{song}')


# 对象
p1 = Person('华晨宇', 31)
print(f'p1: {id(p1)}')
# print(p1.name)
# print(p1.age)
p1.sing('烟火里的尘埃')
print('*' * 60)

p2 = Person('邓紫棋', 30)
print(f'p2: {id(p2)}')
# print(p2.name)
# print(p2.age)
p2.sing('画')
print('*' * 60)
#
p3 = Person('张碧晨', 32)
print(f'p3: {id(p3)}')
p3.sing('凉凉')
