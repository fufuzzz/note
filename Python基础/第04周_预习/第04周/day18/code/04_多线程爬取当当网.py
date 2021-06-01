# 难度: *****
# 当当网图书, 使用正则表达式取出书籍标题，价格，图片路径：
#    http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html
import re
import requests
import time
import threading
# 获取第page页数据
def get_dangdang(page):

    url = f'http://category.dangdang.com/pg{page}-cp01.01.02.00.00.00.html'
    res = requests.get(url)

    # 网页源码
    content = res.text
    # print(content)

    # 正则解析
    # 1.先获取ul中的内容(所有li,所有的图书)
    list1 = re.findall('<ul class="bigimg" id="component_59">(.*?)</ul>', content, re.S)
    # print(len(list1))

    # 2.获取每个li中的内容,并遍历
    content2 = list1[0]
    # print(content2)
    list2 = re.findall('<li.*?>(.*?)</li>', content2, re.S)
    # print(len(list2))
    for i, li in enumerate(list2):
        # 图片路径
        if i == 0:
            img = re.findall("<img src='(.*?)'", li, re.S)[0]
        else:
            img = re.findall("<img data-original='(.*?)'", li, re.S)[0]
        # print(img)

        # 标题
        title = re.findall('<p class="name".*?<a title="(.*?)"', li, re.S)[0]
        # title = title.split()[0]  # 书名
        # print(name)

        # 价格
        price = re.findall('<span class="search_now_price">&yen;(.*?)</span>', li, re.S)[0]
        # print(price)

        # 3.存储到文件中
        with open('dangdang.txt', 'a', encoding='utf-8') as fp:
            s = f'第{page}页-标题:{title}, 价格:{price}, 图片:{img}\n'
            fp.write(s)
            fp.flush()

    print(f'第{page}页 爬取完成')

if __name__ == '__main__':

    start = time.time()
    # 创建多线程,爬取当当网数据
    t_list = []
    for i in range(1, 10):
        # 异步: 使用多线程
        # t = threading.Thread(target=get_dangdang, args=(i, ))
        # t.start()
        # t_list.append(t)

        # 同步: 不使用线程
        get_dangdang(i)


    for t in t_list:
        t.join()

    end = time.time()
    print(end - start)
