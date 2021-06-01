import scrapy


class BinSpider(scrapy.Spider):
    name = 'bin'
    allowed_domains = ['httpbin.org']
    # start_urls = ['http://httpbin.org/ip']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        print(response.text)

        yield scrapy.Request(url=self.start_urls[0], callback=self.parse(), dont_filter=True)