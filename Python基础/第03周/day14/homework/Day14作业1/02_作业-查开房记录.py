#
# 题目： 开房查询
# 	创建函数，传入一个名字，查找到这哥们所有的开房记录，
#           然后写入到以这哥们名字为名的txt文件中 如：张三.txt
#

def fn(name):
    fp = open(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业1\kaifanglist.txt', 'r',
              encoding='utf-8')
    while True:
        s = fp.readline()
        content = s

        if not s:
            print('没有这个人的数据')
            break

        content = s
        # print(content.split(',')[0])
        if content.split(',')[0] == name:
            fp2 = open(f'{name}.txt', 'a', encoding='utf-8')
            fp2.write(content)
            fp2.close()
            print(f'查询到{name}的开房记录并且已经记录到{name}.txt文件中')

    fp.close()
    fp2.close()

fn('游远东')  # 查不到游远东的记录
fn('孙志涛')
fn('易璐')
