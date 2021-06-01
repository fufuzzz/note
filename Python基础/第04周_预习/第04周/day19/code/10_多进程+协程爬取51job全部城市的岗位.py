import gevent
from gevent import monkey
monkey.patch_all()
import multiprocessing

import threading
import re
import os
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}


def get_51job():
    url = "https://jobs.51job.com/"

    res = requests.get(url, headers=headers)
    content = res.content.decode('GBK')
    list1 = re.findall('<div class="lkst">(.*?)</div>', content, re.S)
    city_str = list1[0]
    city_list = re.findall('<a class="" href="(.*?)">(.*?)</a>', city_str, re.S)
    # print(city_list)
    # 遍历每个城市
    for city in city_list:
        city_name = city[1]  # 城市名称
        city_url = city[0]  # 城市链接

        # 使用多进程
        sem = multiprocessing.Semaphore(8)
        t = multiprocessing.Process(target=get_city, args=(city_name, city_url, sem))
        t.start()


# 获取每个城市的网页源码
# sem = threading.Semaphore(6)


def get_city(city_name, city_url, sem):
    with sem:
        # 获取网页源码
        # print(city_url)
        # 协程: 同时爬取某城市的前5页数据
        g_list = []
        for i in range(1, 6):
            # 每一页的url
            city_url2 = f'{city_url}p{i}/'

            # 创建协程
            g = gevent.spawn(get_city_page, i, city_url2, city_name)
            g_list.append(g)
        # 启动携程
        gevent.joinall(g_list)


# 获取每个城市的每一页数据
def get_city_page(page, city_url2, city_name):
    res = requests.get(city_url2, headers=headers)
    content = res.content.decode('gbk')

    # 保存到文件中
    with open(f'citys/{city_name}-{page}.html', 'w', encoding='gbk') as fp:
        fp.write(content)
        fp.flush()

    print(f'{city_name}-{page} 下载完成!')


# if '__name__' == '__main__':
#     for i in range(1, 11):
#         t = threading.Thread(target=get_51job, args=(i, ))
#         t.start()


if __name__ == '__main__':
    # 自动创建citys文件夹
    if not os.path.exists('citys'):
        os.mkdir('citys')
    get_51job()