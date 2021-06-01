
''''''

'''
1. json
    json是一种数据格式
    json解析/json反序列化:
        json字符串 => json对象
        json.loads()
    json序列化:
        json对象 => json字符串
        json.dumps()

2. 正则表达式
    re.match()
    re.search()
    re.findall()
    re.compile() 编译正则
    # re.finditer()
    # re.split()
    # re.sub()
    # re,subn()
    
    符号
    匹配单个字符:
        .
        []
        \d \D
        \w \W
        \s \S
    匹配数量:
        ?
        +
        *
        {}
    边界匹配:
        ^
        $
        ^$
        # \A
        # \Z
        # \A \Z
        # \b \B
        
        | 或者
    分组和捕获
        () 分组,整体
        group() 获取每个分组的内容
        groups()
        (?:) 非捕获性分组
        
        分组取别名:
        (?P<name>正则)
'''
# 分组取别名:
#    (?P<name>正则)

import re

s = '0755-66668888'
pattern = '((?P<aaa>\d+)-(?P<bbb>\d+))'

res = re.search(pattern, s)
print(res.group('aaa'))
