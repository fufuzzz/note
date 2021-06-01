
def inserts(a):
    for i in range(0, len(a)-1):
        for j in range(i+1, 0, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a


a = [5, 3, 6, 2, 7, 9, 0]
print(inserts(a))


'''
n = len(alist)
    for i in range(1,n):
        while i > 0 and alist[i] < alist[i-1]:
            alist[i],alist[i-1] = alist[i-1],alist[i]
            i -= 1


'''