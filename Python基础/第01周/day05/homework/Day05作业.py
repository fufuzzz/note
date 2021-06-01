''''''

''' 基础题 '''
# 【注：以下6题功能全部自己使用循环实现，不能借助于Python内置函数: max, min, sort, reverse】

# 1.自定义一个数字列表，获取这个列表中的最小值
ages = [1, -2, 3, -4, 2, 1]

num = ages[0]
for n in ages:
    if n < num:
        num = n
print(num)

# max1 = 3
#
# m = ages[0]
# mindex = 0
#
# for i in range(len(ages)):
#     # if ages[i] == max1:
#     #     continue
#     if ages[i] < m:
#         m = ages[i]
#         mindex = i
#
# print(m, mindex)


# 2. 自定义一个数字列表，元素为10个 ,找出列表中最大数连同下标一起输出
list1 = [33, 44, 88, 89, 33, 66, 77, 90, 44, 55]
num = list1[0]
x = 0
for i in range(len(list1)):
    if list1[i] > num:
        num = list1[i]
        x = i
print(x, num)

for i, n in enumerate(list1):
    if n > num:
        list1 = n
        x = i
print(x, num)

# 3. 自定义一个数字列表，求列表中第二大数的下标
list1 = [90, 44, 88, 89, 33, 66, 77, 90, 44, 55]
num = list1[0]
x = 0
for i in range(len(list1)):
    if list1[i] > num:
        num = list1[i]

print('最大数:')
num2 = list1[0]
for n in list1:
    if n != num:
        num2 = n
for i in range(len(list1)):
    if list1[i] > num2:
        num = list1[i]
        x = i
print(x, num)

# 4. B哥去参加青年歌手大奖赛 ,有10个评委打分 ,(去掉一个最高分一个最低分)求平均分
scores = [33, 44, 88, 88, 33, 66, 77, 88, 44, 55]
# 1. 先找到最大数和最小数
# 2. 删除一个最高分和最低分 remove
# 3. sum / 8
num1 = scores[0]
num2 = scores[0]
s = 0
for i in range(len(scores)):
    if scores[i] > num1:
        num1 = scores[i]
scores.remove(num1)
for i in range(len(scores)):
    if scores[i] < num2:
        num2 = scores[i]
scores.remove(num2)
for n in scores:
    s += n
s /= len(scores)
print(f'平均分{s}')

# 5. 定义列表，存放5个学生的成绩【成绩值自己设定】，获得成绩之和，平均成绩，最小成绩，最大成绩。
scores2 = [66, 77, 88, 99, 100]

num1 = scores2[0]
num2 = scores2[0]
s = 0
avg = 0
for n in scores2:
    if n > num1:
        num1 = n
print(f'最大成绩{num1}')
for i in range(len(scores2)):
    if scores2[i] < num2:
        num2 = scores2[i]
print(f'最小成绩{num2}')
for n in scores2:
    s += n
print(f'总分{s}')
avg = s / len(scores2)
print(f'平均分{avg}')
# 6. 将一个列表逆序输出, 提示: range(6,-1,-1)
scores2 = [66, 77, 88, 99, 100]
for i in range(len(scores2) - 1, -1, -1):
    print(scores2[i], end=' ')

print(scores2[::-1])

import random

# 7.完成猜拳游戏
# 		-----------------------------
# 		请输入你的选择:
# 		1. 石头
# 		2. 剪刀
# 		3. 布
# 		-----------------------------
# 		如: 你的选择是【布】, 电脑的选择是【石头】
# 		恭喜你获得了胜利！

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

''' 进阶题:可以使用内置函数 '''
# 1.给定一个列表：将列表中指定的某个元素全部删除: count, remove
l1 = [1, 2, 3, 1, 1, 1]

for i in range(l1.count(1)):
    l1.remove(1)
print(l1)
# 2.自定义一个列表，最大的与第一个元素交换，最小的与最后一个元素交换，输出列表(不考虑特殊情况)
list1 = [2, 3, 4, 5, -6, 7, 8, 1]
# 交换: a, b  = b, a
a = list1.index(max(list1))
b = list1.index(min(list1))
list1[a], list1[0] = list1[0], list1[a]
list1[b], list1[-1] = list1[-1], list1[b]
print(list1)
# 3,对称列表. 传入一个列表，元素类型与个数皆未知，返回新列表，由原列表的元素正序反序拼接而成;
# 如传入["One", "Two", "Three"] 返回[“One”, “Two”, “Three” ,”Three” ,”Two”, “One”]
list2 = ["One", "Two", "Three"]
list3 = list2 + list(reversed(list2))
print(list3)

# list2.extend(list2.reverse())
# print(list2)
#
# print(list2 + list2[::-1])
#
#
# list3 = list2.copy()
# list2.reverse()
# list3 += list2
# print(list3)

# 4, 给定一个不存在重复元素的整数列表，例如[6 ,4 ,7 ,2 ,5 ,8]和一个数字，例如10，
# 找出两个元素(或同一个元素加自身)，并且使这两个数的和为给定数字，并打印出来
# 例如[6 ,4 ,7 ,2 ,5 ,8]和数字10. 打印结果为: 6,4  2,8  5,5
list3 = [6, 4, 7, 2, 5, 8]
n = 10
for i in range(len(list3)):
    for j in range(i, len(list3)):
        if list3[i] + list3[j] == n:
            print(list3[i], list3[j])

# 5,有一个从小到大排好序的列表。现输入一个数，要求按原来的规律将它插入列表中,
# 如: [2 ,3 ,4 ,56, 67 ,98]  如插入63, 100
list1 = [2, 3, 4, 56, 67, 98]
list1.append(63)
list1.append(100)
list1.sort()
print(list1)

# 方法二
# l5 = [2, 3, 4, 56, 67, 98]
# m = 63
# for i, n in enumerate(l5):
#     if n > m:
#         l5.insert(i, m)
# else:
#     l5.append(m)
# print(l5)

# 6,列表去重, 将下面的列表中重复的元素去除, 不能使用set()
# list1 = [1 ,2 ,3 ,5 ,4 ,4 ,4 ,5 ,5 ,3 ,2 ,1]

# list1 = [1, 2, 3, 5, 4, 4, 4, 5, 5, 3, 2, 1]
# n = len(list1)
# for i in range(0, n):
#     for j in range(0, n):
#         if list1[i] == list1[j]:
#             list1.pop(i)
#             n -= 1
# print(list1)

# list1 = [1, 2, 5, 2, 3, 5, 4, 4, 4, 5, 5, 1, 1, 3, 2, 1, 9, 7]
# print(list1)
# for i, n1 in enumerate(list1):
#     j = i + 1
#     for j, n2 in enumerate(list1):
#         if n1 == n2:
#             list1.pop(j)
# print(list1)


list1 = [1, 2, 5, 2, 3, 5, 4, 4, 4, 5, 5, 1, 1, 3, 2, 1, 9, 7]
list2 = []
for n in list1:
    if n not in list2:
        list2.append(n)
print(list2)

list1 = [1, 2, 5, 2, 3, 5, 4, 4, 4, 5, 5, 1, 1, 3, 2, 1, 9, 7]
i = 0
while i < len(list1):
    j = i + 1
    while j < len(list1):
        if list1[i] == list1[j]:
            list1.pop(j)
            j -= 1
        j += 1
    i += 1
print(list1)
