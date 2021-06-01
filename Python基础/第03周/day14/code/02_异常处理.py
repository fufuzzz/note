# 错误: Error
# 异常: Exception
#     代码写的时候不报错, 运行的时候报错

# 目标:
#   1.学习能力
#   2.解决问题的能力

# 解决bug:
#   1. 查看错误, 直接解决
#   2. 使用print()
#   3. 百度/谷歌: 5分钟
#   4. 问:老师, 同桌, 小伙伴
#   5. debug, 断点


# 异常处理
#   作用: 防止运行代码时报错,导致后面的代码无法运行

try:  # 尝试执行某段代码
    a = 1 / 0
    print(a)
except:  # 如果出错,则进入except
    print('报错了')

print('*' * 100)

# 重点掌握
try:
    a = 1 / n
except Exception as e:
    print(e, type(e))
    # division by zero <class 'ZeroDivisionError'>

# try:
#     a = 1/n
# except NameError as e:
#     print("NameError:", e)
# except ZeroDivisionError as e:
#     print(" ZeroDivisionError:", e)

# try-except-else
try:
    a = 1 / 1
except:
    print('报错')
else:
    print('没报错')

# try-except-finally
try:
    a = 1 / 1
except:
    print('报错')
finally:
    print('不管报不报错,我都会执行')

print('end')


# 自定义异常


class MyException(Exception):
    def __init__(self, name):
        self.name = name


# raise: 主动抛出异常(主动报错)
# raise MyException('建国同志卧底失败错误')

# raise NameError('haha,错误')


# 断言 Asseert
def fn(n):
    # 我们断定n!=0, 如果和我断定的不一样则抛出异常
    assert n != 0, "报错,n不能为0"

    print(100 / n)


fn(0)
