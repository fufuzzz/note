# 多态:
#   在继承的基础上, 一般是多个子类继承同一个父类,让每个子类都重写父类的同一个方法
#   子类的这个方法写不同的功能, 那么用父类对象指向不同子类时,调用该方法可以实现不同的功能

# 父类
class Animal:
    def eat(self):
        pass


# 子类
class Dog(Animal):
    def eat(self):
        print('吃骨头')


class Cat(Animal):
    def eat(self):
        print('吃鱼')


class Pig(Animal):
    def eat(self):
        print('吃白菜')


# Person
class Person:
    def feed(self, animal: Animal):
        animal.eat()


# 创建对象
dog = Dog()
cat = Cat()
pig = Pig()

Person().feed(pig)