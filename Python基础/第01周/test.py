# a = "hello "
# b = "Jack"
# c = []
# c.append(a)
# c.append(b)
# # print(''.join(c))
# # # print(a+''+b)
# # print(id(a))
# # print(type(a))
# print(a, b, sep='')
# print('%s%s' % (a, b))
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)


# L = float(input('请输入长'))
# W = float(input('请输入宽'))
# s = L * W
# print(round(s, 2))


# def fn1(n1, n2):
#     num = []
#     for i in range(n1, n2 + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             num.append(i)
#     return num
#
#
# print(fn1(100, 200))
#
#
# def fn2(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(f'{j}*{i}={i * j}', end='\t')
#         print()
#
#
# fn2(6)
# print('  s', 'ss', sep='   ')

# def fn3(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print(f'输入的{year}是闰年')
#
#     else:
#         print(f'输入的{year}不是闰年')
#
#
# year = int(input('请输入一个年份'))
# fn3(year)
#
# def fn4(n1, n2):
#     s = 0
#     for i in range(n1, n2 + 1):
#         s += i
#     return s
#
#
# print(fn4(100, 1000))
#
# sum1 = 1
# for num in range(1, 4):
#     sum1 *= num
#
#     print(sum1)
# a = [2, 4, 9, 5, 9, 8, 1]
# [index for index, value in enumerate(a) if value == max(a)]
# print([index for index, value in enumerate(a) if value == max(a)])
#
# a = {'a': 10, 'b': 3, 'c': 5}
#
# b = a
#
# b['c'] = 8
# print(a.values(), type(a.values()))
# print(sum(a.values()))
#
# total = 0
#
#
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数内是局部变量 : ", total)
#     return total
#
#
# sum(2, 3)
# list1 = [1, 2, 3]
#
#
# def func():
#
#     list1.extend([4, 6, 8, 9])
#
#
# func()
#
# print(list1)

# list1=[5,3,1,9,12]
# func = (x for x in list1 if x%3==0)
#
# print(func())
# nums = [2,7,6,7,8]
# nums.insert(nums.index(7),9)
# print(nums)

# a = [2, 5, 3, 9, 6]
# a, b, *c = sorted(a, reverse=True)
# print(b)
#
# def func():
#    for i in range(5):
#        print('-->',i)
#        yield
#
# next(func())
# next(func())
# list0 = ['nice', '你好', '今天天气真好', 'beautiful', 'family', [27, 19, 33]]
# new_list = [i for i in list0 if type(i) is str]
# print(new_list)
# def A(func):
#     print('-->1')
#     def wrapper(*args,**kwargs):
#         func()
#         print('-->hello')
#     return wrapper
# @A
# def show():
#     print('-->python')
#
# show()
#
# import time
# def outer2(fn):  # fn=run
#     def inner():
#         s = time.time()
#         fn()  # 相当于调用原始的run
#         e = time.time()
#         print(e - s)
#
#     return inner
#
#
# # 函数定义
# @outer2  # @outer2 => 相当于在run函数后添加了: run = outer2(run)
# def run():
#     print('跑步...')
#     time.sleep(2)
#
#
# run()

# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'c': 9, 'd': 4, 'e': 5}
# for k, v in d1.items():
#     d2[k] = v
# print(d2)
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'b': 9}
# dict1.pop('a') # 弹出key值为a的键值对
# dict1.update(dict2)  # 合并字典
# print(dict1)

def fn(*args, **kwargs):
    print(args, kwargs)
    print(type(args), type(kwargs))


fn(1, 2, 3, 4, a=9, b=10)


def my_sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


list1 = [1, 3, 5, 6, 7, 9, 0, 2, 4, 7, 9]
print(my_sort(list1))


def my_sum(n):
    s = 0
    for i in range(0, n + 1, 2):
        s += i
    return s


print(my_sum(5))

import random


def my_random(n):
    for i in range(n):
        print(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'), end='')
    print()


my_random(4)


def my_random_num(n):
    num_list = []
    for i in range(n):
        num_list.append(random.randint(1, 20))
    return num_list
a = my_random_num
print(a(4))

print(my_random_num(5))

dict1 = {'a': '001', 'b': '002', 'c': '003'}
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k

print(dict2)

list2 = ['游远东', '张三', 'Tom', '', 'li', '']
list2.remove('')
for n in list2:
    if n == '':
        list2.remove(n)

print(list2)
# li =['jack','tom','lucy']
# print('_'.join(li))


import sys
import time

print(sys.version)
# def f():
#
#     a = []
#
#     for i in range(5):
#
#         a.append(lambda x: i*x)
#     for i in range(5):
#         print(a[i])
#         print(a[i](2))
#     print(a[2])
#     print(a[2](2))
#     return a
#
#
# t = f()
#
# print(t[1](2), t[1](3), t[2](2))
class Person(object):
    __slots__ = ('name', 'age', 'sex')

    def __init__(self, name, age):
        self.name = name
        self.age = age


import test
p = test.Person('lucy', 18)
print(p.__module__)  # test