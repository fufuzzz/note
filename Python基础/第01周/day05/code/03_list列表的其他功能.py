
# index() : 查找列表中第一次出现指定元素的下标,如果不存在则报错

l = [1, 2, 3, 4, 5, 3, 5, 5, 5, 6]
print(l.index(5))  # 4
print(l.index(5, 5,9))
# print(l.index(55))  # 报错

# copy(): 复制/拷贝
# 数据类型:
#   基本类型/不可变类型: int, float, str, bool, tuple, None
#   应用类型/可变类型: list, dict, set

# 赋值问题
# 基本类型/不可变类型: 简单赋值,没有关联
a = 100
b = a
a = 99
print(a, b)  # 99 100

# 引用类型/可变类型: 有关联
l1 = [1, 2, 3]
l2 = l1
l1[1] = 999
print(l1, l2)  # [1, 2, 3] [1, 2, 3]


# 拷贝
# 浅拷贝/浅拷贝
l1 = [1, 2, 3]
l2 = l1.copy()
l1[1] = 999
print(l1, l2)  # [1, 999, 3] [1, 2, 3]

l1 = [1, 2, [3, 4]]
l2 = l1.copy()  # 拷贝第一层
l1[-1][-1] = 999
print(l1, l2)   # [1, 2, [3, 999]] [1, 2, [3, 999]]

# 深拷贝
import copy

l1 = [1, 2, [3, 4]]
l2 = copy.deepcopy(l1)  # 拷贝所有的层
l1[-1][-1] = 999
print(l1, l2)  # [1, 2, [3, 999]] [1, 2, [3, 4]]


# 排序
# sort(): 升序,会改变原列表
# sort(reverse=True): 降序,也会改变原列表
ages = [4, 5, 3, 2, 8, -8]
# ages.sort()  # [-8, 2, 3, 4, 5, 8]
ages.sort(reverse=True)  # [8, 5, 4, 3, 2, -8]
print(ages)

# sorted(): 升序,不会改变原列表
ages = [4, 5, 3, 2, 8, -8]
# ages2 = sorted(ages)  # [-8, 2, 3, 4, 5, 8]
ages2 = sorted(ages, reverse=True)  # 降序 [8, 5, 4, 3, 2, -8]
print(ages)  # [4, 5, 3, 2, 8, -8]
print(ages2)

# reverse(): 倒序/逆序/翻转/反转
#   切片: [::-1]
# reversed(): 倒序,不会改变原列表
ages = [4, 5, 3, 2, 8, -8]
print(ages[::-1])  # [-8, 8, 2, 3, 5, 4]
print(ages)

ages.reverse()
print(ages)
ages = [4, 5, 3, 2, 8, -8]
print(list(reversed(ages)))
