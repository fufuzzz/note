# https://www.ygdy8.net/html/gndy/china/index.html
#
# 抓取 国内电影 板块， 第一页中所有电影的信息
#
# 包括 电影海报、片名、年代、主演。
#
# 把结果存储为json数据。
#
# 例如：
#
# [
#
#     {
#
#         'img': '',
#
#         'name': '长安道/长安盗',
#
#         'year': '2019',
#
#         'actors': '范伟 Wei Fan, 宋洋 Yang Song'
#
#     },
#
#     {
#
#         'img': '',
#
#         'name': '河妖',
#
#         'year': '2019',
#
#         'actors': '林子聪 Tze Chung Lam, 徐冬冬 Dongdong Xu'
#
#     }
#
# ]
import requests
import os
from lxml import etree
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

con = requests.get(url='https://www.ygdy8.net/html/gndy/china/index.html', headers=headers)

con.encoding = 'GBK'
# con.encoding = 'gb2312'

html = etree.HTML(con.text)

urls = html.xpath('//table[@class="tbspan"]//a[2]/@href')




for url in urls:
    req = requests.get('https://www.ygdy8.net/' + url, headers=headers)
    req.encoding = 'GBK'
    html2 = etree.HTML(req.text)
    img = html2.xpath('//div[@id="Zoom"]//img/@src')
    # desc = html2.xpath('//div[@id="Zoom"]')
    # txt_str = ''.join(desc)

    # res = re.search(r'◎片　　名(.*?)◎年　　代(.*?)◎产.*?◎主　　演(.*?)◎标.*?')

    name = re.findall(r'◎片　　名\s(.*?)<.*?<center></center>', req.text, re.S)
    year = re.findall(r'◎年　　代\s(.*?)<.*?<center></center>', req.text, re.S)
    actor = re.findall(r'◎主　　演(.*?)◎.*?<center></center>', req.text, re.S)
    # print(year)
    ht = etree.HTML(actor[0])
    desc = ht.xpath('//text()')
    str = ''.join(desc)

    actor = re.sub(r'\s{3,}', ',', str)
    # print(actor)
    data_list = []
    data_list.append({
        'img': img[0],
        'name': name[0],
        'year': year[0],
        'actor': actor
    })

    with open('dianying.json', 'a', encoding='utf-8') as fp:
        json.dump(data_list, fp, ensure_ascii=False)

