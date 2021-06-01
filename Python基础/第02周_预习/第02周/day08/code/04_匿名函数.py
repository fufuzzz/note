# 匿名函数: 没有名字的函数

# 普通函数
def f(n):
    return n * 2


# 匿名函数
f2 = lambda n: n

print(f(10))  # 20
print(f2(10))  # 20

# 多个参数
f3 = lambda a, b: a + b
print(f3(3, 4))  # 7

# sort(key=)

l = [
    {'name': '贾玲', 'age': 30},
    {'name': '沈腾', 'age': 40},
    {'name': '宋小宝', 'age': 50},
    {'name': '罗志祥', 'age': 40},
    {'name': '马保国', 'age': 69},
    {'name': '特朗普', 'age': 74}
]


# 匿名函数
# l.sort(key=lambda d:d['age'])

# 普通函数
# def fn(d):
#     return d['age']
#
#
# l.sort(key=fn)
# print(l)


# 回调函数
#  普通函数
def a(x, f):  # f=b
    print(f'x = {x}')
    f(x + 1)  # 相当于:b()


# 回调函数
def b(y):
    print('b: y=', y)


# 调用

a(10, b)

print()


# 函数名: 是函数名.也是指向该函数的一个变量(对象)
def fc():
    print('fc')


# 调用
fc()
fd = fc  # 变量只要指向函数,就可以调用函数
fd()


# 扩展: 自定义my_sort函数
def my_sort(l, key=None, reverse=False):
    # 冒泡排序
    for i in range(len(l) - 1):
        for j in range(len(l) - 1 - i):
            left = l[j]
            right = l[j+1]
            if key:
                left = key(left)
                right = key(right)
            # 是否降序
            if reverse == False:
                if left > right:
                    l[j], l[j + 1] = l[j + 1], l[j]
            else:
                if left < right:
                    l[j], l[j + 1] = l[j + 1], l[j]
    return l


l2 = [
    {'name': '贾玲', 'age': 30},
    {'name': '沈腾', 'age': 40},
    {'name': '宋小宝', 'age': 50},
    {'name': '罗志祥', 'age': 40},
    {'name': '马保国', 'age': 69},
    {'name': '特朗普', 'age': 74}
]
l3 = my_sort(l2, key=lambda d: d['age'])
# l3 = my_sort([3, 2, 1, 5, 4])
print(l3)

