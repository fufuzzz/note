
# 算术运算符
# + - * / %(求余数.取模)
# //(取整数) **(幂,次方)
print(100 + 40)  # 140
print(100 - 40)  # 60
print(100 * 40)  # 4000
print(100 / 40)  # 2.5
print(100 % 40)  # 20
print(100 // 40)  # 2
print(-100 // 40)  # -3
print(10 ** 4)  # 10000

# 字符串里有限度的支持加法和乘法运算符

# 加法运算符: 只能用于两个字符串的数据,用来拼接两个字符串
print('hello' + 'world')  # 将多个字符串拼接为一个字符串
# print('18' + 1)  # 在Python里,数字和字符串之间,不能做加法运算

# 乘法运算符: 可以用于数字和字符串之间,用来将一个字符串重复多次

# print('hello' - 'yes')
# print('hello' * 'yes')

# 比较预算符: 关系运算符,得到的结果是一个bool类型: True/False
# > >= < <= == !=
print(10 > 4)  # True
print(10 >= 4)  # True
print(10 < 4)  # False
print(10 <= 4)  # False
print(10 == 4)  # False
print(10 != 4)  # True

# 字符串的比较
#   ASCII码
#       0~9 : 48~57
#       A~Z : 65~90
#       a~z : 97~122
print(10 == '10')  # False
print('a' > 'b')  # 97 > 98 False
# 从左往右一次比较每一个字母的大小,直到有一个字母能比较出大小则直接返回结果
print('abc' >= 'acb')  # False
print('ad' > 'adc')    # False

# 数字和字符串之间,做==运算的结果是False,做!=结果是True,不支持其他的比较运算符
# print('a' > 90)  # 不能比较
print('a' == 97)  # False
print('a' != 97)  # True


