''''''

''' 基础题 '''


# 1.简述必需参数、关键字参数、默认参数、不定长参数的区别
# 必需参数:位置参数,必须以正确的顺序传入参数,调用时的数量和声明时一样
# 关键字参数:写在实参中,参数不需要按照顺序传入参数,调用函数时带上形参的关键字
# 默认参数:写在形参中,直接给形参赋默认值,如果需要修改默认值再改变
# 不定长参数:可以处理比当初声明时候更多的参数
#   *agrs:接收任意多个未知参数,被当做元组tuple处理,变量名相当于元组名
#   **args:接收任意多个关键字参数,被当做字典处理,变量名就相当于字典名字

# 2.封装函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他字符】的个数
def fn(s):
    q = 0
    z = 0
    k = 0
    x = 0
    for n in s:
        if n.isnumeric():
            q += 1
        elif n.isalpha():
            z += 1
        elif n == ' ':
            k += 1
        else:
            x += 1

    return q, z, k, x


print(fn('sdasdsdd  2*'))


# 3.封装函数，判断用户传入的参数（字符串、列表、元组其中之一）长度是否大于5, len()>5
def fn2(s):
    return (len(s) > 5)


print(fn2([1, 2, 3, 5, 6, 7, 8]))


# 4.封装函数，计算1到n的和, 并返回结果打印出来; (n为函数参数)
def fn4(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


print(fn4(5))


# 5.封装函数，计算n的阶乘, 并返回结果打印出来
def fn5(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


print(fn5(3))


# 6.封装函数，传入不定个数的数字，返回所有数字的和, 提示: *args

def fn6(*args):
    s = 0
    for n in args:
        s += n
    return s


print(fn6(7, 8, 9))


# 7.封装函数，判断一个年份是不是闰年
def fn7(n):
    return (n % 4 == 0 and n % 100 != 0 or n % 400 == 0)


print(fn7(1000))

''' 进阶题 '''
# 1.写一个函数，识别字符串是否符合python语法的变量名
#   1.数字字母下划线，且不能以数字开头. 2.不能使用关键字
#
import keyword


# print("name" not in keyword.kwlist)
def fn8(s):
    if s in keyword.kwlist:
        return False
    if s[0].isdigit():
        return False
    for n in s:
        if n.isalnum() == False and n != '_':
            return False

    return True


print(fn8('def'))


# 2.写一个函数计算两个数的最小公倍数; 并返回结果打印出来
def func2(a, b):
    max1 = max(a, b)
    while True:
        if max1 % a == 0 and max1 % b == 0:
            return max1
            break
        else:
            max1 += 1


print(func2(6, 8))


# 3. 年月日分别为自定义函数的参数，判断某一个日期是否为合法的日期;
# 	    如: 2020年12月33日不是合法的日期
# 	        2021年2月29日是不合法的日期

def fun3(year, month, day):
    a = ''
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        a = True
    else:
        a = False
    if month > 12 or month < 1 or day < 1:
        print('不是合法的日期')
        return False

    if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        print('不是合法的日期')
    elif a == True and month == 2 and day > 29:
        print('不是合法的日期')
    elif a == False and month == 2 and day > 28:
        print('不是合法的日期')
    elif day > 31:
        print('不是合法的日期')
    else:
        print('是合法日期')


fun3(-200, 1, 0)
