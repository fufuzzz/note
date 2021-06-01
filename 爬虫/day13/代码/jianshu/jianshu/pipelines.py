# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class JianshuPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(user='root', passwd='201314', database='jianshu', port=3306)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        print(item)
        sql = "insert into jianshu values (%s, %s, %s)"
        values = (None, item['title'], item['writer'])
        self.cur.execute(sql, values)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()