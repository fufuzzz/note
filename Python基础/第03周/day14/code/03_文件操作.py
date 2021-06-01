# 文件操作
#   1.打开文件
#   2.操作文件: 读read / 写 write
#   3.关闭文件

# 示例: 读取 02_异常处理.py文件的内容
# 1.打开文件
#   mode: 打开模式
#       r: 只读, 如果文件不存在,则报错
#       rb: 只读二进制, 如果文件不存在,则报错
#
#       w: 清空写, 如果文件不存在,则创建
#       wb: 清空写二进制, 如果文件不存在,则创建
#
#       a: 追加写, 若果文件不存在,则创建
#       ab:追加写二进制, 如果文件不存在,则创建
# r+ / w+: 写和读

# read
# fp: 文件句柄
# fp = open('02_异常处理.py', encoding='utf-8')
# fp = open('02_异常处理.py', mode='r', encoding='utf-8')
fp = open('02_异常处理.py', 'r', encoding='utf-8')
# fp = open('02_异常处理.py', 'rb')  # 读取二进制
# fp = open('a.txt', 'rb')  # 报错,文件不存在则报错


# 2.读
# print(fp.read())  # 读取所有内容

# print(fp.read(10))  # 一次读取(接下来的)10个字符
# print(fp.read(10))  # 一次读取(接下来的)10个字符

# print(fp.readline())  # 读取下一行
# print(fp.readline())  # 读取下一行
# print(fp.readline())  # 读取下一行

# print(fp.readlines())  # 读取所有行, 返回列表

# print(fp.read().decode())  # 解码

# 3.关闭文件
fp.close()


# write: 写
# fp2 = open('a.txt', 'w', encoding='utf-8')
fp2 = open('a.txt', 'wb')  # 二进制

# fp2.write('hello')
fp2.write('hello'.encode())

fp2.close()


# append: 追加写
# fp3 = open('b.txt', 'a', encoding='utf-8')  newline = ''
fp3 = open('b.txt', 'ab')

# fp3.write('你好')
fp3.write('hello'.encode())

fp3.close()