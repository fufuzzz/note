# 迭代器, 可迭代对象

from collections.abc import Iterable, Iterator

# 可迭代对象:
# type(): 查看数据类型
print(type(100))  # <class 'int'>

# isinstance():
print(isinstance(10, int))  # True
print(isinstance('hello', (int, float, str, list)))  # True
print()

# 可迭代对象: 可以使用for-in循环
print(isinstance(10, Iterable))  # False
print(isinstance(True, Iterable))  # False
print(isinstance(True, Iterable))  # False
print(isinstance(None, Iterable))  # False

print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance({1}, Iterable))  # True
print(isinstance('abc', Iterable))  # True
print(isinstance((i for i in range(2)), Iterable))  # True

# 迭代器
print(isinstance(10, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance(True, Iterator))  # False
print(isinstance(None, Iterator))  # False
print('*' * 60)
print(isinstance([], Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance({1}, Iterator))  # False
print(isinstance('abc', Iterator))  # False
print(isinstance((i for i in range(2)), Iterator))  # True
g = (i for i in range(10, 13))
# iter(): 可迭代对象 => 迭代器
# list(): 迭代器 => 列表

l = [11, 22, 33]
t = iter(l)
print(g)

# # 用for-in
# for i in t:
#     print(i)

# 使用next
print(next(t))  # 11
print(next(t))  # 22
# print(next(t))  # 22

l2 = list(t)
print(l2)

s = lambda x, y: x + y
print(s(1, 2))