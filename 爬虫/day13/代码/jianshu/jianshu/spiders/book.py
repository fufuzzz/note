import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from 爬虫.day13.代码.jianshu.jianshu.items import JianshuItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/\w+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print(response.url)
        writer = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/div/div[1]/span/a/text()').get()
        title = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/h1/text()').get()

        item = JianshuItem(
            writer=writer,
            title=title
        )

        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
