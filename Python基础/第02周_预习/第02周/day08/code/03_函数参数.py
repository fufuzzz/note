# 函数参数

# 1.位置参数/必需参数
def f1(a, b, c):
    print(a, b, c)


f1(2, 3, 4)


# 2.默认参数:形参中
def f2(a, b, c=20):
    print(a, b, c)


f2(1, 2)
f2(1, 2, 200)


# 3.关键字参数: 实参中
#   一般会结合默认参数一起使用
def f3(a, b=3, c=4):
    print(a, b, c)


# f3(a=1, b=2, c=3)
# f3(a=1, c=2, b=3)
f3(10, c=30)


#  4.可变长参数/不定长参数
#   *args
#   **kwargs

# *args: 可以接受任意多个位置参数, 得到元组
def f4(*args):
    print(args)

f4(1)
f4(1, 2, 3)


# **kwargs: keyword arguments
#       可以接受任意多个关键字参数, 得到字典
def f5(**kwargs):
    print(kwargs)


f5(a=1, b=2, c=3)


# {'a': 1, 'b': 2, 'c': 3}

# 形参参数顺序: 位置参数, *args, 默认参数, **kwargs
# 实参参数顺序: 位置参数, 关键字参数

# 通用参数的写法
def fn(*args, **kwargs):
    print(args, kwargs)


fn(1, 2, 3, a=4, b=5)


# (1, 2, 3) {'a': 4, 'b': 5}


# 所有参数
def fn2(a, b, *args, e=5, f=6, **kwargs):
    print(a, b, args, e, f, kwargs)


fn2(1, 2, 3, 4, 50, f=60, g=70, h=80)


def f6(*args):
    print(args)


t = tuple([1, 2, 3])
f6(t)
