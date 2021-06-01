# 随机数
import random

# random.choice(): 在指定列表(序列)中随机选择一个
girlfriends = ['', '小花', '刘亦菲', '范冰冰', '高圆圆', '关晓彤', '如花', '乔碧萝']

print(random.choice(girlfriends))
print(random.choice(range(10)))
print(random.choices('abcde'))

# randint(a, b) : [a, b]范围中随机取一个整数
print(random.randint(2, 3))

# randrange(a, b, step = 1) : [a, b)范围中随机取一个整数
print(random.randrange(2, 3))
print(random.randrange(0, 101, 2))  # 0~100之间取随机的偶数

# 随机的小数: 0~1  [0, 1)
print(random.random())
if random.random() > 0.3:
    print('我有70%几率')

# 指定范围的随机小数 [2, 3)
# uniform(a,b): a+(b-a)*random.random()
print(random.uniform(2, 3))  # 2+(3-2)*random.random()

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)  # 随机排列
print(list1)

