# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os


'''
class Work2ScrapyDoubanPipeline:
    # def __init__(self):
    #     self.fp = open('data.json', 'a', encoding='utf-8')

    def open_spider(self, spider):
        # print(spider.name)
        # print('爬虫开始')
        self.fp = open('douban.json', 'a', encoding='utf-8')
        # self.fp = open('douban,json', 'a')
        # self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encodeing='utf-8')



    def process_item(self, item, spider):
        print(item)
        # if os.path.exists('./douban'):
        #     os.mkdir('./douban/')
        # with open('douban.json', 'a', encoding='utf-8') as fp:
        json.dump(dict(item), self.fp, ensure_ascii=False)
        self.fp.write(',')
        return item

    def close_spider(self, spider):
        # print(spider.name)
        print('爬虫结束')
        self.fp.close()
        
    # def __del__(self):
    #     self.fp.close()
'''

'''
from scrapy.exporters import JsonItemExporter
class Work2ScrapyDoubanPipeline:
    # def __init__(self):
    #     self.fp = open('data.json', 'a', encoding='utf-8')

    def open_spider(self, spider):
        self.fp = open('douban2.json', 'wb')
        self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.fp.close()

    # def __del__(self):
    #     self.fp.close()

'''
'''




'''
from scrapy.exporters import JsonLinesItemExporter
class Work2ScrapyDoubanPipeline:
    # def __init__(self):
    #     self.fp = open('data.json', 'a', encoding='utf-8')

    def open_spider(self, spider):
        self.fp = open('douban3.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        return item

    def close_spider(self, spider):
        self.fp.close()

    # def __del__(self):
    #     self.fp.close()