import scrapy


class WxSpider(scrapy.Spider):
    name = 'wx'
    allowed_domains = ['dreawer.com']
    start_urls = ['http://wxapp.dreawer.com/portal.php?mod=list&catid=2']

    def parse(self, response):
        # print(response.text)
        # print(response.body)
        #
        # with open('wxapp.html', 'w', encoding='utf-8') as fp:
        #     fp.write(response.text)

        # print(type(response))
        # 获取源代码中所有的新闻标题
        titles = response.xpath('//*[@id="itemContainer"]/div/div/h3/a/text()').getall()
        imgs = response.xpath('//*[@id="itemContainer"]/div/a/img/@src').getall()
        # print(titles
        for title, img in zip(titles, imgs):
            data = {
                'title': title,
                'img': img
            }
            yield data