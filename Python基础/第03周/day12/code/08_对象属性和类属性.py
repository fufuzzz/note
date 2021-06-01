class Dog:
    # 类属性
    name = '八公'
    sex = '公'
    age = 16
    likes = ['骨头']

    def __init__(self, color, name):
        # 对象属性
        self.color = color
        self.name = name
        self.likes2 = ['骨头']


# 对象
dog1 = Dog('黄色', '忠犬八公')
# print(dog1.name)  # 对象.类属性
# print(dog1.color)  # 对象.对象属性

# print(Dog.name)  # 类.类属性
# print(Dog.color)  # 类.对象属性,会报错

# 修改属性:
#   类属性: 尽量用 类名.类属性来修改
#   对象属性: 用 对象.对象属性来修改
# Dog.age = 6  # 类.雷属性 修改的是类属性
# dog1.age = 6  # 新增了一个对象属性age:动态添加属性
# print(dog1.age, Dog.age)
#
# dog1.color = 'green'
# Dog.color = 'green'
# print(dog1.color)

# 对象属性和类属性有同名的情况下
# 查询属性值
# print(dog1.name)  # '忠犬八公' 会优先获取对象属性
# print(Dog.name)  # '八公'

# dog1.name = '旺财'
# print(dog1.name, Dog.name)  # 旺财 八公

# Dog.name = '旺财'
# print(dog1.name, Dog.name)  # 忠犬八公 旺财


# 类属性: 可变类型是共享的
print('-'*60)
# 对象属性:可变类型
d1=Dog('白色','小白')
d2=Dog('黑色','小黑')
print(d1.likes2) # ['骨头']
print(d2.likes2) # ['骨头']

d1.likes2.append('狗粮')
print(d1.likes2)  # ['骨头', '狗粮']
print(d2.likes2)  # ['骨头',
