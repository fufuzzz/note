import requests
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

data = {
    'catid': '',
    'nocatid': '',
    'weight': '60,80,90',
    'keyword': '',
    'thumb': '1',
    'page_num': '100',
    'page': '1',
    'm': '0',
    'mid': '0'
}


req = requests.post(url='https://app.chinaz.com/api/GetIndexRandApiHandler.ashx', headers=headers, data=data)
req.encoding = 'utf-8'
s = ''
# print(req.text)
list =req.json()['data']
print(list)
# for n in list:
#     s +='标题:'+n['title']+'\n'+'内容:'+n['desc']+'\n'
# with open('站长之家.txt', 'w', encoding='utf-8') as fp:
#     fp.write(s)


















# print(req.text)

# news_jianjie_list = re.findall('<div class="info-limit">.*?<p class="desc">.*?\t(.*?)\n.*?</p>.*?</div>', req.text, re.S)
#
# news_title_list = re.findall('<div class="info-limit">.*?<a.*?>\n.*?\n(.*?)\n.*?</a>.*?</div>', req.text, re.S)
#
# print(news_title_list)
# print(news_jianjie_list)
