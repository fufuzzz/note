# 1.x 为 0-99 取一个数,y 为 0-199 取一个数,
#   如果 x>y 则输出 x的值，
#   如果 x 等于 y 则输出 x+y的值，
#   否则输出y的值
import random  # 随机数
# n = random.randint(1,6)  # 随机取1~6中的某一个整数
x = random.randint(0, 99)  # 随机取0~99中的某一个整数
y = random.randint(0, 199)  # 随机取0~199中的某一个整数
if x > y :
    print('x:', x)
elif x == y:
    print('x+y:', x+y)
else:
    print('y:', y)

# 2.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
# # 该数的每一位的立方和等于自身的值,比如:153=1^3+5^3+3^3
# # 	例如：153=1^3+5^3+3^3
# # 	n = 153:
# # 	个位：n%10
# # 	十位：(n//10)%10
# # 	百位：n//100

# n = int(input('输入一个三位数:'))
# baiwei = n // 100
# shiwei = n // 10 % 10
# gewei = n % 10
# if (baiwei**3 + shiwei**3 + gewei**3) == n:
#     print(n, '是水仙花数', sep='')
# else:
#     print(n, '不是水仙花数', sep='')

# 3.从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
#  回文数: 对称的5位数
# 	例如：11111   12321   12221

# n = int(input('输入一个五位数'))
# if (n // 10000) == (n % 10):
#     if (n // 1000 % 10) == (n // 10 % 10):
#         print(n, '是一个回文数')
#     else:
#         print(n, '不是回文数')
# else:
#     print(n, '不是回文数')

# 4.从控制台输入两个数，输出较大的值
# a = int(input('输入一个数'))
# b = int(input('输入另一个数'))
# if a > b:
#     print('较大值a:', a)
# else:
#     print('较大值b:', b)


# 5,成绩判定
# 	大于85 优秀
# 	大于等于75小于等于85 良好
# 	大于等于60小于75 及格
# 	小于60  不及格

# grade = int(input('输入成绩'))
# if grade > 85:
#     print('成绩优秀')
# elif grade >= 75:
#     print('成绩良好')
# elif grade >= 60:
#     print('成绩及格')
# else:
#     print('成绩不及格')

''' 进阶题 '''
# 1,判断一个年份是闰年还是平年；
#  （1.能被4整除而不能被100整除.（如2004年就是闰年,1800年不是.）
#   2.能被400整除.（如2000年是闰年））

# year = int(input('输入一个年份'))
# if year % 4 == 0 and year % 100 != 0:
#     print(year, '是闰年')
# elif year % 400 ==0:
#     print(year, '是润年')
# else:
#     print(year, '不是闰年')

# 2,输入一个月份，然后输出对应月份有多少天，将天数输出(不考虑闰年)
# 比如：
# 输入 6 输出为30
# 输入 2 输出为28

# month = int(input('输入一个月份'))
# if month in [1, 3, 5, 7, 8, 10, 12]:
#     print(month, '月有31天')
# elif month == 2:
#     print(month, '月有28天')
# else:
#     print(month, '月有30天')

# 3. 开发一款软件，根据公式（身高-108）*2=标准体重，可以有10斤左右的浮动。
# 来观察测试者体重是否合适, 输入真实身高(cm)，真实体重(斤)

# high = float(input('输入身高'))
# weight = float(input('输入体重'))
# b = (high - 108) * 2
# if (b - weight) <= 10 or (b - weight) >= -10:
#     print('身高', high, '体重', weight, '是合适的')
# else:
#     print('身高', high, '体重', weight, '不是合适的')

# 4.模拟玩骰子游戏，根据骰子点数决定什么惩罚【例如：1.跳舞，2.唱歌....】
# import random
# n = random.randint(1,6)
# if n == 1:
#     print('跳舞')
# elif n == 2:
#     print('唱歌')
# elif n == 3:
#     print('深蹲')
# elif n == 4:
#     print('奔跑')
# elif n == 5:
#     print('仰卧起坐')
# else:
#     print('倒立')

''' 挑战题 (选做) '''
# 1.分别输入某年某月某日，判断这一天是这一年的第几天？（考虑闰年） (*****)
#     year, month， day
#     提示： 使用多个if单分支
# year = int(input("年:"))
# moth = int(input("月:"))
# day = int(input("日:"))
#
# z = year % 4
# y = year % 100
# x = year % 400
# if (z==0 and y!=0) or x == 0:
#     if moth == 1:
#         days = day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 2:
#         days = 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 3:
#         days = 31 + 29 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 4:
#         days = 31 + 29 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 5:
#         days = 31 + 29 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 6:
#         days = 31 + 29 + 31 + 30 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 7:
#         days = 31 + 29 + 31 + 30 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 8:
#         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 9:
#         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 10:
#         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 11:
#         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 12:
#         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
# else:
#     if moth == 1:
#         days = day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 2:
#         days = 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 3:
#         days = 31 + 28 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 4:
#         days = 31 + 28 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 5:
#         days = 31 + 28 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 6:
#         days = 31 + 28 + 31 + 30 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 7:
#         days = 31 + 28 + 31 + 30 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 8:
#         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 9:
#         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 10:
#         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 11:
#         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
#         print('这一天是一年的第', days, '几天')
#     elif moth == 12:
#         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day
#         print('这一天是一年的第', days, '几天')

# 2,输入一个时间，输出该时间的下一秒： (*****)
# 	如：23:59:59，
# 	输入：hour, min, sec
# 	输出 0: 0: 0
hour = int(input("时:"))
min = int(input("分:"))
sec = int(input("秒:"))
if hour <=23 and min <= 59 and sec <= 59:
    if sec + 1 <= 59:
        sec2 = sec + 1
    else:
        sec2 = 0
        min = min + 1
    if min <= 59:
        min2 = min
    else:
        min2 = 0
        hour = hour + 1
    if hour <= 23:
        hour2 = hour
    else:
        hour2 = 0
    print(hour2, min2, sec2)
else:
    print('输入的时间不合法')
