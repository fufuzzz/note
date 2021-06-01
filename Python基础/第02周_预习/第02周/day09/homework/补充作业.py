# # 先输出提示语句,并接收用户输入的年、月
#
# year, month = eval(input('请输入年、月'))
# a = ''
# D = 0
# E = 0
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     a = True
#     days = 366
# else:
#     a = False
#     days = 365
# if month == 4 or month == 6 or month == 9 or month == 11:
#     day = 30
# elif a == True and month == 2:
#     day = 29
# elif a == False and month == 2:
#     day = 28
# else:
#     day = 31
# for i in range(1900, year):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         D += 366
#     else:
#         D += 365
# print(D)
# for i in range(1, month):
#     if i == 4 or i == 6 or i == 9 or i == 11:
#         E += 30
#     elif a == True and i == 2:
#         E += 29
#     elif a == False and i == 2:
#         E += 28
#     else:
#         E += 31
# print(E)
# print(D + E)
# # print(365+365+365+366+365)
# G = (D + E+1 ) % 7
# print(G)
#
# print(' 星期日 ', ' 星期一 ', ' 星期二 ', ' 星期三 ', ' 星期四 ', ' 星期五 ', ' 星期六 ', end='\t')
# print()
# for i in range(G):
#     print('    ', end='\t')
# for j in range(1, day + 1):
#     print(f'   {j}', end='\t')
#     G += 1
#     if G % 7 == 0:
#         print()


# # a.输入年月
# def fa():
#     year, month = eval(input('请输入年、月'))
#     return year, month
#
#
# # b.判断闰年:
# def fb(y):
#     return y % 4 == 0 and y % 100 != 0 or y % 400 == 0
#
#
# # c.判断某月的总天数
# def fc(y, m):
#     days = 31
#     if m == 2:
#         if fb(y):
#             days = 29
#         else:
#             days = 28
#     elif m in [4, 6, 9, 11]:
#         days = 30
#     return days
#
#
# # d.计算当前年距离1900年1月1日的总天数
# def fd(y):
#     s = 0
#     for i in range(1900, y):
#         if fb(i):
#             s += 366
#         else:
#             s += 365
#     return s
#
#
# # e.当前月距离当前年的1月1日总共多少天
#
# def fe(y, m):
#     s = 0
#     for i in range(1, m):
#         s += fc(y, i)
#     return s
#
#
# # f. d+e
# def ff(y, m):
#     return fd(y) + fe(y, m)
#
#
# # g. 计算星期几
# def fg(y, m):
#     days = ff(y, m)
#     week = (days+ 1) % 7
#     return week
#
#
# # h.格式化输出日历
# def fh(y, m):
#     week = fg(y, m)
#     print(week)
#     print('星期日', ' 星期一', '星期二', '星期三', '星期四', '星期五', '星期六', sep='\t')
#     # 先打印空格
#
#     for i in range(week):
#         print(' ', end='\t\t')
#     for i in range(1, fc(y, m) + 1):
#         print(i, end='\t\t')
#
#         if (week+i) % 7 == 0:
#             print()
#
# def fa():
#     year, month = eval(input('请输入年、月'))
#
#     fh(year, month)
#
#
# fa()
