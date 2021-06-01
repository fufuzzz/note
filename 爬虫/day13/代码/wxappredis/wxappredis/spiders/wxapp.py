import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

from ..items import WxappredisItem


class WxAppSpider(RedisCrawlSpider):
    name = 'wxapp'
    allowed_domains = ['dreawer.com']
    # start_urls = ['http://wxapp.dreawer.com/portal.php?mod=list&catid=2&page=1']

    # 开启爬虫后, 会往redis到的队列中插入一个网址,
    # 网址的key就是 start:url, 值就是初始爬取的一个网址
    redis_key = 'start:url'

    rules = (
        # LinkExtractor(allow=r'') 在获取的初始页面源代码中去匹配allow参数中链接地址的正则
        # callback 把请求到的页面源码交给callback方法去获取特定数据
        # follow 代表跟随,如果为True, 表示请求其他页面地址的时候,继续去匹配路由正则
        # 如果为False, 当请求其它页面, 不再去匹配路由正则
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-\d+-\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[1]/h1/text()').get()
        desc = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[3]/p/text()').get()
        # writer = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/p/a/text()').get()
        item = WxappredisItem(title=title, desc=desc)

        yield item




        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
