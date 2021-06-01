''''''
import os


# 1.显示指定路径下所有视频格式文件, 提示: 视频格式mp4，avi，rmvb
#   filename.endswith('mp4')
def search_file(path):
    if not os.path.exists(path):
        print('路径不存在')
    filename_list = os.listdir(path)
    for filename in filename_list:
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            if file_path.endswith('mp4') or file_path.endswith('avi') or file_path.endswith('rmvb'):
                print('文件名:', filename)
        else:
            search_file(file_path)


search_file(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\homework\dir')


# 2.自定义模块:
# 	a.建立一个包
# 	b.在包的下创建一个排序的模块
# 	 	模块下的功能
# 			1. 使用冒泡排序对列表进行降序排序
# 			    def fn1(l):
#
from my_package import module3
l = [1, 2, 5, 7, 2, 1, 3, 4]
print(module3.fn1(l))

# 			2. 使用选择排序对列表进行升序排序
#               def fn2(l):
#

l = [1, 2, 5, 7, 2, 1, 3, 4]
print(module3.fn2(l))

# 			3. 查找列表的元素
# 				找到返回下标, 找不到返回-1
# 				def find(l, n):
#

l = [1, 2, 2, 9, 9, 9, 9, 9, 9, 9, 5, 2, 52]
n = 9
module3.find(l, n)

# 			4.顺序查询，获取列表中所有与指定元素重复的元素下标
#               def fn4(l, n):
#

l = [1, 2, 2, 9, 9, 9, 9, 9, 9, 9, 5, 2, 52]
n = 9
module3.fn4(l, n)

# 	在另外一个文件中导入上述包中的模块，完成模块中功能的调用


# 3. 统计文件夹大小 (os.path.getsize()：获取文件大小)
# 提示: 遍历目录
# size = 0
def search_size(path):
    if not os.path.exists(path):
        return '路径不存在'
    filename_list = os.listdir(path)
    size = 0
    for filename in filename_list:
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            # global size
            size += os.path.getsize(file_path)

        else:
            size +=search_size(file_path)
    return size


print(search_size(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\homework\dir'))


# print(size)
size_list = []
def search_size2(path):
    if not os.path.exists(path):
        return '路径不存在'
    filename_list = os.listdir(path)
    size = 0
    print(filename_list)
    for filename in filename_list:
        size = 0
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            # global size
            print('1')
            size += os.path.getsize(file_path)
            if os.path.getsize(file_path) > 52428800:
            # if os.path.isfile(file_path)‬:
                os.rmdir(file_path)
        else:
            size += search_size(file_path)
        size_list.append(size)
    print(size_list)
    return size

search_size2(r'C:\Users\ause\Desktop\note\note\Python_sklearn')
# print(search_size(r'C:\Users\ause\Desktop\note\note\Python_sklearn'))
# if os.path.getsize(r'C:\Users\ause\Desktop\note\note\Python_sklearn\day02\code\2-pandas_missing_values.ipynb') == 10‬:
#     print('1')

def rmdir(path):
    if not os.path.exists(path):
        return '路径不存在'
    filename_list = os.listdir(path)
    size = 0
    print(filename_list)
    for filename in filename_list:
        size = 0
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            # global size
            print('1')
            size += os.path.getsize(file_path)
            if os.path.getsize(file_path) > 52428800:
            # if os.path.isfile(file_path)‬:
                os.rmdir(file_path)
        else:
            size += search_size(file_path)
        size_list.append(size)
    print(size_list)
    return size