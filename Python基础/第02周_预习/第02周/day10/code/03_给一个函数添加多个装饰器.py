def outer1(fn):
    def inner():
        print('before1')
        fn()
        print('after1')

    return inner()


def outer2(fn):
    def inner(song):
        print('before2')
        if song == '青藏高原':
            song = '死了都要爱'
        fn(song)
        print('after2')

    return inner


# 函数定义
# @outer1
@outer2
def sing(song):
    print('唱歌:', song)


# 函数调用
sing('青藏高原')


# 使用装饰器,给函数set_age控制:传入的n范围是1-100之间,如果超出范围则传入-1

def outer3(fn):
    def inner(n):
        if n > 100 or n < 1:
            n = -1
        fn(n)

    return inner


@outer3
def set_age(n):
    print("age", n)


set_age(101)
