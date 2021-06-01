def fn1(l):
    for i in range(len(l)):
        for j in range(len(l) - 1 - i):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


# l = [1, 2, 5, 7, 2, 1, 3, 4]
# print(fn1(l))


def fn2(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_index]:
                min_index = j

        l[i], l[min_index] = l[min_index], l[i]
    return l


# l = [1, 2, 5, 7, 2, 1, 3, 4]
# print(fn2(l))


def find(l, n):
    for x in l:
        if x == n:
            print(f'元素{n}的下标是{l.index(x)}')
            break
    else:
        print(-1)


l = [1, 2, 2, 9, 9, 9, 9, 9, 9, 9, 5, 2, 52]
n = 9
find(l, n)

def fn4(l, n):
    for i in range(len(l)):
        if l[i] == n:
            print(f'元素{n}的下标有这些{i}')



# l = [1, 2, 2, 9, 9, 9, 9, 9, 9, 9, 5, 2, 52]
# n = 9
# fn4(l, n)

