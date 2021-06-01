import requests
from lxml import etree
import os
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

con = requests.get(url='http://www.tbqq.net/', headers=headers)

# con.encoding = 'utf-8'

html = etree.HTML(con.text)

alts = html.xpath('//div[@class="deanmadouname"]//text()')
srcs = html.xpath('//div[contains(@class, "deanmadoupic")]//img/@src')

print(alts)
print(srcs)

for alt, src in zip(alts, srcs):
    # 先通过requests.get方法请求图片链接
    req = requests.get('http://www.tbqq.net/' + src, headers=headers)
    print(req.url)
    name = alt + os.path.splitext(req.url)[1]
    if not os.path.exists('./美女'):
        os.mkdir('./美女')
    request.urlretrieve(req.url, filename=f'./美女/{name}')