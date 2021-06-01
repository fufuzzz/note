# 装饰器


def sing():
    print('跳舞')
    print('唱歌')


def sing2():
    print('跳舞')
    sing()


#
def eat():
    print('吃饭')


# 装饰器功能:在任何函数之前都可以'跳舞'
def eat2(fn):
    print('跳舞')
    fn()
    print('上个厕所')


eat2(eat)
eat2(sing)
print('*' * 60)


# Python装饰器
def outer(fn):
    def inner():
        print('跳舞')
        fn()
        print('唱歌')

    return inner


#
def sleep():
    print('睡觉')


# 添加装饰器: 装饰器原理
sleep = outer(sleep)
# print(sleep.__name__)  # inner,现在的sleep已经是inner了

# 函数调用
sleep()  # inner()

# 3.写一个装饰器来统计函数运行的时间
import time


# 装饰器: 统计任意函数的执行时间
def outer2(fn):  # fn=run
    def inner():
        s = time.time()
        fn()  # 相当于调用原始的run
        e = time.time()
        print(e - s)

    return inner


# 函数定义
@outer2  # @outer2 => 相当于在run函数后添加了: run = outer2(run)
def run():
    print('跑步...')
    time.sleep(2)


run()
# 添加装饰器
# run = outer2(run)  # 装饰器原理
# run()

# 同一个装饰器给不同的函数装饰
@outer2
def coding():
    print("正在编码...")
    time.sleep(1)

coding()
# 当前时间
print(time.time())
# 1611284107.6178288  时间戳:指定时间1970年1月1日经历过的秒
