# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class ErshoufangPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(user='root', password='201314', database='ershoufang', port=3306)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
        query = "insert into ershoufang values (%s, %s, %s, %s, %s)"
        values = (None, item['title'], item['location'], item['style'], item['size'])
        self.cur.execute(query, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
