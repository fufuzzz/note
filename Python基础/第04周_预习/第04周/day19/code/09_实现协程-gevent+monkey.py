# 这三行写在最前面
import gevent
from gevent import monkey  # 猴子补丁
monkey.patch_all()  # 自动切换协程

import requests

def fn(url):
    print('协程', url)
    res = requests.get(url)
    print('ok:', url, len(res.text))


if __name__ =='__main__':
    url_list = [
        'http://www.qq.com',
        'http://www.baidu.com',
        'http://www.toutiao.com'

    ]
    g_list = []
    for url in url_list:
        # 创建协程
        g = gevent.spawn(fn, url)
        g_list.append(g)

    # 同时启动所有协程
    gevent.joinall(g_list)
