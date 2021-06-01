# 1、使用函数递归，分别统计文件夹newdir中文件和文件夹的个数
#    提示：统计当前目录下的文件数量和文件夹数量
#         如果碰到文件，则文件数量+1
#         如果碰到文件夹，则文件夹数量+1，递归调用fn()并传入当前子文件夹目录，
import os
# file_count = 0
# dir_count = 0
def fn(dirPath):
    file_count = 0
    dir_count = 0
    for filename in os.listdir(dirPath):
        file_path = os.path.join(dirPath, filename)
        if os.path.isfile(file_path):
            # global file_count
            file_count += 1
        else:
            # global dir_count
            dir_count += 1
            count1, count2 = fn(file_path)
            file_count += count1
            dir_count += count2

    return file_count, dir_count


print(fn(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业2\newdir'))
