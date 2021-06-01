class Person:
    # 类属性
    age = 42

    def __init__(self, name):
        # 对象属性
        self.name = name

    # 成员方法: 常用
    def eat(self):
        print('eat')

    # 私有方法: 不想被类外直接使用
    def __sleep(self):
        print("sleep")

    # 类方法
    #   1. 可以使用对象和类来调用类方法,建议使用类调用
    #   2. 只有cls,所以只能调用类属性和其他类方法或静态方法,
    #   3. 不能使用self: 不能调用对象属性,私有属性,成员方法,私有方法等
    @classmethod
    def lol(cls):  # cls: class
        print(cls)  # <class '__main__.Person'>
        print(cls == Person)  # True
        print(cls.age)  # 可以调用类属性
        # print(cls.name)  # 不可以调用对象属性

    # 静态方法: 就是放在类中的一个普通函数,和类中的其他属性或方法没有关系
    #   1. 可以使用对象和类来调用类方法,建议使用类调用
    #   2. 没有cls,虽然可以使用类名,但是尽量不用类属性和其他类方法和静态方法
    #   3. 不能使用self: 不能调用对象属性,私有属性,成员方法,私有方法等
    @staticmethod
    def play_basketball():
        print('打篮球')


# 调用
p = Person('周杰伦')
p.lol()  # 对象.类方法
Person.lol()  # 类.类方法

p.play_basketball()  # 对象.静态方法
Person.play_basketball()  # 类.静态方法
p.eat()  # 对象.成员方法
# Person.eat(p)  # 不推荐
