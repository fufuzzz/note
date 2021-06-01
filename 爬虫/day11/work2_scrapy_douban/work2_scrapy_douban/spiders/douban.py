import scrapy
import re

from 爬虫.day11.work2_scrapy_douban.work2_scrapy_douban.items import Work2ScrapyDoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        # print(response.text)
        names = response.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/text()').getall()
        names = [re.sub(r'\s+|/', '', obj) for obj in names]
        names = [i for i in names if i]
        urls = response.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href').getall()
        scores = response.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/div/span[2]/text()').getall()
        print(names)
        print(urls)
        print(scores)
        item = Work2ScrapyDoubanItem()
        for name, url, score in zip(names, urls, scores):
            # data = {
            #     'name': name,
            #     'url': url,
            #     'score': score
            # }
            # print(data)
            item['name'] = name
            item['url'] = url
            item['score'] = score

            # item.name = name
            # item.url = url
            # item.score = score



            yield item