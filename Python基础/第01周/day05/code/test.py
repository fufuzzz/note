age_list = [10, 13, 16, 39, 20]
s = sum(age_list)
avg = s / len(age_list)
print(s, avg)

a_list = [1, '游远东', 'man']
print(a_list)

n = int(input('给定一个n位(不超过10)的整数'))
s = 0
while n:
    a = n % 10
    # print('a', a)
    s += a * (10 ** (len(str(n)) - 1))
    # print('长度', len(str(n)))
    # print(s)
    n = n // 10
    # s += a * (10 ** (len(str(n)) ))
    # print('长度2', len(str(n)))
    # print('n', n)
    # print(s)
print(s)


height = 100.0
s = 100.0
n = float(input('输入第n次:'))
while height > (100/2**(n-1)):
    height /= 2  # 50 25 12.5
    s += height*2
print('共经过多少米:', s)

height = 100
s = 100
n = int(input('输入第n次:'))
# if n == 1:
#     print('共经过多少米:', s)
# else:

for i in range(2, n+1):
    height /= 2
    s += height * 2


print('共经过多少米:', s)
