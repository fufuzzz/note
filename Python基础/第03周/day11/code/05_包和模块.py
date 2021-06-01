# 包: package,包含__init__.py文件的文件夹

# 模块: module,就是一个.py文件
#   内置模块,比如: os, random... Python提供
#   自定义模块, 自己写的模块
#   第三方模块, 别人写的一般都需要安装

# 1.如何导入模块
#   import
#   from-import

# import
# import os
# import math, random

# print(math.sqrt(100))


# from-import: 精确导入
# from math import sqrt
# print(sqrt(100))
#
# from math import *   # 模糊导入, *通配符
# print(sqrt(100))
# print(ceil(34.567))

# 别名: as
import random as rd

# print(rd.randint(3, 4))   # 原名称不可以使用

from random import randint as ri

print(ri(3, 4))

# 导入自定义包和模块
# 多次导包,也只会导入一次
import module1
import module1

module1.fn()

from module1 import fn
fn()


# 包
# 不推荐
# import my_package.module2
# print(my_package.module2.name)

# 邓紫棋  画 把思念一点一滴化成雨落下
# 张碧晨
# 推荐使用from-import
from my_package import module2
print(module2.name)

from my_package.module2 import name
print(name)
