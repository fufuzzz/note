# 复制目录（考虑拷贝所有子文件）
import os


def copyPath(sourcePath, targetPath):
    # 判断原目录是否存在
    if not os.path.exists(sourcePath):
        return "目录不存在"

    # 判断目标目录是否存在，如果不存在则创建
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)

    # 提示：
    # 遍历sourcePath下的所有子目录和子文件
    #   1， 如果是子文件，则复制文件
    #   2， 如果是子目录，在目标目录创建相同的目录名称，递归调用
    #  注意：子文件或子目录的绝对路径
    filename_list = os.listdir(sourcePath)
    for filename in filename_list:
        file_path = os.path.join(sourcePath, filename)
        copy_path = os.path.join(targetPath, filename)
        if os.path.isfile(file_path):
            fp1 = open(file_path, 'rb')
            fp2 = open(copy_path, 'ab')

            while True:
                content = fp1.read(1024)
                if not content:
                    break
                fp2.write(content)

            fp1.close()
            fp2.close()

        else:
            copyPath(file_path, copy_path)


if __name__ == "__main__":
    # 将sourcePath目录的所有内容拷贝到targetPath目录下
    sourcePath = r"C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业2\newdir"
    targetPath = r"C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业2\newdir-2"
    copyPath(sourcePath, targetPath)
