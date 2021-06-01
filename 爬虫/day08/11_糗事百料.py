import requests
from bs4 import BeautifulSoup
from urllib import request
import threading
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

def get_img(page):
    con = requests.get(f'https://www.qiushibaike.com/imgrank/page/{page}/', headers=headers)

    soup = BeautifulSoup(con.text, 'lxml')
    contents = soup.select('div.thumb img')
    for content in contents:
        alt = content.get('alt')
        src = 'https:' + content.get('src')
        if not os.path.exists(f'糗事百科page{page}'):
            os.mkdir(f'糗事百科page{page}')
        try:
            request.urlretrieve(src, f'./糗事百科page{page}/{alt}.jpg')
        except:
            pass


if __name__ == '__main__':
    for i in range(1, 7):
        p = threading.Thread(target=get_img, args=(i, ))
        p.start()
