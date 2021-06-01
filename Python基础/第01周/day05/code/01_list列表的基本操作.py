
# 列表: list, (数组array)
# 作用: 一般用来保存多个相同类型的数据,可以批量处理

# 变量
#   用变量保存品牌包
a = 'lv'
b = '蔻驰'
c = '爱马仕'
d = '香奈儿'
# 如果有100个包的品牌呢?
# 我们应该用列表来存储
bags = ['lv', '蔻驰', '爱马仕', '香奈儿']

# 1.创建列表
ages = [11, 22, 33]
# ages2 = [11, 'hello', True]  # 可以保存不同类型的元素,但是不推荐

# 2.如何获取元素: 索引/下标
print(ages[0])  # 11 从0开始
print(ages[1])  # 22
print(ages[2])  # 33
# print(ages[3])  # 报错:下标越界,IndexError: list index out of range
print(ages[-1])  # 倒数第一个
print(ages[-2])  # 倒数第二个

# 3.列表长度:列表元素个数
print(len(ages))

# 4.遍历列表
ages = [11, 22, 33]
for n in ages:
    print(n)  # 元素

for i in range(len(ages)):
    print(i, ages[i])  # 下标,元素

# 枚举/列举:同时得到下标和元素
for i, n in enumerate(ages):
    print(i, n)

# 从后往前遍历
for i in range(len(ages)-1, -1, -1):
    print(i, ages[i])

# 5.切片 !!!
ages = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(ages[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(id(ages), id(ages[:]))  # 内存地址不一样
print(ages[3:])  # [4, 5, 6, 7, 8, 9]
print(ages[:3])  # [1, 2, 3]
print(ages[3:6])  # [4, 5 ,6] 下标范围:[3, 6)
print(ages[::-1])  # 倒序,逆序 [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(ages[::2])  # [1, 3, 5, 7, 9]
print(ages[7:1:-2])  # [8, 6, 4]


# 6.重复  *
print([1, 2, 3] * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 7.判断元素是否存在 in
print(3 in ages)  # True
print(3 not in ages)  # False

# 8.列表合并 +
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]

# 9.删除列表或元素
# del ages
# print(ages)


# del ages[0]
# print(ages)  # [2, 3, 4, 5, 6, 7, 8, 9]

del ages[2:5]
print(ages)  # [1, 2, 6, 7, 8, 9]
