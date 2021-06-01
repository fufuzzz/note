''''''

'''
【以下功能都使用函数封装】
提示: 涉及到要返回的题目,请使用return
'''

''' 基础题 '''


# 1.封装函数，计算从1到某个数以内所有奇数的和并返回
def count1(n):
    s = 0
    for i in range(1, n + 1, 2):
        s += i
    return s


print(count1(50))


# 2.封装函数，判断某个数是否是偶数，返回结果(True或False)
def double1(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(double1(6))


# 3.封装函数，交换某两个变量的值, 并返回结果
def translate1(a, b):
    a, b = b, a
    return a, b


a = 1
b = 2
print(translate1(a, b))


# 4,封装函数，将某个字符串中的大写字母转换为小写，小写字母转换为大写，将新的字符串返回【参数设置为默认参数】
# swapcase()
def translate2(s):
    return s.swapcase()


s = 'abdadaAAdaDDD'
print(translate2(s))
''' 进阶题 '''


# 1.封装函数，比较某两个数的大小，返回较大的一个
def compare(a, b):
    if a > b:
        return a
    else:
        return b


print(compare(1, 2))


# 2.封装函数，判断某个数是否是素数，返回结果(True或False)
def decide(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


print(decide(9))


# 3.封装函数，计算2-100之间素数的个数，返回结果
# def count2(x, y):
#     count2 = 0
#     for i in range(x, y + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             count2 += 1
#     return count2

def count2(x, y):
    count3 = 0
    for n in range(x, y + 1):
        if decide(n):
            count3 += 1
    return count3




print(count2(2, 100))

''' 进阶题 '''


# 1,封装函数，实现如下要求
# 	例如：输入2，5，则求 2+22+222+2222+22222的和
def fun1(a, n):
    s = 0
    s1 = 0
    for i in range(n):
        s = s * 10 + a
        s1 += s
    return s1


print(fun1(2, 5))


# 2,已知千锋邮箱的用户名只能由数字字母下划线组成，域名为@1000phone.com,
#    封装函数is_legal_email，判断一个字符串是否是千锋邮箱，是返回True，不是返回False。
#      mail@1000phone.com  是
#      $mail@1000phone.com  不是
#      mail@1000phone.comp  不是
#


# 提示：先找出所有False的情况
#      最后剩下的情况就是True

def is_legel_email(s):
    z = []
    z = s.split('@')
    if len(s) != 2:
        return False
    if z[1] == '1000phone.com':
        for n in z[0]:
            if n.isalnum() == False and n != '_':
                return False
        else:
            return True
    else:
        return False


s = '_mail@1000phone.com'
print(is_legel_email(s))
