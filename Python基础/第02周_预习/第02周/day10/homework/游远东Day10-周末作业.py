''''''

''' 简答题 '''
# 1， Python中的循环有几种:
# for 循环 和 while 循环

# 2， Python的数据类型有哪些:
# 数值型: int float
# 字符串: str
# 布尔类型: False True
# 列表: list
# 元组: tuple
# 字典: dict
# 集合: set

# 3， Python中空类型特殊值是:
# 0,False
# 空列表[], 空元组(),空字符串'',空集合set(),空字典{}

# 4， 判断下列赋值方式正确与否（True or False）
'''
    x = y = z = 1           =>  True
    x=1, y=2                =>  False
    x, *y, z = 1,2,3,4      =>  True
    x, y, z = (1,2,3)       =>  True
'''

# 5, 列举至少5种常用的内置函数,并解释函数的作用：
# print() 打印输出数据
# input() 输入数据
# sort() 给指定数据排序
# max() 取出指定数据的最大值
# min() 取出指定数据的最小值
# sum() 给指定数据求和

# 6，判断下面变量名不正确的有哪些：
# ABC正确, aBC正确, a-bc不正确, a_bc正确， _num123正确, 123num正确, NUM123正确, num_123正确，
# True不正确, false正确, true1正确, false0正确， print不正确, id正确, __id__正确, python正确
# 不正确的有a-bc, True, print

# 7，列举列表list中的至少6个函数，且说明每个函数对应的作用
# append() 在列表末尾添加元素
# insert() 在指定下标插入元素
# pop()  在指定下标弹出元素
# remove() 删除指定元素
# count() 计算元素在列表出现的次数
# sort() 给列表元素排序
# index()  找出指定元素在列表第一次出现的下标

# 8，列举字典dict中的至少3个函数，且说明每个函数对应的作用
# values():获取字典的中的值
# key():获取字典中的关键字
# pop():删除指定下标的元素

''' 编程题 '''


# 1， 将列表中元素去重, 使用至少2种方式
# 方法一
def f1(l):
    l2 = []
    for n in l:
        if n not in l2:
            l2.append(n)
    return l2


# 方法二
def f2(l):
    z = len(l)
    n = 0
    while n < len(l):
        for i in range(len(l) - 1, n, -1):
            if l[i] == l[n]:
                l.pop(i)
        n += 1
    return l


l = [1, 1, 2, 11, 3, 1, 1, 1, 5, 2]
print(f1(l))
print(f2(l))


# 2、编写一个函数gcd(x,y) 求最大公约数，编写一个函数lcm(x,y)求最小公倍数。
# 最大公约数
def gcd(x, y):
    min1 = min(x, y)
    while True:
        if x % min1 == 0 and y % min1 == 0:
            return min1
        else:
            min1 -= 1


print(gcd(6, 4))


# 最小公倍数
def lcm(x, y):
    max1 = max(x, y)
    while True:
        if max1 % x == 0 and max1 % y == 0:
            return max1
        else:
            max1 += 1


print(lcm(6, 4))

# 3、使用Python编程实现下面图形打印,n行：
'''
    *
   **
  ***
 ****
*****
'''


def fn(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)


fn(5)

# 4、使用Python编程实现下面图形打印,n行：
'''
    *
   ***
  *****
 *******
********* 
'''


def fn2(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


fn2(5)


# 5，将字典的key和value置换，
# 如使用字典: d1 = {'a':1,'b':2,'c':3}，
# 置换后生成字典: d2 = {1:'a', 2:'b', 3:'c'}
def fn3(d1):
    d2 = {}
    for k, v in d1.items():
        d2[v] = k
    return d2


d1 = {'a': 1, 'b': 2, 'c': 3}
print(fn3(d1))
# 6、使用Python写一个按照下面方式调用都能正常工作的 my_sum() 方法
'''
    print(my_sum(2,3))     输出 5
    print(my_sum(2)(3))    输出 5     
'''


def my_sum(*args):
    def sum2(*args2):
        return args[0] + args2[0]

    if len(args) < 2:
        return sum2
    else:
        return sum(args)


print(my_sum(2, 3))
print(my_sum(2)(3))

# 提示:
#   通过参数数量判断不同的情况
#   1.有1个参数, 嵌套函数
#   2.有2个参数, 返回和

import math


# 7， 封装函数，传入不定数量的数值型参数，返回所有数字的乘积,
# 提示: *args
def fn7(*args):
    a = 1
    for n in args:
        a *= n
    return a


print(fn7(1, 2, 3, 4, 5, 6))

# 8， 封装一个函数random_color，该函数的返回值为随机十六进制颜色。
# 说明： 十六进制颜色#开头后面接6个十六进制数， 例: #FFFFFF， #000，000 #0033CC
# 提示: colors = '0123456789ABCDEF'
#      random模块
import random

colors = '0123456789ABCDEF'


def random_color(colors):
    s = ''
    for i in range(6):
        s += random.choice(colors)
        # b = int(s, 16)
        # c = hex(b)
    return s


print('#', random_color(colors), sep='')


# 9， 封装函数，
# 第一个函数create_persons()，
#   创建并返回包含5个字典(例如:{"name":"xx","age":xx, "faceValue":100})的列表
#      其中name的值：从["张三","李四","王五","赵六","钱七"]依次取
#      其中age的值：10-100之间的随机整数
#      其中faceValue的值：0-100之间的随机整数
# 第二个函数get_old(), 传入第一个函数创建的列表, 找出列表中年龄最大的人，并将其所有信息打印
# 第三个函数sort_facevalue(), 传入第一个函数创建的列表, 根据颜值升序排列，并打印排序后的信息

def create_persons():
    persons = []

    name = ["张三", "李四", "王五", "赵六", "钱七"]

    for i in name:
        d = {}
        d["name"] = i
        d["age"] = random.randint(10, 100)
        d["faceValue"] = random.randint(0, 100)
        persons.append(d)
    return persons


def get_old(persons):
    # persons.sort(key=lambda a: a['age'])
    # max1 = persons[4]
    # print(f'最大年龄的信息{max1}')
    # print()
    old = max(persons, key=lambda x: x['age'])
    old_person=[p for p in persons if p['age']==old['age']]

def sort_facevalue(persons):
    persons.sort(key=lambda a: a['age'])
    for n in persons:
        print(n)


# 调用
persons = create_persons()
get_old(persons)
sort_facevalue(persons)
