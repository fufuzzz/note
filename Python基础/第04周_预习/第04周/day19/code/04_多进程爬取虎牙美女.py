import multiprocessing
import threading
import requests
import os
from urllib import request  # 图片下载

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}


# 爬取每一页数据
def get_meizi(page):
    url = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2168&tagAll=0&page={page}'

    # 请求虎牙妹子的数据

    res = requests.get(url, headers=headers)
    content = res.json()  # json解析
    # print(content)
    # print(type(content))  # dict

    # 所有颜值主播
    meizi_list = content['data']['datas']
    # 遍历每个妹子的数据
    for meizi in meizi_list:
        nick = meizi['nick']
        img = meizi['screenshot']  # 图片链接

        # 下载图片
        try:
            request.urlretrieve(img, f'huya/{nick}.png')
            request.urlcleanup()
            print(f'{page}-{nick}.png 下载完成!')
        except:
            print(f'{page}-{nick}.png 下载失败!')
        # for i in range(5):
        #     threading.Thread(target=download, args=(page, nick, img)).start()

# def download(page, nick, img):
#     try:
#         request.urlretrieve(img, f'huya/{nick}.png')
#         request.urlcleanup()
#         print(f'{page}-{nick}.png 下载完成!')
#     except:
#         print(f'{page}-{nick}.png 下载失败!')


if __name__ == '__main__':

    # 如果目录不存在,则创建
    if not os.path.exists('huya'):
        os.mkdir('huya')

    # get_meizi()
    # 使用多进程
    for i in range(1, 4):
        multiprocessing.Process(target=get_meizi, args=(i, )).start()

