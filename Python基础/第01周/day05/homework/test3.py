

num1 = int(input('输入一个数'))
num2 = int(input('输入另一个数'))

m = 0
if num1 > num2:
    m = num1
else:
    m = num2
while True:
    m += 1
    if m % num1 == 0 and m % num2 == 0:
        print(f'{m}是最小倍数')
        break
for i in range(1000000):
    pass

# num1 = int(input('输入一个数'))
# num2 = int(input('输入另一个数'))
# s = time.time()
# m = 0
# n = 1
# if num1 > num2:
#     m = num1
# else:
#     m = num2
# while True:
#     m *= n
#     n += 1
#     if m % num1 == 0 and m % num2 ==0:
#         print(f'{m}是最小共倍数')
#         break
# for i in range(1000000):
#     pass

list2 = ["One", "Two", "Three"]
list3 = list2 + list(reversed(list2))
print(list3)
