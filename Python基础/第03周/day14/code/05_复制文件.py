

# 1、拷贝文件【考虑大文件拷贝，每次读取1024字节拷贝】

#   'C:\Users\ause\Desktop\2017101883游远东\学生（实训）总结.doc'

def copy_file(src_path, target_path):
    fp1 = open(src_path, 'rb')  # 读取 源文件
    fp2 = open(target_path, 'ab')  # 写入 目标文件

    while True:
        content = fp1.read(1024)
        # 如果content为空: 则表示读完了
        if not content:
            print("复制完成!")
            break

        fp2.write(content)

    fp1.close()
    fp2.close()


if __name__ == '__main__':
    src = r'C:\Users\ause\Desktop\2017101883游远东\学生（实训）总结.doc'
    target = r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\code\学生（实训）总结-2.doc'
    copy_file(src, target)