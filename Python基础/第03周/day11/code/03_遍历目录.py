import os


# 遍历指定目录的第一层
def search_dir(path):
    # 先获取path下的每一个文件和文件夹名称
    filename_list = os.listdir(path)
    # print(filename_list)  # 子文件和子文件价的名称列表
    # ['dir', 'dir2', 'dir3', 'test1.txt', 'test2.txt]]

    # 然后遍历每个子文件夹和子文件filename_list
    for filename in filename_list:

        # 使用绝对路径
        file_path = os.path.join(path, filename)

        # 判断是否为文件
        if os.path.isfile(file_path):
            print('文件:', filename)
        # 判断是否为目录
        else:
            print('目录', filename)


search_dir(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir')


# 深度遍历目录
def search_dir2(path):
    if not os.path.exists(path):
        return '文件路径不存在'

    filename_list = os.listdir(path)

    for filename in filename_list:
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path):
            print('文件:', filename)
        else:
            print('目录:', filename)

            # 递归调用: 继续遍历子目录
            search_dir2(file_path)

search_dir2(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day11\code\newdir')