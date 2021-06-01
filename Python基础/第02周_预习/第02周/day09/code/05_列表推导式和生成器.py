# 列表推导式: 列表生成式
l = [1, 2, 3, 4]
l = list(range(1, 5))
l = []

for i in range(1, 5):
    l.append(i)

# 列表生成式
l = [i for i in range(1, 5)]  # [1, 2, 3, 4]
l = [i * 2 for i in range(1, 5)]  # [2, 4, 6, 8]
l = [i for i in range(1, 8) if i % 2]  # [1, 3, 5, 7]
l = [i for i in range(1, 8) if i % 2 and i > 2]  # [3, 5, 7]
l = [i for i in range(1, 8) if i % 2 if i > 2]  # [ 3, 5, 7]
l = [i + j for i in "abc" for j in 'xyz']
print(l)

# 将已知的列表中的每个元素求平方
l1 = [2, 3, 4, 5]
l2 = [i ** 2 for i in l1]
print(l2)

# 字典推导式,字典生成式: 了解
d = {i: i * i for i in range(4)}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9}

# 集合推导式,集合生成式: 了解
s = {i ** 3 for i in range(4)}
print(s)  # {0, 1, 27, 8}  无序
print()

# 生成器
g = (i for i in range(10, 13))
print(g)  # generator 生成器

# 需要使用next() 或 for-in循环
# next(): 下一个元素
print(next(g))  # 10
print(next(g))  # 11
print(next(g))  # 12
# print(next(g))  # 报错: StopIteration

# for-in循环
for i in g:
    print('i =', i)


# 生成器函数: 有yiled关键字的生成器函数
#   yield:
#       1.存在于函数中,会让函数变成生成器函数
#       2.会让程序暂停,可以使用next()来调用
#       3.有一个类似的return的功能: 可以返回数据,不一样的是不会立刻终止函数
def fn():
    print('AAA')
    yield 100
    print('BBB')
    yield 200
    print('CCC')
    yield 300

g = fn()
# print(g)  # <generator object fn at 0x000002099DF65E58>

print('--- ', next(g))  # --- 100
print('--- ', next(g))  # --- 200
print('--- ', next(g))  # --- 300

ist1 = [1,2,3,4,5,6]
l = [i for i in ist1 if i % 2 == 0]
print(l)