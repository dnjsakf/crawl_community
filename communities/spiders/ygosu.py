# -*- coding: utf-8 -*-
import scrapy
import os
from urllib.parse  import urlparse

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from datetime import datetime as dt
from communities.items import YgosuItem

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

        self.cate = kargs['cate'] if 'cate' in kargs else 'yeobgi'
        self.page = kargs['page'] if 'page' in kargs else 1

        self.homeUrl = 'https://www.ygosu.com'
        self.loginPath = '/login/common_login.yg'

        self.start_urls = [
            '{0}/community/{1}/?page={2}'.format( self.homeUrl, self.cate, self.page )
        ]

    def start_requests( self ):
        for url in self.start_urls:
            self.logger.info( 'request_url => {0}'.format( url ) )
            meta = {
                "mode": "html"
                , "login_path": self.loginPath
                , "adult": 0
            }
            yield scrapy.Request( url=url, meta=meta, callback=self.parse )

    def parse( self, response ):
        self.logger.info( 'after_response => {0}'.format( response ) )
        contents = response.xpath('//*[@id="contain"]/div[2]/div[1]/div[2]/table/tbody/tr')

        for content in contents:

            no = content.xpath('td[@class="no"]/text()').extract_first()
            if not no: continue
            
            subject = content.xpath('td[@class="tit"]/a/text()').extract_first()
            author = content.xpath('td[@class="name"]/a/text()').extract_first()
            read = content.xpath('td[@class="read"]/text()').extract_first()
            link = content.xpath('td[@class="tit"]/a/@href').extract_first()
            adult = response.request.meta['adult']

            item = YgosuItem(
                community = self.name
                , cate = self.cate
                , no = no.strip() if no else no
                , subject = subject.strip() if subject else subject
                , author = author.strip() if author else author
                , read = read.strip() if read else read
                , link = self.homeUrl + ( link.strip() if link else link )
                , adult = adult if adult else 0
                , login_path = self.loginPath
            )

            yield item


