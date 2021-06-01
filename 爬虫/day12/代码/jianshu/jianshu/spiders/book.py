import scrapy
from scrapy.http import HtmlResponse

from 爬虫.day12.代码.jianshu.jianshu.items import JianshuItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    def parse(self, response):
        # print(response.text)
        href = response.xpath('//ul[@class="note-list"]/li[1]/a/@href').get()
        # print(href, type(href))
        href = response.urljoin(href)
        # print(href)
        yield scrapy.Request(url=href, callback=self.parse_detail)

    def parse_detail(self, response):

        title = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/h1/text()').get()
        num = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/div[1]/div/div/div[2]/span[2]/text()').get()
        print(num)
        item = JianshuItem(title=title, num=num)
        yield item

