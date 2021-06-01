a = [5, 3, 4, 1, 8]

def merge_sort(a):
    if len(a) <= 1:
        return a

    # 获取下表左右的列表
    mid = len(a) // 2
    left_li = merge_sort(a[:mid])
    right_li = merge_sort(a[mid:])

    return merge(left_li, right_li)
'''

left_li = merge_sort(a[:mid]) [5, 3]
    left_li = merge_sort(a[:mid]) [5]
        # left_li = [5]
    right_li = merge_sort(a[mid:]) [3]
        # right_li = [3]        
    merge([5], [3])
        # [3, 5]
        
right_li = merge_sort(a[mid:]) [4, 1, 8] 
    left_li = merge_sort(a[:mid]) [4]
        # left_li = [4]
    right_li = merge_sort(a[mid:]) [1, 8]
        left_li = merge_sort(a[:mid]) [1]
        
        right_li = merge_sort(a[mid:]) [8]
            # right_li = [8]
        merge([1], [8])
    merge([4], [1, 8])
        # [1, 4, 8]



'''

def merge(left_li, right_li):

    # 创建两个指针, 分别指向两个列表的第一个值
    l, r = 0, 0
    lis = []
    # 不断的循环两个列表, 对比两个列表的值, 哪个小, 就现把哪个数据加入到新的列表中
    # 直到其中有一个列表的数据对比完成, 跳出循环, 把另外一个列表剩余的数据加入到新的列表中
    while l < len(left_li) and r < len(right_li):
        if left_li[l] < right_li[r]:
            lis.append(left_li[l])
            l += 1
        else:
            lis.append(right_li[r])
            r += 1

    lis = lis + left_li[l:] + right_li[r:]
    return lis


print(merge_sort(a))