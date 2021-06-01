''''''
'''

Python: 一切皆对象

1. 编程思想
    面向过程: c语言(
        注重的是: 解决一个问题的每个步骤
    面向对象: OC语言(类), c++, Python, java, c#.
        注重的是: 解决一个问题中的每个对象
    
2. 理解面向对象
什么是类: 一系列(class)(泛指,统称), 比如: 人类, 
什么是对象: 具体存在的一个事物(具体的), 比如: 我们班的这个张三
   类是对象的抽象
   对象是类的具体  
          
      类         对象
     鼠标     我桌上的这个鼠标
     电脑       我的这台电脑
    联想电脑  我家里的那台联想电脑
     男人         特朗普
     女人         刘亦菲


     
'''
# 示例： 小狗吃食（闻一闻smell、舔一舔lick、咬一咬bite）
# 	  分别采用面向过程和面向对象来分析
#
# 面向过程 :  先闻一闻, 然后再舔一舔, 最后再咬一咬 (注重过程)
# 面向对象 :  小狗是一个对象, 它可以闻一闻食物, 可以舔一舔食物, 可以咬一咬食物.      (不注重过程, 注重对象)

# 面向过程:
'''
def smell():
    print('闻一闻')


def lick():
    print('舔一舔')
    
    
def bite():
    print('咬一咬')


smell()
lick()
bite()
'''


# 面向对象:
# 类: 属性(变量), 方法(函数)
class Dog:
    name = '旺财'

    def smell(self):
        print(self.name, '闻一闻')

    def lick(self):
        print(self.name, '舔一舔')

    def bite(self):
        print(self.name, '咬一咬')


# 对象: 由类来创建
dog = Dog()
dog.smell()
dog.lick()
dog.bite()
