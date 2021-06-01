''''''

''' 基础题 '''
# 1. 输出10行内容，每行的内容都是“*****”。
for i in range(10):
    print('*' * 5)


# 2. 输出10行内容，每行的内容都不一样，第1行一个星号，第2行2个星号，依此类推第10行10个星号。
'''
*
**
***
..
*********
'''
# 方法一
for i in range(1, 11):
    print('*' * i)
# 方法二
for i in range(1, 11):
    for j in range(i):
        print('*', end='')
    print()

# 3. 输出9行内容，第1行输出1，第2行输出12，第3行输出123，以此类推，第9行输出123456789。
'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, sep='', end='')
    print()

j = 0
for i in range(1, 10):
    j = j * 10 + i
    print(j)

# 4. 计算10个99相加后的值并输出。
s = 0
for i in range(10):
    s += 99
print('s =', s)

# 5. 计算2的20次方。(要求使用for)
s = 1
for i in range(20):
    s *= 2
print('s =', s)

# 6. 计算从1到1000以内所有能被3或者17整除的数的和并输出
s = 0
for i in range(1, 1001):
    if i % 3 == 0 or i % 17 == 0:
        s += i
print('s =', s)

# 7. 计算从1到1000以内所有能同时被3，5和7整除的数的和并输出
s = 0
for i in range(1, 1001):
    if i % (3*5*7) == 0:
        s += i
print('s =', s)

''' 进阶题 '''

# 1. 计算从1到100临近两个整数的和依次输出。比如第一次输出3(1+2)，第二次输出5(2+3)，最后一次输出199(99+100)。
'''
3 5 7 9 11 13
'''

for i in range(1, 100):
    s = 0
    s += i + i+1
    print('s =', s)

# 2. 给定一个不大于9的数n，打印nn乘法表
n = int(input('给定一个不大于9的数'))
for i in range(1, n+1):
    for j in range(1, i+1):
        # print('{a}*{b}={c} '.format(a=j, b=i, c=i*j), end='\t')
        print(f'{j}*{i}={i*j} ', end='\t')
    print()

''' 挑战题 '''
# 1. 给定一个n位（不超过10）的整数，将该数按位逆置，例如给定12345变成54321，12320变成2321.(*****)
n = int(input('给定一个n位(不超过10)的整数'))
s = 0
s2 = 0
s3 = ''
while n:
    a = n % 10
    # print(a, end='')
    s += a * (10 ** (len(str(n)) - 1))
    s2 = s2 * 10 + a
    s3 += str(a)
    n = n // 10
print(s)
print(s2)
print(s3, int(s3))

# 2. 一球从100米高度自由落下，每次落地后反跳回原高度的一半，再落下。求它在第n次落地时，共经过多少米？(*****)
#   规律:
#       第1次落地: 100
#       第2次落地: 100 + 50*2
#       第3次落地: 100 + 50*2 + 25*2
#       第4次落地: 100 + 50*2 + 25*2 + 12.5*2
#       第5次落地: 100 + 50*2 + 25*2 + 12.5*2 + ...
height = 100.0
s = 100.0
n = float(input('输入第n次:'))
while height > (100/2**(n-1)):
    height /= 2  # 50 25 12.5
    s += height*2
print('共经过多少米:', s)

height = 100
s = 100
n = int(input('输入第n次:'))
# if n == 1:
#     print('共经过多少米:', s)
# else:

for i in range(2, n+1):
    height /= 2
    s += height * 2


print('共经过多少米:', s)


# 3. 已知 abc+cba=1333, 其中的a,b,c均为一位数，编写一个程序，求出a,b,c分别代表什么数字 (*****)
# a*100+b*10+c+a+b*10+c*100=1333
# 101*a+20*b+101*c =1333

# for a in range(10):
#   for b in range(10):
#       for c in range(10):
#           ..

for a in range(10):
    for b in range(10):
        for c in range(10):
            if 101 * a + 20 * b + 101 * c == 1333:
                print(f'a:{a}, b:{b}, c:{c}')




import time
s = time.time()  # 当前时间

for i in range(1000000):
    pass

e = time.time()  # 当前时间

print(e - s)


