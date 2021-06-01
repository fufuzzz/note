# 构造函数: 初始化函数 __init__(self):
#       在对象创建时会自动调用,用来初始化属性
# 析构函数:
#       在对象销毁时会自动调用,用来清理内存等

class Cat:

    # 构造函数: 构造方法,初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__')

    # 析构函数: 了解
    def __del__(self):
        print('__del__')


# 对象
cat1 = Cat('Tom', 3)

print('hello')
print(cat1.name)
