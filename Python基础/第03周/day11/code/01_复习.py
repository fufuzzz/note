''''''


'''
1. 装饰器
    def outer(fn):
        def inner(*args, **kwargs):
            print('before')
            fn()
            print('after')
        return inner
    
    
    @outer
    def sing():
        print(100)
        return 100

2. 函数递归
    1.找公式
    2.找临界值
    3.要相信函数可以实现
    


    
'''