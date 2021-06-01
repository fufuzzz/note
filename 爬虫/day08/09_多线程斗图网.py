import re
import requests
from urllib import request
import os
import multiprocessing
import threading

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}


def get_img(a, b):
    for page in range(a, b):
        con = requests.get(url=f'http://www.bbsnet.com/doutu/page/{page}', headers=headers)
        con.encoding = 'utf-8'
        res = re.findall(r'<ul id="post_container" class="masonry clearfix">(.*?)</ul>', con.text, re.S)
        img = re.findall(r'<img.*?src="(.*?)".*?alt="(.*?)"/>', res[0], re.S)
        # print(len(img))
        for i, n in enumerate(img):
            name = n[1] + os.path.splitext(n[0])[1]
            try:
                if not os.path.exists(f'page{page}'):
                    os.mkdir(f'page{page}')
                request.urlretrieve(url=n[0], filename=(f'page{page}/{name}'))
                print(f'page{page}/{name}下载成功')
            except:
                print(f'page{page}/{name}下载失败')


if __name__ == '__main__':
    # 使用多进程
    lis = []
    for page in range(3):
        # if not os.path.exists(f'page{page}'):
        #     os.mkdir(f'page{page}')
        t = threading.Thread(target=get_img, args=(2*page+1, 2*page+3))
        t.start()
        lis.append(t)

    for j in lis:
        j.join()