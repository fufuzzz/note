import scrapy


class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/']

    def parse(self, response):
        pass
