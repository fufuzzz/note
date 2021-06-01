def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


def test5():
    l = []
    for i in range(1000):
        l.insert(0, i)

def test6():
    l = []
    l.extend(range(1000))

from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("+", t1.timeit(number=1000), "seconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "seconds")

t3 = Timer("test3()", "from __main__ import test3")
print("列表生成式", t3.timeit(number=1000), "seconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list(range)", t4.timeit(number=1000), "seconds")

t5 = Timer("test5()", "from __main__ import test5")
print("insert", t5.timeit(number=1000), "seconds")

t6 = Timer("test6()", "from __main__ import test6")
print("extend", t6.timeit(number=1000), "seconds")