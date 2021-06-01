# 一、有一个多层嵌套列表alist, 请写一段代码遍 历alist中的每一个元素并打印出来。
# 思路：写个递归函数，做迭代输出
alist = [1, [2, 3, [4, 5, [6, 7, [8, 9, 10, 11], 12], 13], 14], 15]

def travel(alist):
    for n in alist:
        if type(n) is not list:
        # if not isinstance(n, list):
            print(n, end=' ')
        else:
            travel(n)
    # print()


travel(alist)