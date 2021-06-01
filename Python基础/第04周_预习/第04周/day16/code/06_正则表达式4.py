import re

# 边界匹配
# ^: 开头匹配
# $: 结尾匹配
# ^$: 完全匹配
print(re.search('^google', 'google123'))
print(re.search('google$', '123google'))
print(re.search('^google$', 'google google'))  # None
print(re.search('^go+gle$', 'google'))

# \A: 开头匹配
# \Z: 结尾匹配
# \A \Z: 完全匹配
print(re.search('\Agoogle', 'google123'))
print(re.search('google\Z', '123google'))
print(re.search('\Agogle\Z', 'google google'))
print(re.search('\Ago+gle\Z', 'golooooooogle'))

# 区别
# ^在换行模式下,每一行都会重新开头匹配
print(re.findall('^#\w+', '#baidu\n#google\n#bing', re.M))
# ['#baidu', '#google', '#bing']

print(re.findall('\A#\w+', '#baidu\n#google\n#bing', re.M))  # re.M
# ['#baidu']

# \b: 单词边界
# \B: 非单词边界
print(re.search(r'google\b', '123google abcgoogle'))
print(re.search(r'google\B', '123google abcgoogle123'))

# | 或
print(re.search('aa|bb', 'ab123'))

# [^ ]: 范围取反
print(re.search('a[^a-c]c', 'a,c'))
