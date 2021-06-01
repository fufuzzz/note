''''''

'''
1. 模块
    时间模块:
        import time
            time.time()
            time.sleep()
        import datetime
            d = datetime.datetime.now()
            d = datetime.datetime(2022,11,22, 11,22,33)
            
            d.year, d.month, d.day, d.date()
            d.hour, d.minute, d.second, d.time()
            
            d.strftime('%Y-%m-%d %H:%M:%S')
            d.strptime()
            
            d.timestamp()
            d.fromtimestamp()
            
            时间差
            datetime.timedelta(days=10)
    加密模块hashlib
        import hashlib
        m = hashlib.md5()
        m.update('dfsd'.encode())
        m.hexdigest()

2. 面向对象
    1. 面向对象和面向过程的区别
        面向对象:类
        面向过程:函数
    2. 类和对象
        类: 用来创建对象
        对象: 用类创建的具体的实例
        
        类中的属性和方法
            属性: 变量, 静态的
            方法: 函数, 动态的, 功能
    3. self
        1. 不是关键字,但是尽量写成self
        2. self是不传值得
        3. self就是指向当前类的对象: 谁调用当前方法,则self就是谁
        4. self的作用: 用来调用类中其他属性和方法
    4. 对象属性和类属性
        推荐:
            对象属性 用来对象调用
            类属性 用来类调用
    5. 构造函数 和 析构函数
        构造函数: __init__(self):
        析构函数: __del__(self):
    6. 私有属性 和 私有方法
        私有: 使用双下划线,比如: __age
                _sex : 认为是私有
        调用私有属性: 对象._类名__私有属性(不推荐)
            
'''

import datetime

