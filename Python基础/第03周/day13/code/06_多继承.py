# 单继承: 只有一个父类
# 多继承: 有多个父类

# 父类
class Father:
    def __init__(self, name):
        self.name = name

    def money(self):
        print('赚钱')


class Mother:
    def __init__(self, age):
        self.age = age

    def cook(self):
        print('做饭')


# 子类
class Son(Father, Mother):
    def __init__(self, name, age):
        # 调用父类的init方法
        # 显式调用
        # Father.__init__(self, name)
        # Mother.__init__(self, age)
        # 隐式调用
        # super().__init__(name)
        super(Son, self).__init__(name)
        super(Father, self).__init__(age)

    def eat(self):
        print('吃')


# 调用
son = Son('思聪', 33)
print(son.name)
print(son.age)
son.eat()
son.money()
son.cook()

# mro算法: 从左往右的一个继承链
print(Son.__mro__)
# (<class '__main__.Son'>,
# <class '__main__.Father'>,
# <class '__main__.Mother'>,
# <class 'object'>)


# 2种使用场景
#   1. 直接继承另一个类, 比如: 猫继承动物类, 男人继承人类
#   2. 提取2个类(或多个类)的共有属性或方法 组成一个父类
