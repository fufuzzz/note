class Apple:
    def __init__(self, color, name, weight):
        self.name = name
        self.color = color
        self.weight = weight

    # 运算符重载: 了解
    def __add__(self, other):
        return self.weight + other.weight


# __sub__

# 调用
apple = Apple('红色', '红富士', 500)
# print(apple.__class__)
# print(Apple.__class__)

# print(apple.__name__)  # 报错
# print(Apple.__name__)  # 类名

# print(apple.__dict__)  # {'name': '红富士', 'color': '红色'}
# print(Apple.__dict__)

# print(apple.__module__)  # 所在模块 __main__
# print(Apple.__bases__)  # 所有基类(父类)

a1 = Apple('绿色', '青苹果', 250)
print(a1 + apple)