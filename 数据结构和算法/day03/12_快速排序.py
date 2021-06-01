
def quick_sort(a, start, end):
    while start >= end:
        return
    low = start
    high = end
    mid = a[start]
    while low < high:
        while a[high] >= mid and low < high:
            high -= 1

        a[low] = a[high]

        while a[low] < mid and low < high:
            low += 1

        a[high] = a[low]
    a[low] = mid

    quick_sort(a, low+1, end)
    quick_sort(a, start, high-1)
    return a

def sort(a):
    if len(a) <= 1:
        return a

    mid = a.pop()
    left = []
    right = []
    for n in a:

        if n < mid:
            left.append(n)

        else:
            right.append(n)

    return sort(left) + [mid] + sort(right)


a = [5, 3, 6, 2, 7, 9, 0]
# print(quick_sort(a, 0, len(a)-1))
print(sort(a))



# array = [5, 3, 6, 2, 7, 9, 0]
# quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
#
# print(quick_sort(array))