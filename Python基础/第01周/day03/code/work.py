# 1.假设本周的上课时间为156789秒，编程计算本周上课时间是多少天, 多少小时，多少分钟，多少秒；以‘XX天XX时XX分X秒’的方式表示出来。

time = 156789
day = time // (60*60*24)
hour = time // (60*60) % 24
minute = time // 60 % 60
second = time % 60
print(day,'天', hour, '时', minute, '分', second, '秒', sep='')

# 2.写出判断一个数是否能同时被3和7整除的条件语句, 并且打印对应的结果。

# num = int(input('输入一个数'))
# if num % 3 == 0 and num % 7 == 0:
#     print(num, '可以被3和7整除')
# else:
#     print('这个数不能被3和7整除')


# 3.写出判断一个数是否能够被3或者7整除，但是不能同时被3和7整除的条件语句， 并且打印对应的结果。

# num2 = int(input('输入一个数'))
# if num2 % 3 == 0 or num2 % 7 == 0:
#     if num2 % 21 != 0:
#         print(num2, '能够被3或者7整除，且不能同时被3和7整除')
#     else:
#         print(num2, '能够被3或者7整除,但是同时被3和7整除')
# else:
#     print(num2, '不能被3或者7整除')

# 4.定义两个变量保存一个人的身高和体重，编程实现判断这个人的身材是否正常!
# 公式: `体重(kg)/身高(m)的平方值` 在18.5 ~ 24.9之间属于正常。

# weight = float(input('输入体重'))
# high = float(input('输入身高'))
# a = weight / (high**2)
# if a >= 18.5 and a <= 24.9:
#     print('正常')
# else:
#     print('不正常')

