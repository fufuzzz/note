# num1 = int(input('输入一个整数'))
# num2 = int(input('输入另一个整数'))
# if abs(num1 - num2) % 2 == 0:
#     print('结果不是奇数')
# else:
#     print(abs(num1 - num2))


for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=' ')
print()

n = 0
while n <= 100:
    if n % 2 == 0:
        print(n, end=' ')
    n += 1
print()

n = 3000
i = 0
while n >= 5:
    n /= 2
    i += 1
print(i)

for i in range(1, 101):
    if i % 3 == 0 or i % 10 == 3:
        print(i)
print('-' * 50)

for i in range(0, 101):
    if i % 3 == 0 and i % 10 == 2:
        print(i)

# n = int(input('输入一个正整数'))
# count = 0
# while n:
#     n = n // 10
#     count += 1
# print(count)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(10):
            if i**3 + j**3 + k**3 == i*100 + j*10 + k:
                print(i*100 + j*10 + k)

# n = 1
# while n:
#     n = int(input('输入一个数'))
#
# n = 0
# for i in range(101, 201):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         n += 1
#         print(j, end=' ')
# print()
# print(f"101-200中有{n}个素数")


# 1+1 2
# 1+2 3
# 2+3 5
# 3+5
# 5+8
# 8+13

n = int(input('输入一个n'))
a = [1, 1, 1]
for i in range(n-2):
    a[2] = a[0] + a[1]
    a[0] = a[1]
    a[1] = a[2]
print(a[2])
# n = 0.00008
# count = 0
# while n <= 8848.13:
#     n *= 2
#     count = count + 1
# print(count)
#
# for i in range(1,35):
#     for j in range(1, 51):
#         for k in range(1, 201):
#             if i*3 + j*2 + k*0.5 == 100 and i + j + k == 100:
#                 print(f'有{i}匹大马,{j}匹中马,{k}匹配小马')
