a = [0, 1, 2, 4, 5, 7, 8]

'''
# 递归查找
def dg(a, item):
    if len(a):
        return False

    # 找到中间的下标
    mid = len(a) // 2

    # 判断找的值 和 中间值对比
    # 如果中间值就是要找的值
    if a[mid] == item:
        return True
    elif a[mid] > item:
        return dg(a[:mid], item)
    else:
        return dg(a[mid:], item)

print(dg(a, 32))
'''
def search(a, item):
    start, end = 0, len(a)-1
    while start <= end:
        mid = (start+end) // 2
        if a[mid] == item:
            return True
        if a[mid] > item:
            end = mid - 1
        elif a[mid] < item:
            start = mid + 1

    return False


print(search(a, 1))