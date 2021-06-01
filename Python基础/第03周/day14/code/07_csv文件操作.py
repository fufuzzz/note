import csv


# csv文件
# 读取
def read_csv(path):
    fp = open(path, 'r', encoding='utf-8')

    reader = csv.reader(fp)
    # print(reader)
    for row in reader:
        print(row)

    fp.close()


# 写入
def write_csv(path):
    fp = open(path, 'a', encoding='utf-8', newline='')

    # csv写入
    writer = csv.writer(fp)
    # 写入一行
    writer.writerow(['ww', '55', 'man'])
    # 同时写入多行
    writer.writerows([['zl', '66', 'man'], ['sq', '77', 'women']])
    fp.close()


if __name__ == '__main__':
    # read_csv(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\code\test.csv')
    write_csv(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\code\test.csv')