# -*- coding: utf-8 -*-
import scrapy
import os
from urllib.parse  import urlparse

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from datetime import datetime as dt
from communities.items import YgosuItem

from pprint import pprint

class YgosuSpider(scrapy.Spider):
    name = 'ygosu'
    allowed_domains = ['www.ygosu.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'communities.pipelines.MongoPipeline': 100,
        }
    }
    
    def __init__( self, *args, **kargs ):
        super(YgosuSpider, self).__init__( *args, **kargs )
        ''' request_data is scrapyrt.Resources.CrawlResource.prepare_crawl에서 받아옴 '''

        request_data = kargs['request_data'] if 'request_data' in kargs else kargs

        self.collection = 'ygosu'
        self.cate = request_data['cate'] if 'cate' in request_data else 'yeobgi'
        self.page = request_data['page'] if 'page' in request_data else 1

        self.homeUrl = 'https://www.ygosu.com'
        self.loginPath = '/login/common_login.yg'

        self.start_urls = [
            f'{ self.homeUrl }/community/{ self.cate }/?page={ self.page }'
        ]

    def start_requests( self ):
        for url in self.start_urls:
            print( f'request_url => { url }' )
            yield scrapy.Request( url, callback=self.parse )

    def parse( self, response ):
        print( f'after_response => { response }' )
        contents = response.xpath('//*[@id="contain"]/div[2]/div[1]/div[2]/table/tbody/tr')

        for content in contents:

            no = content.xpath('td[@class="no"]/text()').extract_first()
            if not no: continue
            
            subject = content.xpath('td[@class="tit"]/a/text()').extract_first()
            author = content.xpath('td[@class="name"]/a/text()').extract_first()
            read = content.xpath('td[@class="read"]/text()').extract_first()
            link = content.xpath('td[@class="tit"]/a/@href').extract_first()
            load_dttm = dt.now().strftime('%Y%m%d%H%M%S')

            item = YgosuItem(
                community = self.name
                , cate = self.cate
                , no = no.strip() if no else no
                , subject = subject.strip() if subject else subject
                , author = author.strip() if author else author
                , read = read.strip() if read else read
                , link = self.homeUrl + ( link.strip() if link else link )
                , load_dttm = load_dttm
            )
            
            yield item


