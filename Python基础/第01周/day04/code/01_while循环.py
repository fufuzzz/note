
# while循环
#  语法格式:
#   while 循环条件(循环的终止条件):
#       循环体(代码)
#       循环的改变量
#

import time


# if单分支: 当if后的条件满足,则进入一次if
if 3 > 2:
    print('ok')

# while
# 死循环: 循环不会停止
# while 3 > 2:
#     print('ok')
#     time.sleep(0.5)  # 暂停0.5秒


# while循环计算: 1+2+3+...+100

# 第1次循环,循环前: i=1,s=0; 判断i<=100是否成立, 循环后: s=0+1=1, i=1+1=2
# 第2次循环,循环前: i=2,s=1; 判断i<=100是否成立, 循环后: s=0+1+2, i=2+1=3
# 第3次循环,循环前: i=3,s=2; 判断i<=100是否成立, 循环后: s=0+1+2+3, i=3+1=4
# ...
# 第99次循环,循环前: i=99,s=..; 判断i<=100是否成立, 循环后: s=0+1+2+3+...+99, i=99+1=100
# 第100次循环,循环前: i=100,s=98; 判断i<=100是否成立, 循环后: s=0+1+2+3+...+99+100, i=100+1=101
# 第101次循环,循环前: i=101,s=5050;判断i<=100是否成立,不成立
# i = 1   # 循环的初始值:只会执行一次
# s = 0
# while i <= 100:  # 循环的条件
#     print(i, end=' ')
#     s += i
#     i += 1   # 循环改变量
# print()
# print('i =', i)
# print('s =', s)


# 1.求1-100之间可以被7整除的数的个数
count = 0
i = 1
while i <= 100:
    if i % 7 == 0:
        count += 1
    i += 1
print('count =', count)


# 2.计算从1到100以内所有奇数的和。
s = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        s += i
    i += 1
print('s =', s)

# 3.计算从1到100以内所有能被3或者17整除的数的和。
s = 0
i = 1
while i <= 100:
    if i % 3 == 0 or i % 17 == 0:
        s += i
    i += 1
print('s =', s)
# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
count = 0
i = 1
while i <= 100:
    if (i % 3 == 0 or i % 7 == 0) and i % 21 != 0:
        count += 1
    i += 1
print('count =', count)


# 5.计算1到500以内能被7整除但不是偶数的数的个数。

count = 0
i = 1
while i <= 500:
    if i % 7 == 0 and i % 2 != 0:
        count += 1
    i += 1
print('count =', count)

# 让用户输入密码,允许最多输错3次,真实密码是123


i = 1
while i <= 3:
    password = input('请输入密码:')
    if password == '123':
        print('密码正确!')
        break  # 立刻结束循环
    else:
        print('密码错误,请重新输入')

    i += 1
if i == 4:
    print('最多输入三次')


# 石头剪刀布:
#   电脑随机出石头1,剪刀2,布3
#   自己输入石头1,剪刀2,布3

import random
i = 1
while i:
    print('-' * 20)
    # 1.电脑随机石头1,剪刀2,布3
    computer = random.randint(1, 3)
    # 2.自己输入石头1,剪刀2,布3
    me = int(input('请出拳(石头1,剪刀2,布3)'))

    # 3.判断输赢
    if me == computer:
        print('平手,请继续出拳...')
    elif me - computer == -1 or me - computer == 2:
        print('恭喜你!赢了')
    else:
        print('你输了')
    i = int(input('是否结束游戏,结束游戏请输入0否则输入1'))
