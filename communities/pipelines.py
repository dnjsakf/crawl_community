# -*- coding: utf-8 -*-
import pymongo

from scrapy.exceptions import DropItem

class QueuePipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def open_spider(self, spider, *args, **kwargs):
        print( spider )

    def process_item(self, item, spider):
        raise DropItem('test-pipeline')
        return item

class MongoPipeline(object):

    mongo_uri = None
    mongo_db = None

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider, *args, **kwargs):
        self.client = pymongo.MongoClient( self.mongo_uri )

        self.db = self.client[ self.mongo_db ][ spider.collection ]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.db.update(
                { 
                    'cate': item['cate']
                    , 'no': item['no'] 
                }, 
                { 
                    '$set': dict(item) 
                }, 
                upsert=True 
            )
        except Exception as err:
            print( err )

        return item
