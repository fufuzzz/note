# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），
# 如何求出所有a、b、c可能的组合?

'''
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print(a, b, c)
'''

for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print(a, b, c)