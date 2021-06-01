import requests
import os
import re
from lxml import etree
import json
import multiprocessing

# def get_house(i):

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
data_list = []
for i in range(1, 6):
    con = requests.get(f'https://sz.lianjia.com/ershoufang/pg{i}/', headers=headers)

    html = etree.HTML(con.text)

    titles = html.xpath('//div[@class="info clear"]//div[@class="title"]//a/text()')
    # print(titles, len(titles))
    # locations = html.xpath('//div[@class="positionInfo"]//a//text()')
    # for p in locations:
    #     d = p.xpath('.//text()')
    # styles = html.xpath('//div[@class="houseInfo"]//text()')

    locations = re.findall(r'<div class="positionInfo">.*?<a.*?data-el="region">(.*?)\s</a>.*?target="_blank">(.*?)</a>', con.text, re.S)

    for j, n in enumerate(locations):
        n = list(n)
        n = '-'.join(n)
        locations[j] = n

    styles = re.findall(r'<div class="houseInfo">.*?</span>(.*?)["|"].*?</div>', con.text, re.S)
    sizes = re.findall(r'<div class="houseInfo">.*?</span>.*?["|"](.*?)["|"].*?</div>', con.text, re.S)
    price_alls = html.xpath('//div[contains(@class, "totalPrice")]//span//text()')
    prices = html.xpath('//div[@class="unitPrice" or @class="totalPrice"]//text()')
    for title, location, style, price_all, price in zip(titles, locations, styles, price_alls, prices):
        if price_all != '暂无数据':
            price_all = '参考价:'+price_all+'万元'
        data_list.append({
           'title': title,
           'location': location,
           'style': style,
           'price_all': price_all,
           'price': price

        })

    # print(len(data_list))
    # print(len(data_list))

with open('house.json', 'w', encoding='utf-8') as fp:
    json.dump(data_list, fp, ensure_ascii=False)


# if __name__ == '__mian__':
#     sem = multiprocessing.Semaphore(5)
#     for i in range(1, 6):
#         multiprocessing.Process(target=get_house, args=(i, sem)).start()
#
#     # with open('house.json', 'a', encoding='utf-8') as fp:
#     #     json.dump(data_list, fp, ensure_ascii=False)