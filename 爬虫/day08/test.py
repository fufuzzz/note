import requests

from bs4 import BeautifulSoup

from pyecharts.charts import Bar

from pyecharts import options as opts

all_data = []

def parse_page(url):

    res = requests.get(url)

    text = res.content.decode()

    soup = BeautifulSoup(text, 'lxml')

    conMidtab = soup.select('div.conMidtab')[0]

    tables = conMidtab.find_all('table')

    for table in tables:

        trs = table.find_all('tr')[2:]

        for index, tr in enumerate(trs):

            if index == 0:

                city = tr.find_all('td')[1].get_text().strip()

            else:

                city = tr.find('td').get_text().strip()

            min_temp = tr.find_all('td')[-2].string

            all_data.append({

                'city': city,

                'min_temp': min_temp

            })

def main():

    urls = {

        'http://www.weather.com.cn/textFC/hb.shtml',

        'http://www.weather.com.cn/textFC/db.shtml',

        'http://www.weather.com.cn/textFC/hd.shtml',

        'http://www.weather.com.cn/textFC/hz.shtml',

        'http://www.weather.com.cn/textFC/hn.shtml',

        'http://www.weather.com.cn/textFC/xb.shtml',

        'http://www.weather.com.cn/textFC/xn.shtml'

    }

    for url in urls:

        parse_page(url)

    all_data.sort(key=lambda x: int(x['min_temp']))

    data = all_data[0:10]

    cities = map(lambda x: x['city'], data)

    temps = map(lambda x: x['min_temp'], data)

    bar = Bar()

    bar.add_xaxis(list(cities))

    bar.add_yaxis("气温", list(temps))

    bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))

    bar.render('weathers.html')

if __name__ == '__main__':

    main()