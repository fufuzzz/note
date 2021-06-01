
# 重写
#   在继承的基础上,让子类可以有和父类一样的方法,则子类重写了父类的方法

class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('跑1KM')

class Man(Person):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print('跑10km')

# 调用
man = Man('博尔特')
man.run()