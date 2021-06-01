# filter()函数用于过滤序列,过滤掉不符合条件的元素,
# 返回一个迭代器对象,如果转换为列表,可以使用list()来转换.
# 接收两个参数,第一个为函数,第二个为序列,
# 序列的每个元素作为参数传递给函数进行判断,然后返回True和False,
# 最后返回True的元素放到新列表中

# filter(function, iterable)
# function -- 判断函数  iterable--可迭代器对象
print(list(filter(None, range(10))))
a = range(50)
print(a[2:30:5])


def func(a, b, *args):
    print(a, b, args)


func(*[1, 2, 3, 4])
