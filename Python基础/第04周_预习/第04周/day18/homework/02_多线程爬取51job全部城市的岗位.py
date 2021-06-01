# 多线程爬取51job全部城市岗位，并分别保存到单独的以城市名为文件名的html中，如: 深圳.html
# url = "https://jobs.51job.com/"


# '<div class="lkst">(.*?)</div>'

import requests
import threading
import re
import os

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
    print(city_list)
    # 遍历每个城市
    for city in city_list:
        city_name = city[1]  # 城市名称
        city_url = city[0]  # 城市链接

        # 使用多线程
        t = threading.Thread(target=get_city, args=(city_name, city_url))
        t.start()


# 获取每个城市的网页源码
sem = threading.Semaphore(6)


def get_city(city_name, city_url):
    with sem:
        # 获取网页源码
        res = requests.get(city_url, headers=headers)
        content = res.content.decode('gbk')

        # 自动创建citys文件夹
        if not os.path.exists('citys'):
            os.mkdir('citys')

        # 保存到文件中
        with open(f'citys/{city_name}.html', 'w', encoding='gbk') as fp:
            fp.write(content)
            fp.flush()

        print(f'{city_name} 下载完成!')


# if '__name__' == '__main__':
#     for i in range(1, 11):
#         t = threading.Thread(target=get_51job, args=(i, ))
#         t.start()


if __name__ == '__main__':
    get_51job()