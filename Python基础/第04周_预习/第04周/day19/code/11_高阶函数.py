
# 高阶函数: 把函数当成参数传入另一个函数中

# sorted()
# max()

# map(): 可以批量处理列表中的每个元素
list1 = [1, 2, 3, 4]
# list2 = [i*i for i in list1]
# list2 = map(lambda x: x * x, list1)
list2 = map(lambda x,y: x+y, list1, [10, 20, 30, 40])

print(list(list2))

# reduce(): 累计运算
from functools import reduce
print(reduce(lambda x, y: x+y, range(1, 4)))
print(reduce(lambda x, y: x*y, range(1, 3)))

# filter(): 过滤
list3 = filter(lambda x: x > 10, range(1, 21))
print(list3, list(list3))
