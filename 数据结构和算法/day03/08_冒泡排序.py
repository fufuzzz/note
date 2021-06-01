def maopao(a):
    for i in range(0, len(a)-1):
        for j in range(0, len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a



a = [1,3,6,2,7,4]
print(maopao(a))