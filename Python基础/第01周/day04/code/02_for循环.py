
# for 循环


# range(): 取一个整数范围的一系列整数
print(list(range(5)))  # 范围:[0, 5),[0, 1, 2, 3, 4]
print(list(range(0, 5)))  # 范围:[0, 5),[0, 1, 2, 3, 4]
print(list(range(2, 8)))  # 范围:[2, 8)
print(list(range(1, 9, 2)))  # [1, 3, 5, 7]
print(list(range(9, 1, -1)))  # [9, 8, 7, 6, 5, 4, 3, 2]

# 5,4,3,2,1,0
print(list(range(5, -1, -1)))

# for-in
# 注意: in 的后面必须要是一个可迭代对象!!!
# 可迭代对象: 字符串、列表、字典、元组、集合、range
for i in 'hello':
    print(i)
# 1+2+3+...+100
s = 0
for i in range(1, 101):
    # print(i, end=' ')
    s += i
print('s =', s)

#  求1-100的偶数和
s = 0
for i in range(2, 101, 2):
    s += i
print('s =', s)

# 列表
ages = [13, 15, 17, 20]
for i in ages:
    print(ages)   # 列表中的元素

# 下表/索引: index
print(ages[0])   # 13 第一个元素
print(ages[1])   # 15 第二个元素
print(ages[2])
print(ages[3])

for i in range(0, 4):
    print(i, ages[i])

print(len(ages))  # ages元素个数

for i in range(0, len(ages)):  # [0, len(ages)]
    print(i, ages[i])

# 从后往前打印ages的元素

for i in range(len(ages)-1, -1, -1):
    print(i, ages[i])


# 1.求1-100之间可以被7整除的数的个数

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print('count =', count)

# 2.计算从1到100以内所有奇数的和。
s = 0
for i in range(1, 101, 2):
    s += i
print('s =', s)

# 3.计算从1到100以内所有能被3或者17整除的数的和。
s = 0
for i in range(1,101):
    if i % 3 == 0 or i % 17 == 0:
        s += i
print('s =', s)

# 4.计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数。
count = 0
for i in range(1, 101):
    if (i % 3 == 0 or i % 7 == 0) and i % 21 != 0:
        count += 1
print('count =', count)
# 5.计算1到500以内能被7整除但不是偶数的数的个数。
count = 0
for i in range(1, 501):
    if (i % 7 == 0) and i % 2 != 0:
        count += 1
print('count =', count)

# for循环的嵌套
for i in range(1, 6):
    for j in range(1, 6):
        print(i, '*', j, '=', i*j)

for i in range(1, 6):
    j = 1
    while j < 6:
        print(i, '*', j, '=', i*j)
        j += 1


# 输出以下图形,要求每次print只能输出一个*:

for i in range(4):  # 行
    for j in range(10):
        print('*', end='')
    print()

for i in range(1, 8):  # 行
    for j in range(i):
        print('*', end='')
    print()

# 打印九九乘法表

for i in range(1, 10):  # 行
    for j in range(1, i+1):
        print(str(j) + '*' + str(i) + '=' + str(i*j), end='\t')
    print()

