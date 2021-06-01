''''''
import os
# 递归删除文件夹(可能包含子文件或子文件夹)
# 【温馨提示：创建一个文件夹，不要直接操作已有的文件夹】

# 提示：要先将文件夹中的所有子文件删除再删除本文件夹
# remove(): 删除文件
# rmdir()： 删除空目录

def del_dir_file(path):
    if not os.path.exists(path):
        return '该文件夹目录不存在'

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            del_dir_file(file_path)

    os.rmdir(path)


del_dir_file(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业2\newdir-2')