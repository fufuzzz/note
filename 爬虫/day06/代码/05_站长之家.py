import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}
for i in range(1):
    if i>1:
        con = requests.get(url=f'https://www.chinaz.com/news/{i}.shtml', headers=headers)
    else:
        con = requests.get(url=f'https://www.chinaz.com/news/', headers=headers)
    con.encoding = 'utf-8'
    # 缩小范围
    res = re.findall(r'<ul id="waterfall" class="scrollload-content">(.*?)</ul>', con.text, re.S)
    # print(res)
    # news_title = re.findall(f'<div class="info-limit">.*?<h3><a.*?>(.*?)</a></h3>', con.text, re.S)
    news_titles = re.findall(r'<h3>.*?>(.*?)<', res[0], re.S)
    # news_desc = re.findall(f'<div class="info-limit">.*?<p class="desc">(.*?)</p>', con.text, re.S)
    news_descs = re.findall(r'<p class="desc">(.*?)</p>', res[0], re.S)
    # news_tags = re.findall(f'<div class="tags">.*?</i>(.*?)</a>.*?</i>(.*?)</a>.*?</i>(.*?)</a>.*?</div>', con.text, re.S)
    news_tags = re.findall(r'<div class="tags">.*?</i>(.*?)</a>', res[0], re.S)
    # print(len(news_titles))
    # print(len(news_descs))
    # print(news_tags)
    data_list = []
    for title, desc, tag in zip(news_titles, news_descs, news_tags):
        data_list.append({
            'title': title,
            'desc': desc,
            'tag': tag
        })
    print(data_list)