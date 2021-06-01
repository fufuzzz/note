import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ErshoufangItem


class HouseSpider(CrawlSpider):
    name = 'house'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/pg1/']

    # rules = (
    #     # Rule(LinkExtractor(allow=r'.+ershoufang/pg\d+'), callback='parse_item', follow=True),
    #     Rule(LinkExtractor(allow=r'.+ershoufang/pg\d+'), callback='parse_item', follow=True),
    # )
    rules = (
        Rule(LinkExtractor(allow=r'.+/ershoufang/pg\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+ershoufang/[0-9]{12}\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(response.url)
        title = response.xpath('/html/body/div[3]/div/div/div[1]/h1/text()').get()
        location = response.xpath('/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a/text()').getall()
        location = ','.join(location)
        style = response.xpath('/html/body/div[5]/div[2]/div[4]/div[1]/div[1]/text()').get()
        size = response.xpath('/html/body/div[5]/div[2]/div[4]/div[3]/div[1]/text()').get()
        # print(datas[0])
        # styles = [data.split('|')[0].strip() for data in datas]
        # sizes = [data.split('|')[1].strip() for data in datas]
        # print(titles)
        # print('22222')
        # print(titles)
        # print(styles)
        # print(sizes)
        # print(locations)
        item = ErshoufangItem(
            title=title,
            location=location,
            style=style,
            size=size
        )
        # print(item)
        yield item


        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
