import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    # 项目开始就发送post请求,需要重写父类的数据
    def start_requests(self):
        data = {
            'kw': 'world'
        }
        yield scrapy.FormRequest(url='https://fanyi.baidu.com/sug', formdata=data, callback=self.post_data)



    '''
    def parse(self, response):

        # post请求的方法
        data = {
            'kw': 'world'
        }
        yield scrapy.FormRequest(url='https://fanyi.baidu.com/sug', formdata=data, callback=self.post_data)
    '''

    def post_data(self, response):

        print(response.json())