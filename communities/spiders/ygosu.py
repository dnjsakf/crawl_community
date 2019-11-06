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
    
    def __init__( self, *args, **kargs ):
        super(YgosuSpider, self).__init__( *args, **kargs )

        self.collection = 'ygosu'
        self.cate = kargs['cate'] if 'cate' in kargs else 'yeobgi'
        self.page = kargs['page'] if 'page' in kargs else 1

        self.homeUrl = 'https://www.ygosu.com'
        self.loginPath = '/login/common_login.yg'

        self.start_urls = [
            f'{ self.homeUrl }/community/{ self.cate }/?page={ self.page }'
        ]
    
    def start_requests( self ):
        for url in self.start_urls:
            print( f'request_url => { url }' )
            yield scrapy.Request( url, callback=self.parse_data)

    def parse_data( self, response ):
        print( f'after_response => { response }' )
        contents = response.xpath('//*[@id="contain"]/div[2]/div[1]/div[2]/table/tbody/tr')

        for content in contents:

            no = content.xpath('td[@class="no"]/text()').extract_first()
            if not no: continue
            
            tit = content.xpath('td[@class="tit"]/a/text()').extract_first()
            name = content.xpath('td[@class="name"]/a/text()').extract_first()
            read = content.xpath('td[@class="read"]/text()').extract_first()
            href = content.xpath('td[@class="tit"]/a/@href').extract_first()
            load_dttm = dt.now().strftime('%Y%m%d%H%M%S')

            item = YgosuItem(
                cate = self.cate
                , no = no.strip() if not no else no
                , tit = tit.strip() if not tit else tit
                , name = name.strip() if not name else name
                , read = read.strip() if not read else read
                , href = self.homeUrl + ( href.strip() if not href else href )
                , load_dttm = load_dttm
            )
            
            yield item


