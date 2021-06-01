
# 字符串: 用引号包裹的
#       'hello', "hello"
# str : string

# 字符串的基本操作:
# 1.创建字符串
s = '亲, 买房吗'

# 2.索引
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[-1])

# 3.长度
print(len(s))

# 4.遍历
for c in s:
    print(c, end=' ')  # 字符
print()

for i in range(len(s)):  # 下标
    print(i, end=' ')
print()

for i, c in enumerate(s):
    print(i, c)

# 5.切片
s = 'hello'
print(s[2:4])
print(s[::-1])


# 6.重复
print(s * 3)

# 7.合并
print(s + ' world')

# 8.判断成员
print('hel' in 'hello')

# 9.删除
# 字符串不可以改变
s = 'hello'
# del s[0]
# print(s)
