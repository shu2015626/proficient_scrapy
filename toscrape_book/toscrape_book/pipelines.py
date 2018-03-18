# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import Item


class BookPipeline(object):
    rating_dict = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def process_item(self, item, spider):
        rating = item.get('review_rating')
        if rating:
            item['review_rating'] = self.rating_dict[rating.title()]
        else:
            item['review_rating'] = 0
        return item


class MongoDBPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URI = crawler.settings.get("MONGO_DB_URI",
                                          "mongodb://127.0.0.1:27017")
        cls.DB_NAME = crawler.settings.get("MONGO_DB_NAME", "scrapy_data")
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URI)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post_data = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post_data)
        return item