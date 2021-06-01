''''''
# 函数基础

'''
1.函数定义/函数声明
    def fn(a,b):
         print(a,b)
         return a+b

2.函数调用
    fn(3,4)


3.函数参数:
    形参,实参
    
    形参中:位置参数/必需参数, *args,默认参数,**kwargs
    实参中:位置参数/必需参数
4.返回值
    return

5.回调函数

6.匿名函数
    lambda

'''


def fn(*args, **kwargs):
    print(args)
    print(kwargs)


l = [1, 2, 3]
fn(*l)  # (1, 2, 3)

d = {'name': '特朗普', 'age': 74}

fn(*l, **d)  # fn((1,2,3),{'name': '特朗普', 'age': 74}


# return
def fn():
    def fn2():
        print('fn2')
        return 200

    return fn2

