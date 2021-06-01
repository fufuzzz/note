# 字符串功能
s = 'hello python'
print(s.count('ll'))
# 子字符串 在 字符串中出现的次数

# 大小写
print('hello'.upper())  # 变成大写
print('HELLO1334'.lower())  # 变成小写
print('you are a good MAN'.title())  # 每个单词首字母大写
print('you are a good MAN'.capitalize())  # 句子的首字母首字母大写,其他小写
# print('you are a good MAN'.swapcase())  # 切换大小写

# 判断
print('10'.isdigit())
print('10'.isalnum())  # 判断是不是数字
print('abCD'.isalpha())  # 是否为字母
print('abCD123'.isalnum())  # 是否为字母或数字
print('ABC'.isupper())  # 是否为大写
print('abc'.islower())  # 是否为小写
# print('I Am A Good Man'.istitle())  # 是否标题话格式  判断是否每个单词字母大写
print(' '.isspace())  # 是否为空格

# 查找
# find(): 从左往右, 找到指定子字符串第一次出现的下标位置,如果找不到则返回-1
# rfind(): 从右往左, 找到指定子字符串第一次出现的下标位置,如果找不到则返回-1
s = 'today is good day, today is tuesday'
print(s.find('day'))  # 2
print(s.find('one'))  # -1
print(s.rfind('day'))  # 32

# index(), rindex()
print(s.index('day'))  # 2
# print(s.index('one'))  # 报错
print(s.rindex('day'))  # 32
# print(s.rindex('one'))  # 报错

# 拆分,分割
# split(): 返回一个列表
s = 'today is  good day'
print(s.split())  # 默认按空格拆分['today', 'is', 'good', 'day']
print(s.split(' '))  # ['today', 'is', '', 'good', 'day']
print(s.split('o'))  # ['t', 'day is  g', '', 'd day']
print(s.split('day'))  # ['to', ' is  good ', '']
print(s.split('abAB'))  # ['today is  good day']
print(s.split('o', 1))  # 使用前2个'o'进行拆分 ['t', 'day is  good day']

# splitline()
s = '''登鹳雀楼
白日依山尽
黄河入海流
欲穷千里目
更上一层楼'''

print(s.splitlines())  # 得到列表 ['登鹳雀楼', '白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼']
# print(s.splitlines(True))  # ['登鹳雀楼\n', '白日依山尽\n', '黄河入海流\n', '欲穷千里目\n', '更上一层楼']
print(s.split('\n'))

# 合并
# join()
l = ['登鹳雀楼', '白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼']
print(','.join(l))
print('\n'.join(l))

# 列表中要是字符串类型
print('+'.join(['1', '2', '3']))

# 替换
# replace()
s = 'I like study,study make me happy'
# 第一个参数是: 旧的字符串
# 第二个参数是: 新的字符串
print(s.replace('study', 'game'))
# print(s.replace('study', 'game'), 1)


# 编码和解码
# 编码: encode 字符串 => 二进制
# 解码: decode 二进制 => 字符串
s = '你好 hello'
b = s.encode()  # 默认 utf-8
b = s.encode('utf-8')  # b'\xe4\xbd\xa0\xe5\xa5\xbd hello'
# b = s.encode('gbk')  # b'\xc4\xe3\xba\xc3 hello'
print(b)  # b'\xe4\xbd\xa0\xe5\xa5\xbd hello'

s2 = b.decode()
print(s2)

# ASCII
# gb2312
# gbk
# unicode
# unf-8

# 对齐
# print('郑爽代孕'.center(50))
# print('郑爽代孕'.center(50, '-'))
# print('郑爽代孕'.ljuest(50, '-'))
# print('郑爽代孕'.rjuest(50, '-'))
# print('郑爽代孕'.zfill(50))

# strip去掉两边指定的字符
print('---鲁班---墨子---'.strip())
print('---鲁班---墨子---'.strip())
print('---鲁班---墨子---'.lstrip())
print('---鲁班---墨子---'.rstrip())

# eval(): 将字符中的内容当成表达式运算
print(eval('1' + '1'))  # 2
list1 = eval('[1,2,3]')
print(type(list1))

# ASCII码 转换
print(chr(65))  # B
print(ord('b'))  # 98

# 简单加密
# md5,RSA
trans = str.maketrans('abc', '123')
print('I like abc'.translate(trans))
# i like 123

# 转义字符: \
s = '特朗普 \n 你马上要下台了'
s = '特朗普 \\ n你马上要下台了'
s = r'特朗普 \n 你马上要下台了'
print(s)
