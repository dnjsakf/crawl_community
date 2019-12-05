# -*- coding: utf-8 -*-
import os
import scrapy
import pymongo

from urllib.parse  import urlparse

from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.files import FilesPipeline

from communities.items import FileItem
from communities.pipelines import MediaFilePipeline

from pprint import pprint
from datetime import datetime as dt

from communities.config.mongo_pipelines import getContents

class MediaSpider(scrapy.Spider):
    name = 'media'
    custom_settings = {
        'ITEM_PIPELINES': {
            'communities.pipelines.MediaFilePipeline': 100
        }
    }
    
    def __init__(self, *args, **kargs):
        super(MediaSpider, self).__init__(*args, **kargs)

        settings = get_project_settings()

        mongo_uri = settings.get('MONGO_URI'),
        mongo_db = settings.get('MONGO_DATABASE')
        mongo_collection = settings.get('MONGO_COLLECTION')
        
        pipeline = getContents(community='ygosu', cate='adultpic', limit=10 )

        self.client = pymongo.MongoClient( mongo_uri )
        self.database = self.client[ mongo_db ][ mongo_collection ]
        self.contents = list( self.database.aggregate( pipeline ) )
        self.logger.info( self.contents )

    def start_requests(self):
        for content in self.contents:
            self.logger.info( '@@@@@@ request_url => {0}'.format(content["link"]) )
            meta = {
                '_id': content['_id']
                , 'mode': 'html'
                , 'login_path': content['login_path']
            }
            yield scrapy.Request( url=content['link'], meta=meta, callback=self.parse_item )


    def parse_item(self, response):
        self.logger.info( '@@@@@@ parse_item => {0}'.format( response.request.meta["_id"] ) )
        
        xpath = '//div[@id="contain"]//div[@class="container"]'
        
        file_urls = []
        for tag in response.xpath( xpath + '//*[@src]' ):
            tagName = tag.xpath('name()').extract_first().strip()
            src = tag.xpath('@src').extract_first().strip()
            parsed = urlparse( src )
            
            if tagName == 'embed':
                print( '@@@@@@ embed => {0}'.format( src ) )
            else:
                #print( f'@@@@@@ src => { src }' )
                
                if parsed.query and parsed.query[0:3] == 'url':
                    file_urls.append( parsed.query[4:] )
                elif parsed.netloc:
                    file_urls.append( src )
    
        item = FileItem()
        item['file_urls'] = file_urls
        item['_id'] = response.request.meta["_id"]
        
        yield item
