''''''

# 递归删除文件夹(可能包含子文件或子文件夹)
#  【温馨提示: 创建一个文件夹,不要直接操作已有的文件夹】

# 提示: 要现将文件夹中的所有子文件删除再删除本文件夹
# remove(): 删除文件
# rmdir:删除空目录
import os

s = os.listdir(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir')
print(s)


def del_dir(path):
    if not os.path.exists(path):
        return '文件路径不存在'
    file_list = os.listdir(path)
    # print(file_list)
    for filename in file_list:
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):

            os.remove(file_path)

        else:
            del_dir(file_path)

    # for dirname in file_list:
    #     dir_path = os.path.join(path, dirname)
    #     os.rmdir(dir_path)

    os.rmdir(path)
del_dir(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir2')
