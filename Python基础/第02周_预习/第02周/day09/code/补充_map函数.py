
# map()会根据提供的函数对指定序列做映射
# map(function, iterable, ...)
# function -- 函数
# iterable -- 一个或多个序列

res = map(lambda x: x**2, [1, 2, 3, 4])
print(list(res))

