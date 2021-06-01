# 函数
#   作用:封装一个具有特定功能的代码
# 数学的函数:
#   f(x) = 3x + 2

# Python的函数:
# def f(x):
#       return 3*x + 2

# 1.函数定义
def f():
    print('f')


# 2.函数调用
f()
f()


# 3.参数
# 求x和y的和
def my_sum(x, y):
    s = x + y
    print(s)


my_sum(1, 3)
my_sum(100, 200)

# 参数: 形参,实参
#       形参: x,y;  形式参数,函数定义时括号()中的参数(变量)
#       实参: 3,5;  实际参数,函数调用时括号()中的参数(值)
print('-' * 50)


# 4. 返回值
#   return:
#     1.存在于函数中
#     2.可以返回结果(可以是1一个值,或多个值:会返回元组)
#     3.会立刻终止函数(立刻退出函数)
#     4.如果不写return或return后不写值,则默认返回None
def sum2(x, y):
    s = x + y
    return s
    # return 100, 200
    print('我永远不会执行')


r = sum2(3, 5)
print(r)

print(sum2(100, 200) * 10)


# 判断一个函数is_leap(year)判断闰年,并返回True或False
def is_leap(year1):
    if year1 % 4 == 0 and year1 % 100 != 0 or year1 % 400 == 0:
        return True
    else:
        return False


a = is_leap(2000)
print(a)
