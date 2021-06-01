# 正则表达式:
#   Regular Expresssion
#   作用: 匹配字符串

import re


# 引入案例: 匹配QQ号码, 要求:1.必须全是数字,2.不能以0开头,3.长度5~11位
def is_qq(qq):
    # if not qq.isdigit():
    #     return False
    # if qq.startswith('0'):
    #     return False
    # if len(qq)<5 or len(qq)>11:
    #     return False
    # return True

    # 使用正则表达式处理
    return re.search('^[1-9]\d{4,10}$', qq)


print(is_qq('123456'))

# 常用的3个方法
# re.match(): 匹配是否以指定正则开头
res = re.match('\d+', '123abc')
print(res)

# re.search(): 字符串中是否存在正则所匹配的内容
res = re.search('\d+', 'abc123')
print(res)

# re.findall(): 获取所有与正则匹配的内容(列表)
# res = re.findall('google', 'google')  # res = re.findall('google', 'google123 google')
res = re.findall('google', 'google123 google')  # res = re.match('\d+', '123abc')
res = re.findall('google', 'abc')  # []

print(res)

