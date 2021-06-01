#
# 题目： 邮编查询
# 	创建函数， 传入一个邮编，得到归属地
#

def serach_postcode(postcode):
    fp = open(r'C:\Users\ause\Desktop\Python2101\Python基础\第03周\day14\homework\Day14作业1\youbian.txt', 'r',
              encoding='utf-8')

    while True:
        s = fp.readline()
        if not s:
            break
        content = s
        # print(content.split(','))
        if content.split(',')[0][1:7] == postcode:
            return content.split(',')[1][0:len(content.split(',')[1])-1]


print(serach_postcode('110100'))