''''''

'''
    for循环题目
'''
''' 基础题 '''
# 1,打印100以内7的倍数
for i in range(1, 101):
    if i % 7 == 0:
        print(i, end=' ')
print()
# 2,打印100以内的奇数
for i in range(1, 101, 2):
    print(i, end=' ')
print()

# 3,打印100以内所有偶数的和
for i in range(2, 101, 2):
    print(i, end=' ')
print()

# 4,判断一个数是不是合数。(指自然数中除了能被1和本身整除外，还能被其他的数整除（不包括0)的数。)
num = eval(input('输入一个数字'))
for i in range(2, num):
    if num % i == 0:
        print('这是一个合数')
        break

# 5,判断一个数是不是素数。(除了1和它本身以外不再有其他的除数整除。)
num = eval(input('输入一个数字'))
for i in range(2, num):
    if num % i == 0:
        break
else:
    print('这是一个素数')

# 6,求整数1～100的累加值，但要求跳过所有个位为3的数。
s = 0
for i in range(1, 101):
    if i % 10 == 3:
        continue
    s += i
print(s)

# 7, 一个新入职，月工资为2000元的员工，每年涨当年工资5%，20年后的月工资是多少？
s = 2000
for i in range(1, 21):
    s *= 1 + 0.05
print(s)

# 8, 山上有一口缸可以装50升水，现在有15升水。老和尚叫小和尚下山挑水，每次可以挑5升。
#    问：小和尚要挑几 次水才可以把水缸挑满？通过循环解决这个问题。
n = 15
count = 0
while n < 50:
    n += 5
    count += 1
print(count)

# 9, 打印100–200之间所有能被3或者7整除的数
for i in range(100, 201):
    if i % 3 == 0 or i % 7 == 0:
        print(i, end=' ')
print()
# 10, 计算10的阶乘(1*2*3*4*5*6*7*8*9*10, n的阶乘:1*2……*n)
# import math
# print(math.factorial(10))
x = 1
for i in range(1, 11):
    x *= i
print(x)
# 11, 计算1+3+5+...+99的和
# print(sum(range(1, 100, 2)))
s = 0
for i in range(1, 99, 2):
    s += i
print(s)
# 12, 输出20~80之间能被3整除的整数, 每行5个
n = 0

for i in range(20, 81):
    if i % 3 == 0:
        print(i, end=' ')
        n += 1
        if n % 5 == 0:
            print()
# 13, 打印1000~2000年中所有的闰年, 每行4个
n = 0
for i in range(1000, 2001):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i, end=' ')
        n += 1
        if n % 4 == 0:
            print()
print()
# 14, 求: 1-1/2+1/3-1/4 …  1/100的和
#   提示: 1/1-1/2+1/3-1/4 …  1/100
s = 0
for i in range(1, 100):
    s += 1 / i * ((-1) ** (i - 1))
    # print((-1)**(i-1))
print(s)
# 15, 输出99乘法表
'''
1 * 1 = 1
1 * 2 = 2	2 * 2 = 4
1 * 3 = 3	2 * 3 = 6	3 * 3 = 9
1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16
1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25
1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36
1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49
1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64
1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {i * j}', end=' \t')
    print()
'''
    字典题目
'''
# 1. 声明一个字典保存一个学生的信息，学生信息中包括:
#       姓名、年龄、成绩(单科)、电话、性别(男、女、不明)
stu_info1 = {'name': '宋亮亮', 'age': 19, 'score': 100, 'tel': 18866669998, 'sex': '女'}
stu_info2 = {'name': '游远东', 'age': 21, 'score': 100, 'tel': 17607042334, 'sex': '男'}
stu_info3 = {'name': '吴迪', 'age': 18, 'score': 88, 'tel': 18866669995, 'sex': '不明'}
stu_info4 = {'name': '张三', 'age': 18, 'score': 29, 'tel': 18866669992, 'sex': '不明'}
stu_info5 = {'name': '李四', 'age': 18, 'score': 10, 'tel': 18866669993, 'sex': '不明'}
stu_info6 = {'name': '王五', 'age': 17, 'score': 78, 'tel': 18866669994, 'sex': '不明'}

# 2. 声明一个列表，在列表中保存6个学生的信息(6个(题1)中的字典)
information = [stu_info1, stu_info2, stu_info3, stu_info4, stu_info5, stu_info6]
#   (1) 统计不及格学生的个数
count = 0
for n in information:
    if n['score'] < 60:
        count += 1
print(count)

#   (2) 打印不及格学生的名字和对应的成绩
for n in information:

    if n['score'] < 60:
        print(n['name'], n['score'])
#   (3) 统计未成年学生的个数
count = 0
for n in information:
    if n['age'] < 18:
        count += 1
print(count)
#   (4) 打印手机尾号是8的学生的名字
for n in information:
    if n['tel'] % 10 == 8:
        print(n['name'])

#   (5) 打印最高分和对应的学生的名字
# max1 = 0
# name2 = ''
# for n in information:
#     if n['score'] > max1:
#         max1 = n['score']
#         name2 = n['name']
# print(f'最高分是{max1}的人叫{name2}')
# max1 = information[0]['score']
#
# for n in information:
#     if n['score'] > max1:
#         max1 = n['score']
# for n in information:
#     if n['score'] == max1:
#         print(f'最高分是{max1}的人叫' + n['name'])

#   (6) 删除性别不明的所有学生(选做)
# for i in range(len(information) - 1, -1, -1):
#     if information[i]['sex'] == '不明':
#         information.pop(i)
# print(information)
#
# i = 0
# while i < len(information):
#     stu = information[i]
#     if stu['sex'] == '不明':
#         information.pop[i]
#         i -= 1
#     i += 1
#
# for stu in information:
#     print(stu)
#   (7) 将列表按学生成绩从大到小排序(难,选做)
# 提示:
# 方式一: 排序算法
# 方式二: sort(key=)

# information.sort(reverse=True, key=lambda x: x['score'])
# for stu in information:
#     print(stu)


for i in range(len(information)-1):
    for j in range(len(information)-1-i):
        if information[j]['score'] < information[j+1]['score']:
            information[j], information[j+1] = information[j+1], information[j]
for stu in information:
    print(stu)
