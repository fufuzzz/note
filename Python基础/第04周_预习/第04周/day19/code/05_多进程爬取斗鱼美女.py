import multiprocessing
import threading
from urllib import request
import requests
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
count = 0
def get_meizi(page):
    url = f'https://www.douyu.com/gapi/rknc/directory/yzRec/{page}'

    res = requests.get(url, headers=headers)
    content = res.json()
    meizi_list = content['data']['rl']
    for meizi in meizi_list:
        name = meizi['nn']
        img = meizi['rs1']

        # try:
        #     request.urlretrieve(img, f'douyu/{name}.png')
        #     request.urlcleanup()
        #     print(f'{page}-{name}.png 下载完成')
        # except:
        #     print(f'{page}-{name}.png 下载失败')
        # threading.Thread(target=download, args=(page, name, img)).start()
        download(page, name, img)

def download(page, name, img):
        try:
            request.urlretrieve(img, f'douyu/{name}.png')
            request.urlcleanup()
            print(f'{page}-{name}.png 下载完成')
        except:
            print(f'{page}-{name}.png 下载失败')



if __name__ == '__main__':
    s = time.time()
    if not os.path.exists('douyu'):
        os.mkdir('douyu')
    time_list = []
    for i in range(1, 5):
        t = multiprocessing.Process(target=get_meizi, args=(i, ))
        t.start()
        time_list.append(t)
    for t in time_list:
        t.join()

    e = time.time()
    print(e-s)