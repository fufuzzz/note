# 面向对象有4大特征:
#   1.封装: 将属性和方法封装在类中,私有属性等.
#   2.继承: 让子类继承父类的属性和方法
#   3.多态
#   4.抽象


# 继承: 让子类继承父类的属性和方法

# 子类: 派生类
# 父类: 基类

# Ipod类: mp3
class Ipod(object):
    def __init__(self, color):
        self.color = color

    def play_music(self):
        print('听歌')


# Ipad类: 平板
class Ipad(Ipod):
    def __init__(self, color, price):
        # 需要调用父类的init方法: 借用父类的init方法来初始化属性
        # Ipod.__init__(self, color)  # 显式调用
        super().__init__(color)  # 隐式调用
        self.price = price
        # self.__price2 = price2

    def play_lol(self):
        print('玩游戏')
        # print('---', self.__price2)


# Iphone类
class Iphone(Ipad):
    def __init__(self, color, price, size):
        Ipad.__init__(self, color, price)
        self.size = size

    def call(self):
        print('打电话')
        # 报错, 不可以使用父类的私有属性和私有方法
        # print(self.__price2)


# 多重继承
# 调用
iphone12 = Iphone('骚红色', 8000, '6.1')
print(iphone12.color, iphone12.price, iphone12.size)
iphone12.call()
iphone12.play_lol()

# 调用
# ipad = Ipad('银色', 3000)
# print(ipad.price, ipad.color)
#
# ipad.play_music()
# ipad.play_lol()
