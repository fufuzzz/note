class People:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # 间接访问
    # getter 方法
    # def get_age(self):
    #     return self.__age
    #
    # # setter方法
    # def set_age(self, new_age):
    #     if new_age >=18:
    #         self.__age = new_age

    # 装饰器
    # @property : 作用是将方法属性化:让方法可以当成属性来来使用
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def money(self):
        return f'{self.name}: 我先定个小目标一个亿'


# 调用
p = People('思聪', 33)
# print(p.get_age())  # 33
# p.set_age(18)
# print(p.get_age())   #18

# 装饰器后调用方式
print(p.age)  # 获取
p.age = 18  # 设置
print(p.age)  # 获取

print(p.money)