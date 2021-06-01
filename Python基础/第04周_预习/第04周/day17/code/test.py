# import time
#
#
# def outer(fn):
#     def inner():
#         s = time.time()
#         fn()
#         d = time.time()
#         print(d - s)
#
#     return inner
#
#
# @outer
# def run():
#     print('跑步')
#     time.sleep(1)

#
# run()

# import time
# def outer2(fn):  # fn=run
#     def inner():
#         s = time.time()
#         fn()  # 相当于调用原始的run
#         e = time.time()
#         print(e - s)
#
#     return inner
#
#
# # 函数定义
# @outer2  # @outer2 => 相当于在run函数后添加了: run = outer2(run)
# def run():
#     print('跑步...')
#     time.sleep(2)
#
#
# run()

# def testFun():
#     temp = [lambda x: i * x for i in range(4)]
#     # for n in temp:
#     #     print(n(3))
#     return temp
#
#
# for everyLambda in testFun():
#     print(everyLambda)

# def fn(n):
#     if n <= 2:
#         return 1
#     return fn(n-1)+fn(n-2)
#
#
# print(fn(5))
import datetime


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def add_hour(self, num):
        self.hour += num

    def add_minute(self, num):
        self.minute += num

    def add_second(self, num):
        self.second += num

    # def show(self):
    #     hour = ''
    #     minute = ''
    #     second = ''
    #     if len(self.hour) == 1:
    #         hour = '0' + str(self.hour)

    def show(self):
        hour = ''
        minute = ''
        second = ''
        if len(str(self.hour)) == 1:
            hour = '0' + str(self.hour)
        else:
            hour = str(self.hour)
        if len(str(self.minute)) == 1:
            minute = '0' + str(self.minute)
        else:
            minute = str(self.minute)
        if len(str(self.second)) == 1:
            second = '0' + str(self.second)
        else:
            second = str(self.second)
        print(f'{hour}:{minute}:{second}')


t = Time(12, 56, 8)
t.show()


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


class PlainRect(Rect):
    def __init__(self, start_x, start_y, width, height):
        self.start_x = start_x
        self.start_y = start_y
        super().__init__(width, height)

    def is_inside(self, x, y):
        if (0 <= x - self.start_x <= self.width) and (0 <= self.start_y - y <= self.height):
            return True
        else:
            return False


rect = PlainRect(1, 4, 6, 2)
print(rect.is_inside(1, 3))


def testFun():
    temp = [lambda x: i * x for i in range(4)]
    return temp


for everyLambda in testFun():
    print(everyLambda(2))


def fn1(n):
    if n <= 2:
        return 1
    return fn1(n - 2) + fn1(n - 1)


print(fn1(5))
