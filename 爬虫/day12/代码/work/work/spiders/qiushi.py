import scrapy
from scrapy.http import HtmlResponse
import re
from 爬虫.day12.代码.work.work.items import WorkItem


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/page/1/']

    def parse(self, response):
        # print(response.text)
        # page = response.meta.get('page', 1)
        page = re.search('page/(\d+)', response.url).group(1)
        if int(page) == 6:
            return
        srcs = response.xpath('//div[@id="content"]/div/div[2]/div/div[2]/a/img/@src').getall()
        srcs = [response.urljoin(src) for src in srcs]
        # src = response.xpath('//div[@id="content"]/div[1]/div[2]/div/div[@class="thumb"]/a/img/@src')
        # print(srcs)
        names = response.xpath('//div[@id="content"]/div/div[2]/div/div[2]/a/img/@alt').getall()

        for src, name in zip(srcs, names):
            item = WorkItem(src=src, name=name, page=page)
            # item['src'] = src
            # item['name'] = name
            yield item

        # while True:
        #     if page == 5:
        #         break
        #     page += 1
        #     url = f'https://www.qiushibaike.com/imgrank/page/{page}/'
        #     yield scrapy.Request(url=url, callback=self.parse, meta={'page': page})

        url = f'https://www.qiushibaike.com/imgrank/page/{int(page)+1}/'
        yield scrapy.Request(url=url, callback=self.parse)