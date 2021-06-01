import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AppSpider(CrawlSpider):
    name = 'app'
    allowed_domains = ['dreawer.com']
    start_urls = ['http://wxapp.dreawer.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        # LinkExtractor(allow=r'') 在获取的初始页面源代码中去匹配allow参数中链接地址的正则
        # callback 把请求到的页面源码交给callback方法去获取特定数据
        # follow 代表跟随,如果为True, 表示请求其他页面地址的时候,继续去匹配路由正则
        # 如果为False, 当请求其它页面, 不再去匹配路由正则
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'),follow=True),
        Rule(LinkExtractor(allow=r'.+article-\d+-\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        writer = response.xpath('//*[@id="ct"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/p/a/text()').get()
        print(writer)
        print(response.url)
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
