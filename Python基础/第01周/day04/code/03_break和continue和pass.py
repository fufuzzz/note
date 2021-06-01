
# break: 关键字
#   1.存在于循环中: for,while
#   2.可以立刻终止当前所在的这层循环
#   3.breake后面的代码不会再执行
#   4.可以和for-else,while-else一起结合使用

# 找出1~100中第一个能被6整除的数
for i in range(1, 101):
    if i % 6 == 0:
        print(i)
        break
        print('ok')  # 不会执行

for i in range(1, 4):
    for j in range(1, 4):
        if j == 3:
            break  # 只能跳出最里面的这层循环
        print(i, j)


# for-else
# 1.要和break结合使用
# 2.如果执行了break则不执行else,如果不执行break则执行else


# 1.给一个数,判断是不是一个质数（质数是只能被1和它自身整除的数）
n = 3753

# 思路: 遍历2~n~1中的每个数:
#   1.如果有某个数能被n除尽,就说明不是素数
#   2.如果中间的每个数都不会被n除尽,就说明是素数
for i in range(2, n):
    if n % i == 0:
        print(n, '不是质数')
        break
else:
    print(n, '是质数')

# while-else

i = 2
while i < n:
    if n % i == 0:
        print(n, '不是质数')
        break
    i += 1
else:
    print(n, '是质数')

# 不使用for-else

for i in range(2, n):
    if n % i == 0:
        print(n, '不是质数')
        break
if i == n-1:
    print(n, '是素数')

f = True
for i in range(2, n):
    if n % i == 0:
        print(n, '不是质数')
        f = False
        break
if f:
    print(n, '是质数')

# pass
#   1.空语句,占位语句
#   2.保证代码完整性,防止报错

# for i in range(1, 9):
#     pass
# print(i)

# contimue: 继续
#   1.在循环中使用
#   2.停止当次循环,直接进入下一次循环
#   3.continue后的代码不执行

# 打印1-10的每个值,跳过3的倍数的数
for i in range(1, 11):
    if i % 3 == 0:
        continue
        print('ok')
    print(i, end=' ')
print()

for i in range(1, 11):
    if i % 3 != 0:
        print(i, end=' ')
print()
for i in range(1, 11):
    if i % 3 == 0:
        pass
    else:
        print(i, end=' ')
print()


# for: 一般用于已知循环次数的情况,能用for的就用for
# while: 一般用于未知循环次数的情况(结合break), 死循环

m = 0
while m < 3:
    print(m)
    if m == 4:

        break
    m += 1
else:
    print("else")