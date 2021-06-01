''''''

''' 基础题 '''
# 1, 五位数中，对称的数称为回文数，找出所有的回文数。
#       如: 12321
# n = int(input('输入一个数'))
# a = []
# while n:
#     a.append(n % 10)
#     n //= 10
# if a[:] == a[::-1]:
#     print('是一个回文数')
# else:
#     print('不是一个回文数')

# 2, 求1!+2!+3!+4!+5!
#       !表示阶乘
import math

a = 1
s = 0
for i in range(1, 6):
    # s += math.factorial(i)
    a *= i
    s += a
print(s)

# 3, 找出所有的水仙花数，三位数，各位立方和等于该数本身。
#        如: 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(10):
            if i ** 3 + j ** 3 + k ** 3 == 153:
                print(i * 100 + j * 10 + k)

''' 进阶题 '''
# 1, 输入任意两个数，如果第一个数小，从第一个数打印到第二个数，如果第二个数小，从第二个数打印到第一个数
# eval(): 会计算字符串的表达式
# print(eval('3,4'))

# num1 = int(input('输入一个数'))
# num2 = int(input('输入另一个数'))
num1, num2 = eval(input('请输入2个数'))
min1 = min(num1, num2)
max1 = max(num1, num2)
for i in range(min1, max1+1):
    print(i, end=' ')

# a = []
# a.append(num1)
# a.append(num2)
# if num1 < num2:
#     print(a[:2])
# else:
#     print(a[1::-1])
# 2, 输入两个数n,a, 输出对应的结果
#   如: n=3,a=2; 输出 2 + 22 + 222 的值。（****）
#   如: n=4,a=3; 输出 3 + 33 + 333 + 3333的值。
# 提示: 1、n = 3,相加三次,每次相加比前一次相加的数,多一位
#      2、每次多的这个位数的值为a,  3, 3*10+3(33), 33*10+3(333),...
n = int(input('输入一个n'))
a = int(input('输入一个a'))
s = 0
s2 = 0
for i in range(n):
    s += a * 10 ** i
    s2 += s
print(s2)

# 3,  输入两个数，求两个数的最大公约数（*****）
#         如: 12和8的最大公约数是4,
#         提示: 能够同时整除两个数的最大数
#          1, 先找出两个数中最小的那个数,
#          2, 最小数--, 找出能被两个数整除的数(退出循环break)
num1 = int(input('输入一个数'))
num2 = int(input('输入另一个数'))
m = 0
if num1 < num2:
    m = num1
else:
    m = num2
for i in range(m - 1, 1, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        break
else:
    print('这两个数没有公约数')

# 4,  输入两个数，求两个数的最小公倍数（****）
#         如: 9和6的最小公倍数是18,
#          1, 先找出两个数中的最大数
#          2, 最大数++，找出能被两个数整除的数(退出循环break)
num1 = int(input('输入一个数'))
num2 = int(input('输入另一个数'))
m = 0
if num1 > num2:
    m = num1
else:
    m = num2
while True:
    m += 1
    if m % num1 == 0 and m % num2 == 0:
        print(f'{m}是最小公倍数')
        break
num1 = int(input('输入一个数'))
num2 = int(input('输入另一个数'))
m = 0
n = 1
if num1 > num2:
    m = num1
else:
    m = num2
while True:
    m *= n
    n += 1
    if m % num1 == 0 and m % num2 == 0:
        print(f'{m}是最小公倍数')
        break
# 5, 宰相的麦子：相传古印度宰相达依尔，是国际象棋的发明者。有一次，国王因为他的贡献要奖励他，问他想要什么。
# 达依尔说：“只要在国际象棋棋盘上（共64格）摆上这么些麦子就行了：第一格一粒，第二格两粒，……，
# 后面一格的麦子总是前一格麦子数的两倍，摆满整个棋盘，我就感恩不尽了。”国王一想，这还不容易，
# 刚想答应，如果你这时在国王旁边站着，你会不会劝国王别答应，为什么？
# 不会 因为:
s = 0
for i in range(64):
    s += 2 ** i
print(f'国王付不起{s}粒的米')

# 丈母娘要彩礼
#   第1天  1分
#   第2天  2分
#   第3天  4分
#   第4天  8分
# ...
#   第30天 2^29分

print(2 ** 29)  # 536 8709.12

s = 0
for i in range(30):
    s += 2 ** i

print(s)  # 1073 7418.23
