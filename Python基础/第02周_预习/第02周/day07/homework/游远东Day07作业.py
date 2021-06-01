''''''
''' 基础题 '''
# 1.已知字符串：“this is a test of Python”
# 	a.统计该字符串中字母s出现的次数: count()
c = 'this is a test of Python'
print(c.count('s'))

# 	b.取出子字符串“test”, 用切片,不能数: 使用find(),len()
a = c.find('test')
b = c[a:a+len('test')]
print(b)
# 	c.采用不同的方式将字符串倒序输出: 切片，循环
d = []
print(c[::-1])
for i in range(len(c)-1, -1, -1):
    print(c[i], end='')
print()
# 	d.将其中的"test"替换为"exam" : replace
print(c.replace('test', 'exam'))
# 2.去掉字符串123@zh@qq.com中的@;
# 提示: replace
s = '123@zh@qq.com'
print(s.replace('@', ''))

''' 进阶题 '''
# 1.已知字符串 s = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
# 	a.请将s字符串的大写改为小写，小写改为大写: swapcase()
s = "aAsmr3idd4bgs7Dlsf9eAF"
print(s.swapcase())
# 	b.请将s字符串的数字取出，并输出成一个新的字符串: 循环，isdigit()
z = ''
for n in s:
    if n.isdigit():
        z += n
print(z)

# 	c.请统计s字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
# 	    并输出成一个字典。 例 d = {'a':2,'s':1, 'm':1}
#       提示：循环,判断字符是否在字典中 'a' in d
s = "aAsmr3idd4bgs7Dlsf9eAF"
d = {}
z = s.lower()
for n in z:
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1
print(d)


# 	d.输出s字符串出现频率最高的字母, 如果有多个最高,将每个都输出: max(d.values()),再循环
max1 = max(d.values())
for k in d:
    if d[k] == max1:
        print(k, end=' ')
print(max1)
# 	e.请判断'boy'字符串中的每一个字母，是否都出现在s字符串里。
# 	    如果出现，则输出True，否则，则输出False
s = "aAsmr3idd4bgs7Dlsf9eAF"
for n in 'boy':
    if n not in s:
        print(False)
        break
else:
    print(True)
# 2.将字符串按照单词进行逆序，空格作为划分单词的唯一条件
#      如传入:”Welcome to Beijing”改为 “Beijing to Welcome”
s = 'Welcome to Beijing'
# split, reverse, join
z = s.split()
print(' '.join(z[::-1]))

''' 挑战题 '''
# 1.输入一个字符串，压缩字符串如下aabbbccccbbd变成a2b5c4d1
s = 'aabbbccccbbd'
#  a2b5c4d1
# count()
d = {}
for n in s:
    if n not in d:
        d[n] = 1
    else:
        d[n] += 1
s2 = ''
for k, v in d.items():
    s2 += k + str(v)
    print(f'{k}{v}', end='')
print()
print(s2)



# 2,将字符中单词用空格隔开
#       已知传入的字符串中只有字母,每个单词的首字母大写，
#       请将每个单词用空格隔开，只保留第一个单词的首字母大写
#       传入:”HelloMyWorld”
#       返回:”Hello my world”

s = 'HelloMyWorld'
s2 = ''
for i in range(len(s)):
    if s[i].isupper() and i > 0:
        s2 += ' ' + s[i].lower()
    else:
        s2 += s[i]
print(s2.capitalize())
# s = 'HelloMyWorld'
# a = [0]
# d = ''
# for k, v in enumerate(s):
#     if k > 0:
#         if v.isupper():
#             a.append(k)
# print(a)
# i = 0
# p = []
# z = s.capitalize()
# while i < len(a):
#     p.append(z[a[i]:a[i + 1]])
#     i += 1
#     if (i + 1) >= len(a):
#         p.append(z[a[i]:len(s)])
#         break
# print(p)
# b = ' '.join(p)
# print(b)
