# 元组: tuple
#   是一个不可改变的列表

# 基本操作
# 1.创建元组
t = ()  # 空元组
t = (1,)  # 一个元素的元组
t = (1, 2, 3, 'hello')
print(t, type(t))

# 2.索引
t = (1, 2, 3)
print(t[0])  # 1
print(t[1])  # 2
print(t[2])  # 3
# print(t[3])  # 报错
print(t[-1])  # 3

# 3.长度
print(len(t))

# 4.遍历
for n in t:
    print(n)

for i in range(len(t)):
    print(i)
    print(t[i])

for i, n in enumerate(t):
    print(i, n)

# 5.重复
print(t * 3)

# 6.切片
t = (1, 2, 3, 4, 5, 6)
print(t[3:6])
print(t[::-1])

# 7.合并
print(((1, 2, 3) + (4, 5, 6)))

# 8.判断成员 in, not in
print(3 in t)

# 其他功能
# 增删改查: 增删改都不可用
t = (1, 2, 3, 6, 5, 4)

# 排序: sorted() 返回一个列表
# 倒序: reversed()
# t2 = sorted(t)
# t4 = sorted(t, reverse=True)
t3 = reversed(t)
# print(t2)
# print(t4)

print(list(t3))

# 列表和元组之间的转换
print(list((1, 2, 3)))
print(tuple([1, 2, 3]))
# dict()
# set()
# bool()

print(int((3.14,)))

# 元组包含列表
t = (1, 2, [3, 4])
t[-1][-1] = 100

print(t)

# 快速取值
a, b = (3, 4)
a, b = [3, 4]
print(a, b)
