import re

# 1, 通过 / 的形式分组
# s = 'abcabcabcdef'
#
# res = re.match(r'(abc)\1', s)
# res = re.sub(r'(abc)abc', r'\1', s)
# print(res.group(0))

# 2,通过 (?P<name>) 分组
# s = '8disen8abc'
# res = re.match(r'(?P<num>\d)disen(?P=num)', s)
#
# print(res.group(0))

# 贪婪模式
# print(re.findall(r'<(.*?)>', '<tr>abc<tr>'))
# print(re.findall(r'a(\d{2,4}?)', 'a8675'))

# 单行模式匹配
# s = '''
# <div>
#     <div class="one">
#         <span>abc</span>
#         <ul>
#             <li>111</li>
#             <li>222</li>
#         </ul>
#     </div>
#     <div class="two">
#         <span>def</span>
#     </div>
# </div>
#
# '''
# 用正则获取 class="one" 的div中的内容
# re.S让 . 能够识别到换行
# re.DATALL 和 re.S 作用是一样的
# res = re.findall(r'<div class="one">(.*?)</div>', s, re.S)
# print(res)


# re.M多行模式
# s = '''
# hello world
# hello worlD
# hello worLD
# '''
#
# res = re.search(r'^h.*?D$', s, re.M)
# print(res.group(0))

# re.I 忽略大小写
s = 'HeLlo woRLD'
res = re.findall(r'hello', s, re.I)
print(res)