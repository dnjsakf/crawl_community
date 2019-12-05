# -*- coding: utf-8 -*-
import os
import pymongo
import scrapy
import logging

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.media import MediaPipeline
from scrapy.http import HtmlResponse
from scrapy.exceptions import DropItem

from urllib.request import Request, urlopen
from urllib.parse  import urlparse

from bson.objectid import ObjectId
from datetime import datetime as dt

logger = logging.getLogger(__name__)


class MediaFilePipeline( FilesPipeline ):

    mongo_uri = None
    mongo_db = None
    mongo_collection = None

    def open_spider(self, spider, *args, **kwargs):
        self.spiderinfo = self.SpiderInfo(spider)

        self.client = spider.client
        self.database = spider.database

    def close_spider(self, spider):
        self.client.close()
        spider.client.close()

    def file_path(self, request, response=None, info=None):
        return 'files/' + os.path.basename(urlparse(request.url).path)

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            logger.info( 'file_url => {0}'.format( file_url ) )
            yield scrapy.Request( url=file_url, dont_filter=True, meta={ 'mode': 'data' } )

    def item_completed(self, results, item, info):
        failure_path = [ [res, res.args] for success, res in results if success == False]
        success_path = [ res['path'] for success, res in results if success == True]

        logger.info( 'file_item_completed => {0} {1}'.format( len(success_path), len(failure_path) ))
        logger.debug( failure_path )

        #if not success_path:
        #    raise DropItem("Item contains no images")
        item['files'] = success_path
        
        self.database.update(
            {
                '_id': ObjectId(item['_id'])
            },
            {
                '$set': {
                    'completed': {
                        'date': dt.now().strftime('%Y%m%d%H%M%S')
                        , 'success': len( success_path )
                        , 'failure': len( failure_path )
                    },
                }
            }
        )

        return item


class MongoPipeline(object):

    mongo_uri = None
    mongo_db = None
    mongo_collection = None

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE'),
            mongo_collection = crawler.settings.get('MONGO_COLLECTION')
        )

    def open_spider(self, spider, *args, **kwargs):
        self.client = pymongo.MongoClient( self.mongo_uri )
        self.database = self.client[ self.mongo_db ][ self.mongo_collection ]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            item['load_dttm'] = dt.now().strftime('%Y%m%d%H%M%S')

            self.database.update(
                { 
                    'community': item['community']
                    , 'cate': item['cate']
                    , 'no': item['no']
                }, 
                { 
                    '$set': dict(item)
                }, 
                upsert=True 
            )
        except Exception as err:
            logger.error( err )

        return item
