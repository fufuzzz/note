# {}: 表示前面字符出现的次数
# []: 表示单个字符出现的取值范围
# (): 表示整体, 分组

import re

s = '0755-88889999'
pattern = '(\d+)-(\d+)'
# (?: ) 非捕获性分组
# pattern = '(?:\d+)-(\d+)'

res = re.search(pattern, s)
# print(res)
# print(res.group())  # 0755-88889999
# print(res.group(0))  # 0755-88889999
# print(res.group(1))  # 0755 第一个分组的内容
# print(res.group(2))  # 88889999  第二个分组的内容
#
# # groups() : 所有分组的内容
# print(res.groups())  # ('0755', '88889999')
print(re.findall(pattern, s))  # [('0755', '88889999')]

# 正则编译
res = re.compile('(\d+)-(\d+)')
print(res.findall(s))

# 其他方法: 了解
# finditer
res = re.finditer('\d+', 'abc123def456')
for i in res:
    print(i.span(), i.group())

# split: 拆分
print(re.split('\d', '1a2b3c4d'))
# ['', 'a', 'b', 'c', 'd']


# sub : 替换
print(re.sub('\s', '-', '赖小平 被判 死刑')) #赖小平-被判-死刑
print(re.subn('\s', '-', '赖小平 被判 死刑')) # ('赖小平-被判-死刑', 2)
