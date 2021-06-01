#
# 题目：创建函数， 从文件guishudi.txt中获取数据，输入完整手机号11位，匹配前7位，输出对应的地址和卡类型
#
# 60268|1340475|0431|吉林省长春市|吉林移动大众卡
#   手机号前7位 ：1340475
#
def read_phone(path, num):
    fp = open(path, 'r', encoding='utf-8')
    content = []
    # while True:
    #     s = fp.readline().decode()
    #     if s:
    #         content.append(s)
    #     else:
    #         break
    # print(content)
    content = fp.readlines()
    for i in range(len(content)):
        if content[i].split('|')[1] == num[:7]:
            print(content[i].split('|')[-2], content[i].split('|')[-1])
            break
    else:
        print('无')


read_phone(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业1\guishudi.txt', '13404750431')
