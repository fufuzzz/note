# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from urllib import request
import os

class WorkPipeline:
    def open_spider(self, spider):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.base_img_path = os.path.join(base_path, 'images')

    def process_item(self, item, spider):
        page = item['page']
        if not os.path.exists(f'page{page}'):
            os.mkdir(f'page{page}')
        name = item['name']
        request.urlretrieve(url=item['src'], filename=f'./page{page}/{name}.jpg')

        return item
