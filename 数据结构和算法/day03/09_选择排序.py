def xuanze(a):
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    return a


a = [1, 3, 6, 2, 7, 4]
print(xuanze(a))