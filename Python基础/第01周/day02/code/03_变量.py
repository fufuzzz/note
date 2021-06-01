# 变量: variable
# age : 变量名称
# =   : 赋值(将10赋值给age变量)
# ==  : 相等
# 10  : 一个值
age = 10
print(age)

# 变量可以重复定义
age = 20
print(age)

# 连续赋值
a = b = 10
print(a, b)

# 分别对x,y赋值
x, y = 10, 20
print(x, y)

c = 3; d = 4
print(c, d)

# 交换两个变量的值
a = 3
b = 4

# 第一种方式交换(掌握)
# a, b = b, a

# 第二种方式(了解)
# c = a
# a = b
# b = c

# 第三种方式(扩展)
# a = a + b
# b = a - b
# a = a - b

# 第四种方式(扩展): 位运算
a = a ^ b
b = a ^ b
a = a ^ b

print('a =', a, ', b =', b)


# 变量命名规范
#   规则(2点,必须遵守)
#       1.由数字,字母,下划线,且不能以数字开头
#       2.不能使用关键字
#   规范(3点,建议遵守)
#       1.区分大小写,比如:age和AGE是两个不同的变量,不建议用大小写区分两个变量
#       2.尽量见名知意,比如:age表示年龄,user_list来表示多个用户的列表
#       3.多个单词之间使用下划线连接:my_person
#               大驼峰:MyPerson, 小驼峰:myPerson

ageABC_123 = 10
# 123abc = 10

# 关键字
import keyword
print(len(keyword.kwlist))  # len() : length 长度,列表中的元素个数
'''
    ['False', 'None', 'True', 'and', 'as',
    'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else',
    'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 
'''

false = 10

# 删除变量
# del false
# print(false)

# Python是动态数据类型(弱类型)语言
# 强类型: c, c++, java
# 弱类型: Python, PHP, JavaScript

a = 10
print(type(a))
a = 'hello'
print(type(a))

