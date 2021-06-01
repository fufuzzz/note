import re

# 匹配单个字符

# .表示匹配除了换行以外的任意单个字符

# . 表示匹配除了换行以外的任意单个字符
# re.S: 让.可以匹配换行
# re.I: 忽略大小写 ignore case
print(re.search('ap.le', 'ap,le'))
print(re.search('ap.le', 'ap\nle'))
print(re.search('ap.le', 'ap\nle', re.S))
print(re.search('apple', 'Apple', re.I))

# []: 匹配单个字符的取值范围
# [xyz]: 匹配x或y或z
# [a-z]: 匹配小写字母
# [A-Z]: 匹配数字
# [0-9]: 匹配数字
# [a-zA-Z0-9]: 数字或字母
# [a-zA-Z0-9_]: 数字或字母或下划线
print(re.search('ap[a-z]le', 'apxle'))
print(re.search('ap[abz]le', 'apxle'))
print(re.search('ap[a-zA-Z0-9_]le', 'ap9le'))

# \d: 表示数字, 等价于:[0-9]
# \D(了解): 表示非数字, 等价于:[^0-9]
# \w: 表示数字字母下划线.等价于:[a-zA-Z0-9_]
# \W(了解): 表示非数字字母下划线.等价于:[^a-zA-Z0-9_]
# \s: 表示空格,换行\n,制表符\t,换页符\f,回车符\r
## \S(了解): 表示非   空格,换行\n,制表符\t,换页符\f,回车符\r

print(re.search('ap\dle', 'ap8le'))
print(re.search('ap\wle', 'ap_le'))
print(re.search('ap\sle', 'ap le'))


