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
# 实例化一个队列
page_url = queue.Queue()
# 2, 把要爬取的页面链接存放到队列中
for i in range(1, 7):
    url = f'http://www.bbsnet.com/doutu/page/{i}'
    page_url.put((url, str(i)))

# 4,创建方法
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
        if not os.path.exists(f'./斗图网{page}'):
            os.mkdir(f'./斗图网{page}')
        try:
            for alt, src in zip(alts, srcs):
                alt = alt + os.path.splitext(src)[1]
                request.urlretrieve(src, filename=f'./斗图网{page}/{alt}')
        except:
            pass

# 3,创建3个线程
for i in range(3):
    t = Thread(target=get_data)
    t.start()
    join_list.append(t)

for j in join_list:
    j.join()