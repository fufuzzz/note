# 排序算法
#   冒泡排序
#   选择排序

l = [5, 4, 3, 2, 1, 8, 7, 9, 6]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] < l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)


# 字符串
'''
1. 基本操作:
    1.创建字符串:
        s = "hello"
    2.索引:
        s[0], s[-1]
    3.长度
        len(s)
    4.循环
        for c in s:
        for i in range(len(s))
        for i , c in enumerate(s):
    5.切片:
        s[::-1]  s[2:4]
    6.重复
        s * 3
    7.合并
        "hello" + "world"
    8.判断成员:
        if "hello" in s:
            print('in')
    9.删除
        del s
功能:
    计数:
        count()
    大小写:
        upper()
        lower()
        title()
        capitalize()
        swapcase()
    判断:
        isupper()
        islower()
        istitle()
        isdigit()
        isalpha()
        isalnum()
        isspace()
    查找:
        find()
        rfind()
        # index()
        # rindex()
    拆分合并:
        split()
        splitlines()
        # splitlines(True)
        join()
    替换:
        replace()
    编码解码:
        str.encode() : 字符串 => 二进制
        bytes.decode : 二进制 => 字符串
    ASCII码:
        chr(65): ASCII => 字符
        ord('a'): 字符 => ASCII
    转义:
        \
        r''
    将字符串当成表达式运算:
        eval()
    对齐(了解即可):
        center()
        ljust()
        rjust()
        zfill()
    去掉头尾指定字符(了解即可)
        strip()
        lstrip()
        rstrip()
    简单加密:
        maketrans()
        translate()


'''

# startswith() : 是否以指定字符开头
print('hello'.startswith('hel'))

# endswith()  : 是否以指定字符结尾
print('hello'.endswith('llo'))
