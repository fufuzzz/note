
name = '郑爽'

def fn():
    print('-- fn --')


# print(globals())
print('__name__: ', __name__)

# 1.作为代码运行的入口
# 2.作为内部测试代码使用
#   a.如果是直接运行当前文件,则进入if, __name__ == '__main__'
#   b.如果是其他模块导入了当前模块,则不进入if,  __name__ == 'module'(模块名)


if __name__ == '__main__':
    fn()
