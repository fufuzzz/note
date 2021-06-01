# 使用with关键字打开文件
#   1. 可以自动关闭文件
#   2. 就算报错也会自动关闭
with open('b.txt', 'r', encoding='utf-8') as fp:
    # a = 1/0
    print(fp.read())

#
# 对象能使用with的条件是有下面的方法
#   __enter__()
#   __exit__()


# 防止打开文件时,出现文件不存在而报错的问题
try:
    fp2 = None
    fp2 = open('c.txt', 'r', encoding='utf-8')
    print(fp2.read())

except:
    print("报错了")

finally:
    if fp2:
        fp2.close()
