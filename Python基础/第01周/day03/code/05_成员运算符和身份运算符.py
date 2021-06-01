
# 成员运算符
# in, not in
print(3 in [1, 2, 3])  # True
print(4 not in [1, 2, 3])  # True


# 判断某个月份是否是31天
month = 3
# print(month == 1 and month==3....)
print(month in [1, 3, 5, 7, 8, 10, 12])  # True


# 身份运算符: 了解
# is, is not
# 作用: 判断内存地址是否相同
a = 100
b = 100
print(id(a))  #
print(id(b))

# id() : 查看内存地址

print(a is b)  # True
print(a is not b)  # False
