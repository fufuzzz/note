# 集合: set
#   1.唯一
#   2.无序

# 1. 创建集合
# s = {} # 字典
s = set()  # 空集合
s = {1, 1, 1, 2, 2, 3, 2, 3}
# s = {'a', 'b', 'c', [1]}  # 报错
s = {'a', 'b', 'c'}
print(s, type(s))

# 2.查: 遍历
for n in s:
    print(n)

# 3.长度
print(len(s))  # 3

# 重复不行

# 其他功能
# 增
s = {1, 2, 3}
s.add(4)
s.update([5, 6])
print(s)
# 删除
# s.pop()  无序
# s.remove(3)
# s.discard(33)
s.clear()
print(s)

# 集合之间的关系
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 & s2)  # 交集, {3, 4}
print(s1 | s2)  # 并集, {1, 2, 3, 4, 5, 6}
print(s1 - s2)  # 差集, {1, 2}
print(s2 - s1)  # 差集, {5, 6}
print(s1 ^ s2)  # 对称差集,{1, 2, 5, 6}
print(s1 > s2)  # s1是否包含s2, False
print(s1 < s2)  # s2是否包含s1, False

# 去重:去除重复元素
# set() 转成集合
# list() 转成列表
list1 = [1, 1, 4, 1, 2, 3, 4, 4, 4, 3, 2, 66, 7, 9]
print(list(set(list1)))
#
n = 0
i = 20
while i <= 80:
    while n < 5:
        if i % 3 == 0:
            print(i)
            i += 1
            n += 1