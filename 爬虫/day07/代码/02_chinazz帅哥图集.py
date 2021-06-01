import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

con = requests.get(url='https://sc.chinaz.com/tupian/shuaigetupian.html', headers=headers)

con.encoding = 'utf-8'

html = etree.HTML(con.text)

alts = html.xpath('//div[contains(@class, "box")]//img/@alt')
srcs = html.xpath('//div[contains(@class, "box")]//img/@src2')

data_list = []
for alt, src in zip(alts, srcs):
    data_list.append({
        'alts': alts,
        'srcs': srcs

    })