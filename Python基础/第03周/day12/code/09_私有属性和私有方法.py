# 类
class Pig:
    def __init__(self, name, age, sex):
        self.name = name
        # 私有属性:
        #   1.在属性前添加双下划线则是私有属性
        #   2.只能在当前类内部使用
        self.__age = age
        self._sex = sex

    def sleep(self):
        print(f'{self.name}正在睡觉...')

    # 私有方法
    def __eat(self):
        print(f'{self.name}正在吃饭...')


# 对象
peiqi = Pig('佩奇', 2, '母')
print(peiqi.name)
# print(peiqi.age)  # 报错, 私有属性不可以在类外使用
print(peiqi._sex)  # 公有属性


# 私有方法
# peiqi.__eat()  # 私有方法不可以在类外使用


# 虽然可以使用 _类名__私有属性 来访问,但是我们也要认为不可以访问
print(peiqi._Pig__age)
peiqi._Pig__eat()