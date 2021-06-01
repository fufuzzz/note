
#
# 单例模式: 设计模式中的一种
# 设计模式: 23种
#   工厂模式, 适配器模式, 单例模式, 装饰器模式,代理模式...

# 单例模式: 单个实例 (了解)
# __new__() 掌握

class A:
    # init: 初始化属性
    def __init__(self, name):
        print('__init__()')
        self.name = name

    # 类属性
    instance = None

    # new: 创建对象时会自动调用
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__()')

        if cls.instance == None:
            # 借用父类的new来创建对象
            cls.instance = super().__new__(cls)

        return cls.instance

# 对象
a1 = A('宝强')
a2 = A('宝强')
a3 = A('宝强')
