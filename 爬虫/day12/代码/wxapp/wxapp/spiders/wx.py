import scrapy
from scrapy.http import HtmlResponse

from 爬虫.day12.代码.wxapp.wxapp.items import WxappItem


class WxSpider(scrapy.Spider):
    name = 'wx'
    allowed_domains = ['dreawer.com']
    start_urls = ['http://wxapp.dreawer.com/portal.php?mod=list&catid=2']
    num = 1

    def parse(self, response):

        # 获取meta从参数的方法
        page = response.meta.get('page', 1)
        print(page)


        # response.urljoin 在不完整的页面补充
        hrefs = [response.urljoin(href) for href in response.xpath('//*[@id="itemContainer"]/div/div/h3/a/@href').getall()]

        for href in hrefs:
            # 怎么用scrapy去访问每个链接地址
            yield scrapy.Request(url=href, callback=self.parse_detail)

        while True:
            if page == 3:
                break
            page += 1
            url = f''
            yield scrapy.Request(url=url, callback=self.parse)



    def parse_detail(self, response):
            title = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[1]/h1/text()').getall()
            desc = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[3]/p/text()').getall()
            item = WxappItem(title=title, desc=desc)
            yield item


