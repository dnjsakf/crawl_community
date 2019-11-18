# -*- coding: utf-8 -*-
import scrapy
import os
from urllib.parse  import urlparse

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from datetime import datetime as dt

from communities.items import FileItem

from pprint import pprint

class MediaSpider(scrapy.Spider):
    name = 'media'
    allowed_domains = ['*']
    
    custom_settings = {
        'ITEM_PIPELINES': {
            'communities.pipelines.MediaFilePipeline': 2
            , 'communities.pipelines.MediaImagePipeline': 1
        },
        'FILES_STORE ': 'files',
        'IMAGES_STORE': 'files',
    }
    
    def __init__(self, *args, **kargs):
        super(MediaSpider, self).__init__(*args, **kargs)
        
        self.loginPath = None
        
        self.start_urls = [
            #'http://web.humoruniv.com/board/humor/read.html?table=pds&pg=1&number=915310' # humoruniv
            'http://www.gezip.net/bbs/board.php?bo_table=best&wr_id=1198627'
        ]
    
    def start_requests(self):
        for url in self.start_urls:
            print( f'@@@@@@ request_url => { url }' )
            yield scrapy.Request( url=url, callback=self.prase_tag, meta={'mode': 'html'} )
            
    def prase_tag(self, response):
        # xpath = '//div[@id="cnts"]' # humoruniv
        xpath = '//div[@class="view-content"]'  # gezip
        
        for tag in response.xpath( xpath + '//*[@src]' ):
            tagName = tag.xpath('name()').extract_first().strip()
            src = tag.xpath('@src').extract_first().strip()
            parsed = urlparse( src )
            
            if tagName == 'embed':
                print( f'@@@@@@ embed => { src }' )
                
                yield scrapy.Request( url=src, callback=self.parse_item, meta={'mode': 'html'} )

    def parse_item(self, response):
        print( f'@@@@@@ parse_item => { response }' )
        
        # xpath = '//div[@id="cnts"]' # humoruniv
        xpath = '//div[@class="view-content"]'  # gezip
        
        file_urls = []
        for tag in response.xpath( xpath + '//*[@src]' ):
            tagName = tag.xpath('name()').extract_first().strip()
            src = tag.xpath('@src').extract_first().strip()
            parsed = urlparse( src )
            
            if tagName == 'embed':
                print( f'@@@@@@ embed => { src }' )
            else:
                print( f'@@@@@@ src => { src }' )
                
                if parsed.query and parsed.query[0:3] == 'url':
                    file_urls.append( parsed.query[4:] )
                elif parsed.netloc:
                    file_urls.append( src )
    
        item = FileItem()
        item['file_urls'] = file_urls
        yield item
    
