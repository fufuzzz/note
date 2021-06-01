from timeit import Timer


# def test1(n):
#     length = 1
#     for i in range(n):
#         for j in range(i+1, n):
#             if length < j-i+1:
#                 length = j-i+1
#
#
# def fun(n):
#     i = 1
#     while i<=n:
#         i=i*2
#     return i
#
# def test3(n):
#     x = 2
#     while x < n/2:
#         x = 2*x
#
#
# t1 = Timer("test1(100)", "from __main__ import test1")
# print("test1", t1.timeit(number=1000), "seconds")
#
# t2 = Timer("fun(100)", "from __main__ import fun")
# print("fun", t2.timeit(number=1000), "seconds")
#
# t3 = Timer("test3(100)", "from __main__ import test3")
# print("test3", t2.timeit(number=1000), "seconds")
def test4():
    s = 0
    for i in range(1, 101):
        s += i


def test4(n):
    list = []
    for i in range(n-1):
        if i == 0 or i == 1:
            list.append(1)
        else:
            list.append(list[i-1]+list[i-2])
    return list


print(test4(5))



