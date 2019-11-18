# -*- coding: utf-8 -*-
import os
import pymongo
import scrapy

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.http import HtmlResponse
from scrapy.exceptions import DropItem

from urllib.request import Request, urlopen
from urllib.parse  import urlparse

from pprint import pprint

class MediaImagePipeline( ImagesPipeline ):
    
    def file_path(self, request, response=None, info=None):
        return 'images/' + os.path.basename(urlparse(request.url).path) +'.mp4'

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            print( f'image_url => {file_url}' )
            yield scrapy.Request( url=file_url, meta={'mode': 'data'} )

    def item_completed(self, results, item, info):
        pprint( f'image_completed => {results}' )
        
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['files'] = image_paths
        
        return item

class MediaFilePipeline( FilesPipeline ):
    
    def file_path(self, request, response=None, info=None):
        return 'files/' + os.path.basename(urlparse(request.url).path)

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            print( f'file_url => {file_url}' )
            
            yield scrapy.Request( url=file_url )

    def item_completed(self, results, item, info):
        pprint( f'file_item_completed => {results}' )
        
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['files'] = image_paths
        
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
