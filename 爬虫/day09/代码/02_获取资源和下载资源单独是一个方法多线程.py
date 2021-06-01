# 1, 导入队列的包
import os
import queue
from threading import Thread
import requests
import re
from bs4 import BeautifulSoup
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

join_list = []
join_list2 = []
# 实例化一个分页队列
page_url = queue.Queue()
# 图片队列

img_url = queue.Queue()

# 2, 把要爬取的页面链接存放到队列中
for i in range(1, 7):
    url = f'http://www.bbsnet.com/doutu/page/{i}'
    page_url.put((url, str(i)))


# 4,创建方法,获取图片资源的方法
def get_data():
    # 不断的去监听队列
    # 如果队列中有page连接,就进行这个页面的爬取
    # 如果队列为空, 表示数据已经处理完成,不再处理数据
    while True:
        # 判断队列为空, 就return
        if page_url.empty():
            return
        url, page = page_url.get()

        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')
        alts = [obj.get('alt') for obj in soup.select('#post_container img')]
        srcs = [obj.get('src') for obj in soup.select('#post_container img')]

        # 通过页码创建目录
        if not os.path.exists(f'./斗图网zz{page}'):
            os.mkdir(f'./斗图网zz{page}')

        # 把图片资源放入图片队列中
        for alt, src in zip(alts, srcs):
            alt_path = f'./斗图网zz{page}/' + alt + os.path.splitext(src)[1]
            img_url.put((src, alt_path))

# 下载图片资源的方法
def dowload_img():
    # 判断图片队列是否为空
    # 如果不为空, 不断监听图片队列, 拿出数据
    # 为空,就不再处理
    while True:

        # 当页面队列和图片队列同时为空,才表示资源下载完成
        if img_url.empty() and page_url.empty():
            return

        src, file_path = img_url.get()
        try:
            request.urlretrieve(src, filename=file_path)

        except:
            pass



# 3,创建3个线程
for i in range(3):
    t = Thread(target=get_data)
    dowload_t = Thread(target=dowload_img)
    t.start()
    dowload_t.start()
    join_list.append(t)
    join_list2.append(dowload_t)

for j, k in zip(join_list, join_list2):
    j.join()
    k.join()