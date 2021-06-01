# 函数嵌套

def f1():
    print('--- f1 ---')

    def f2():
        print('--- f2 ---')

    return f2


# # f1()
# f = f1()  # f=f2
# f()  # f2()

# f1()()

# 全局变量: 1.可能被修改(污染),2.不会被释放
x = 10


def fn1():
    global x
    x += 1
    print(x)


fn1()


# 局部变量
def fn2():
    y = 10


fn2
# print(y)  # 报错,局部变量,内部有GC(垃圾回收机制/内存会自动回收)


# 闭包: 函数嵌套函数,且会返回内部函数,则外部函数的变量或参数不会被回收
def f3(x=1):
    print('--- f3 ---')

    a = 10
    def f4(y=2):
        # print('--- f4 ---:', x, y)
        nonlocal a
        a += 1
        print('a =', a)

    return f4


# f3(5)(6)

f = f3()  # f=f4
f()  # 11
f()  # 12
f()  # 13
