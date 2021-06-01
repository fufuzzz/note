import requests
from bs4 import BeautifulSoup
import re
import json
from multiprocessing import Process,Manager, Semaphore

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
#
# con = requests.get('https://www.autohome.com.cn/all/#pvareaid=3311230', headers=headers)
#
# con.encoding = 'gb2312'
#
# soup = BeautifulSoup(con.text, 'lxml')
#
# div = soup.select('div#auto-channel-lazyload-article')[0]
# ul = div.select('ul.article')
# hrefs = ['https:' + obj.get('href') for ul in ul for obj in ul.select('a')]
# # print(len(hrefs))
# # hrefs =ul.select('a')

def get_data(href, data, sem):
    with sem:
        req = requests.get(href, headers=headers)
        req.encoding = 'gb2312'
        soup2 = BeautifulSoup(req.text, 'lxml')
        try:
            div2 = soup2.select('div#articlewrap')[0]
            titles = div2.select('h1')[0].get_text().strip()
            writers = div2.select('div.name')[0].get_text().strip()
            times = div2.select('span.time')[0].get_text().strip()
            srcs = div2.select('p a img')
            imgs = []
            for src in srcs:
                imgs.append('https:' + src.get('src'))
            # print(imgs)
            # imgs = '   '.join(imgs)
            data.append({
                'title': titles,
                'writer': writers,
                'time': times,
                'img': imgs
            })
        except:
            req = requests.get(href, headers=headers)
            req.encoding = 'gb2312'
            # soup2 = BeautifulSoup(req.text, 'lxml')
            # print(req.text)
            url = re.findall(r'<script type="text/javascript">.*?"#fanhui1,#fanhui2".*?_articleurl.*?"(.*?)"', req.text, re.S)
            u = href.split('#')
            # print(url)
            url = u[0] + url[0]
            get_data(url, data, sem)

# for href in hrefs:
#     get_data(href)


if __name__  == '__main__':
    con = requests.get('https://www.autohome.com.cn/all/#pvareaid=3311230', headers=headers)
    con.encoding = 'gb2312'
    soup = BeautifulSoup(con.text, 'lxml')
    div = soup.select('div#auto-channel-lazyload-article')[0]
    ul = div.select('ul.article')
    hrefs = ['https:' + obj.get('href') for ul in ul for obj in ul.select('a')]
    # print(len(hrefs))
    # hrefs =ul.select('a')
    with Manager() as manager:
        sem = Semaphore(6)
        data = manager.list()
        p_list = []
        for href in hrefs:
            p = Process(target=get_data, args=(href, data, sem))
            p.start()
            p_list.append(p)
        for j in p_list:
            j.join()
        # print(data[0])
        # print(type([data]))
        data_list = []
        for data in data:
            data_list.append(data)
        # data_list.append(data[0])
    with open('汽车之家.json', 'w', encoding='utf-8') as fp:
        json.dump(data_list, fp, ensure_ascii=False)

# req = requests.get('https://www.autohome.com.cn/news/202103/1127067.html#pvareaid=102624', headers=headers)
#
# req.encoding = 'gb2312'
#
# # soup2 = BeautifulSoup(req.text, 'lxml')
# # print(req.text)
#
# url = re.findall(r'<script type="text/javascript">.*?"#fanhui1,#fanhui2".*?_articleurl.*?"(.*?)"', req.text, re.S)
# u = 'https://www.autohome.com.cn/news/202103/1127067.html#pvareaid=102624'.split('#')
# # print(url)
# print(u)
# url = u[0] + url[0]
# print(url)
