# 作用域: 起作用的区域

if 1:
    a = 10
print(a)

for i in range(1):
    b = 10
print(b)


# if,for,while不包含作用域

def fn():
    c = 100
    print(c)


fn()
# print('c=', c)

# 在函数内部定义的变量,在函数外不可以调用
# print('c =', c)  # 报错

# 全局作用域: G(Global)
# 局部作用域: L(local)

# 局部变量: 函数内的变量
# 全局变量: 函数外的变量

x = 100


def f2(z=300):
    y = 200
    print(x, y, z)


f2()
print('x =', x)  # x是全局变量
# print('x =', y)  # y是局部变量
# print('x =', z)  # z是局部变量


# 作用域种类
# 内建作用域: Built-in
# Python 提供的内置函数,类,等

d = 1  # 全局作用域 Global


def f3():
    e = 2  # 函数作用域: Enclosing 闭包

    def f4():
        f = 3  # 局部作用域 local


# 关键字
#   global
#   nonlocal

# global关键字
i = 100


def f5():
    global i  # 声明使用的i是全局变量
    i += 200
    print('i =', i)


f5()
print('-- i =', i)

# nonlocal关键字
j = 1


def f6():
    j = 2

    # 当前作用域下的变量: 了解
    # print(locals())
    def f8():
        j = 22
        o = 1
        def f7():
            # global j  # 声明使用的是全局变量j=1
            nonlocal j, o  # 声明使用的是j=22
            j += 3
            o += 3
            print('j =', j, o)

        f7()
    f8()

f6()
print('-- j =', j)

print(globals())  # 打印所有的全局变量
print(list(globals().keys()))  # 打印所有的全局变量
