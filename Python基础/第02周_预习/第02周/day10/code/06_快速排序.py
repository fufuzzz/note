# 冒泡排序
# 选择排序

# 快速排序: 扩展
''''''

'''
        [4, 5, 6, 7, 2, 1, 3, 8, 9]
        
        [4, 2, 1, 3]   [5]   [6, 7, 8, 9]
        [1][2][4, 3]   [5]   [6][7][8,9]
        [1][2][][3][4]  [5]  [6][7] [][8][9]
        
'''


def quick_sort(l):
    # 临界值
    if len(l) < 2:
        return l
    # 1.取一个元素
    middle = l.pop(len(l) // 2)

    # 2.定义2个列表:left,right,分别存放小于n,和大于middle的元素
    left = []
    right = []

    for n in l:
        if n < middle:
            left.append(n)
        else:
            right.append(n)
    print(left, [middle], right)
    # 函数递归
    return quick_sort(left) + [middle] + quick_sort(right)


l = [4, 2, 6, 7, 5, 1, 3, 9]

print(quick_sort(l))
