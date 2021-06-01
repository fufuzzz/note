
# 逻辑运算符
#   and 并且,与
#   or  或者,或
#   not 非,取反

# and 且,与
#   两边都会True则为True,只要有一个为False则为False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or 或
#   两边都为False则为False,只要有一个为True则为True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # True

# not 非
print(not True)  # False
print(not 0)  # True
print(not '')  # True
print(not ' ')  # False
print(not None)  # False
print(not [])  # True
print(not {})  # True


# bool(记住)
#  数字: 0是假,其它为真
#  字符串: 空字符串("")是假,其他为真
#  None: None是假
#  list: 空列表([])是假
#  dict: 空字典({})是假

#  短路操作
print('*' * 100)

# and  隐式判断
#   两边都为True则为True,只要有一个为False则为False
a = 0 and 4  # a=0
a = 3 and None and 6  # None
a = 2 and print('hello')
print(a)

# or
#   两边都为False则为False,只要有一个个True则为True
b = 2 or 5
b = 2 or print('hello')

print(b)

# 练习
x = 5 and True
y = 3 or False
result = x * 2 + y
print(result)

# 逻辑运算的结果,一定是布尔值吗? 不一定
# 逻辑与运算做取值是,取第一个为False的值; 如果所有的运算数都为True,取最后一个值
print(3 and 5 and 0 and 'hello')  # 0
print('good' and 'yes' and 'ok' and 100)  # 100

# 逻辑或运算做取值时,取第一个为True的值;如果所有的运算数都是False.取最后一个值
print(0 or [] or 'list' or 5 or 'ok')  # list
print(0 or [] or {} or ())  # ()
