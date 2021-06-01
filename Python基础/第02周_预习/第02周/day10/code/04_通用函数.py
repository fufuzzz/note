# 通用装饰器: 用来匹配任意参数

def outer(fn):
    def inner(*args, **kwargs):
        print('before')
        result = fn(*args, **kwargs)
        print('after')

        return result
    return inner


@outer
def eat():
    print('吃饭:')
    return '吃饭'


@outer
def eat2(food):
    print('吃饭:', food)
    return '吃饭2'


print(eat())
print()
print(eat2('面'))
