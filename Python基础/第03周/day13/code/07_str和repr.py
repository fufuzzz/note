class Dog:
    # 限制属性: 限制可以使用哪些属性
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__() :
    #    1.必须返回字符串
    #    2.作用是: 让打印对象时可以输出__str__()的返回值
    def __str__(self):
        return f'姓名:{self.name}, 年龄:{self.age}'

    # __repr__(): 和__str__类似,但是会优先使用__str__()
    def __repr__(self):
        return f'姓名2: {self.name}, 年龄:{self.age}'


# 调用
d = Dog('旺财', 2)
print(d, type(d))  # 姓名: 旺财, 年龄: 2   <class '__main__.Dog'>
