# 输出

print(100)
print(100, 200, 300)  # 同时输出多个值
print(100, '你好')
# print(100 200) # 报错, 不可以这样写
# 注释快捷键: ctrl + /

# end = '\n'
# '\n' 表示换行符
print(1000, end='=======')
print(2000)

# sep= ' ' 分隔符
print(100, 200, 300, sep='+++')

# 输入
# input: 会让程序暂停(会阻塞),需要在控制台输入内容,然后按enter键.
# input(): 得到的一定是一个字符串类型.
# input : 只要输入的是数字,我们就是用int().
# age 是一个变量名.
# = 是一个赋值符号.
age = input('请输入您的年龄:')
print(age)  # '16'

# type() : 查看类型
print(type(age))  # <class 'str'>
print(type(int(age)))  # <class 'int'>
print()

# int() : integer 转换成整数
print(int(age) + 10)
# str() : string 转换成字符串
print(age + str(10))  # '16' + '10' = '1610' 字符串拼接
print('强东' + '奶茶妹妹')  # '强东奶茶妹妹'

print('end')

# 如果输入的是整数,则使用int()
age2 = int(input("请输入一个数字:"))
print(age2, type(age2))
# 15 <class 'int'>

