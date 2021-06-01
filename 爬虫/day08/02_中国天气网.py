import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
url = 'http://www.weather.com.cn/textFC/hb.shtml'
data = []
req = requests.get(url, headers=headers)
req.encoding = 'uft-8'
# bs4获取数据
soup = BeautifulSoup(req.text, "lxml")
# html = etree.HTML(con.text)

hrefs = ['http://www.weather.com.cn' + obj.get('href') for obj in soup.select('.lq_contentboxTab2 a')][0:5]
print(hrefs)


def get_data(href):
    con = requests.get(href, headers=headers)
    con.encoding = 'uft-8'
    # bs4获取数据
    soup = BeautifulSoup(con.text, "lxml")
    # html = etree.HTML(con.text)

    divs = soup.select('.conMidtab')[0].select('.conMidtab2')


    for div in divs:
        trs = div.select('tr')[2:]
        for i, tr in enumerate(trs):
            city = tr.select('td')[-8].get_text().strip()
            min_hot = tr.select('td')[-2].get_text().strip()
            data.append({
                "city": city,
                "min_hot": min_hot

            })


for href in hrefs:
    get_data(href)

data.sort(key=lambda x: int(x.get('min_hot')))
data = data[:10]
city_list = [obj.get('city') for obj in data]
min_hot_list = [obj.get('min_hot') for obj in data]

bar = Bar()
bar.add_xaxis(city_list)  # 参数是列表, 表示用哪个数据作为横坐标
bar.add_yaxis('最低温度', min_hot_list) # 第一个参数是
bar.set_global_opts(title_opts=opts.TitleOpts(title='温度情况'))
bar.render('weathers.html')
