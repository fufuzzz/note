l1 = [1, 2, 3, 1, 1, 1]

for i in range(l1.count(1)):
    l1.remove(1)
print(l1)

list1 = [2, 3, 4, 5, -6, 7, 8, 1]
# 交换: a, b  = b, a
a = list1.index(max(list1))
b = list1.index(min(list1))
list1[a], list1[0] = list1[0], list1[a]
list1[b], list1[-1] = list1[-1], list1[b]
print(list1)

list2 = ["One", "Two", "Three"]
list3 = list2 + list(reversed(list2))
print(list3)



list2 = ["One", "Two", "Three"]
list3 = list2
list2.reverse()
list3 += list2
print(list3)

list3 = [6, 4, 7, 2, 5, 8]
n = 10
for i in range(len(list3)):
    for j in range(i, len(list3)):
        if list3[i] + list3[j] == n:
            print(list3[i], list3[j])

list1 = [2, 3, 4, 56, 67, 98]
list1.append(63)
list1.append(100)
list1.sort()
print(list1)


list1 = [1, 2, 5, 2, 3, 5, 4, 4, 4, 5, 5, 3, 2, 1, 9, 7]
print(list1)
for i in list1:
    for j in list1:
        if i == j:
            list1.remove(j)
print(list1)

ages = [1, -2, 3, -4, 2, 1]

num = ages[0]
for n in ages:
    if n < num:
        num = n
print(num)

list1 = [33, 44, 88, 89, 33, 66, 77, 90, 44, 55]
num = list1[0]
x = 0
for i in range(len(list1)):
    if list1[i] > num:
        num = list1[i]
        x = i
print(x, num)

list1 = [33, 44, 88, 89, 33, 66, 77, 90, 44, 55]
num = list1[0]
x = 0
for i in range(len(list1)):
    if list1[i] > num:
        num = list1[i]
        x = i
list1.pop(x)
print(list1)
num2 = list1[0]
for i in range(len(list1)):
    if list1[i] > num2:
        num = list1[i]
        x = i
print(x, num)

list1 = [33, 44, 88, 89, 33, 66, 77, 90, 44, 55]
num1 = list1[0]
num2 = list1[0]
s = 0
for i in range(len(list1)):
    if list1[i] > num1:
        num1 = list1[i]
list1.remove(num1)
for i in range(len(list1)):
    if list1[i] < num2:
        num2 = list1[i]
list1.remove(num2)
for n in list1:
    s += n
s /= len(list1)
print(f'平均分{s}')

scores2 = [66, 77, 88, 99, 100]

num1 = scores2[0]
num2 = scores2[0]
s = 0
avg = 0
for i in range(len(scores2)):
    if scores2[i] > num1:
        num1 = scores2[i]
print(f'最大成绩{num1}')
for i in range(len(scores2)):
    if scores2[i] < num2:
        num2 = scores2[i]
print(f'最大成绩{num2}')
for n in scores2:
    s += n
print(f'平均分{s}')
avg = s / len(scores2)
print(f'平均分{avg}')

scores2 = [66, 77, 88, 99, 100]
for i in range(len(scores2)-1, -1, -1):
    print(scores2[i], end=' ')
print()
print(scores2[::-1])


import random
print('''
-----------------------------
请输入你的选择(1/2/3):
1. 石头
2. 剪刀
3. 布
-----------------------------
''')
# 石头 > 剪刀
# 剪刀 > 布
# 布 > 石头
computer = random.randint(1, 3)
me = int(input())
if me - computer == -1 or me - computer == 2:
    print('恭喜你赢了')
elif me == computer:
    print("平手")
else:
    print('你输了')

print(computer)

