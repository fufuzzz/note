import os

# 了解
print(os.name)  # nt => windows系统
print(os.environ)  # 环境变量
print(os.environ.get('PATH'))

# 掌握
print(os.curdir)
# curdir: current directory
# . 表示当前目录
# ..表示上一级目录

# 当前路径
print(os.getcwd())
# C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code

# listdir(): 返回指定目录下的所有文件夹和文件名称,返回的是列表
print(os.listdir(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir'))

# mkdir(): make dir 创建目录
# os.mkdir('haha')
# os.makedirs('a/b/c')  # 创建多层文件夹

# rmdir() : remove dir 删除目录
# os.rmdir('haha')
# os.rmdir('a')  # 删除空文件夹 目录不是空的. : 'a'

# 删除文件
# os.remove('hello.txt')

# 重命名
# os.rename('a', 'aaa')

# 文件属性:了解
# print(os.stat('newdir/test1.txt')

# os.path: 掌握
# os.path.join(): 合并路径
print(os.path.join(r'C:\Users\newdir', 'dir11'))
# 'C:\Users\newdir' + '\' +'dir11
# 'C:\Users\newdir\dir11

# os.path.split(): 拆分路径
print(os.path.split(r'C:\Users\newdir\dir11'))
# (r'C:\Users\newdir', 'dir11')

# os.path.splitext(): 拆分扩展名
print(os.path.splitext('aaa.txt'))
# ('aaa', 'txt')

# os.path.getsize(): 获取文件大小
print(os.path.getsize(r'newdir/test1.txt'))

# 路径是否存在
dir_path = r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir'
file_path = r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir\test2.txt'

# 路径是否存在
print(os.path.exists(dir_path))  # True
print(os.path.exists(file_path))  # True
# 是否为目录
print(os.path.isdir(dir_path))  # True
print(os.path.isdir(file_path))  # True
# 是否为文件
print(os.path.isfile(dir_path))  # True
print(os.path.isfile(file_path))  # True

# 路径:
#   绝对路径: absolute,包括盘符的完整路径
#   相对路径: relative,相对于当前文件所在的路径
print(os.path.abspath('newdir/test1.txt'))
# C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir\test1.txt

# dirname():父目录
print(os.path.dirname('newdir/test1.tst'))
# newdir
# basename():文件名
print(os.path.basename('newdir/test1.txt'))
# test1.txt
