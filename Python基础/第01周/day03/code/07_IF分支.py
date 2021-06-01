
# if分支
# 作用:分支结构,选择结构,可以分多钟情况执行不同的代码

# 3大结构
# 顺序结构
# 分支结构
# 循环结构

# 单分支: if
# age = 40
# sex = input('请输入张柏芝的性别')
# if sex == '女':
#     age = 18
#
# print(age)

if 1:
    print('hello 蔡徐坤')
    print('hello 蔡徐坤2')

# IF双分支
n = int(input('请输入一个整数:'))
if n % 2 == 0:
    print(n, '是偶数')
else:
    print(n, '是奇数')


# IF多分支: if-elif-else
# 判断成绩:
#   <0或>100: 输入不合法
#   60以下: 不及格
#   60~80: 良好
#   80~100: 优秀

score = int(input('请输入一个成绩:'))
if score < 0 or score > 100:
    print("输入成绩不合法")
elif score < 60:
    print('成绩不及格')
elif score <80:
    print('成绩良好')
else:
    print('成绩优秀')


# IF嵌套
if score >= 0 and score <= 100:
    if score < 60:
        print('不及格')
    elif score < 80:
        print('成绩良好')
    else:
        print('成绩优秀')
else:
    print('不合法')


# 输入2个数,得到较大的那个,并打印
a = int(input('输入一个数'))
b = int(input('输入另一个数'))
# 方法1:
if a > b:
    print('较大的数是:', a)
else:
    print('较大的数是:', b, sep='')

# 方法2:
c = a if a > b else b
print(c)
