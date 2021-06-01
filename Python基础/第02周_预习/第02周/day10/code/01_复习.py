''''''

'''
1.函数作用域
    内建作用域
    全局作用域
    函数作用域
    局部作用域
    
    全局变量
    局部变量
    
    global
    nonlocal
    
    globals()
    locals()  
2.函数的特殊用法
    函数名: 是函数名字,也是指向该函数的变量
    回调函数

3.函数嵌套和闭包
    函数嵌套:
    def outer():
        def inner():
            pass
            
    闭包:
    def outer():
        x = 10
        def inner():
            nonlocal x
            x += 1
            print(x)
        
        return inner
    
    f = outer()
    f()
    f()
    f()

4. 列表生成式
    l= [i for i in range(4)]  # 列表生成式
    d= {i:i for i in range(4)}  # 字典生成式
    s= {i for i in range(4)}  # 集合生成式
    g= (i for i in range(4))  # 生成器
    
5. 生成器和生成函数
    # 生成器
    g= (i for i in range(4))
    
    # 生成器函数
    def fn():
        yield
    
    # 2中调用方式:
    #   1.next()
    #   2.for-in
    
6. 迭代器和可迭代对象
    type()  # <class 'int'>
    isinstance  # True or False
    
    可迭代对象: 能用for-in循环的
        list, str ,tuple, dict,set,generator
    迭代器: 能用for-in循环的,且可以用next调用
        generator
    iter() 转换成迭代器
    
7.偏函数(了解)

8.栈和队列
    栈:先进后出
    队列:先进先出
         
'''


def fn(x):
    print(x)
    yield x + 1


print(fn(100))
print(next(fn(100)))