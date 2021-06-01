# 函数名:既是函数名,也是指向函数的变量
def abs(n):
    if n < 0:
        return -n
    return n


print(abs(-10))  # 10

f = abs  # 所有指向函数的变量都可以通过()调用该函数
print(f(-20))
print(id(f), id(abs))


# 再讲一遍回调函数
# 把函数当成参数来使用

# 使用匿名匿名
def f1(x, f):
    x = x + 10
    print(f(x))


f1(1, lambda a: a ** 2)


# 使用普通函数
def f2(x, f):  # x=1; f=fn1
    x = x + 10  # 相当于调用:fn1(x)
    # print(f(x))
    return f(x)


def fn1(a):
    return a ** 2


def fn2(a):
    return a ** 3


# f2(1, fn1)
r = f2(1, fn2)
print('r =', r)
