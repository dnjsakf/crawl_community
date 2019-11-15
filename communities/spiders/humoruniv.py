# -*- coding: utf-8 -*-
import scrapy
import os
from urllib.parse  import urlparse

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from datetime import datetime as dt
from communities.items import HumorunivItem

from pprint import pprint

class HumorunivSpider(scrapy.Spider):
    name = 'humoruniv'
    allowed_domains = ['web.humoruniv.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'communities.pipelines.MongoPipeline': 100,
        }
    }
    
    def __init__( self, *args, **kargs ):
        super(HumorunivSpider, self).__init__( *args, **kargs )

        pprint( '='*50 )
        pprint( kargs['request_data'] if 'request_data' in kargs else [None] )
        pprint( '='*50 )

        request_data = kargs['request_data'] if 'request_data' in kargs else kargs

        self.collection = 'humoruniv'
        self.cate = request_data['cate'] if 'cate' in request_data else 'pds'
        self.page = request_data['page']-1 if 'page' in request_data else 0

        self.homeUrl = 'http://web.humoruniv.com'
        self.loginPath = '/user/login.html'

        self.start_urls = [
            f'{ self.homeUrl }/board/humor/list.html?table={ self.cate }&pg={ self.page }'
        ]

    def start_requests( self ):
        for url in self.start_urls:
            print( f'request_url => { url }' )
            yield scrapy.Request( url, callback=self.parse )

    def parse( self, response ):
        contents = response.xpath('//*[@id="cnts_list_new"]/div[1]/table[2]/tbody/tr')

        print( f'after_response => { len(contents) } / { response } ' )

        for content in contents:

            id = content.xpath('@id').extract_first()

            if not id: continue

            no = id.replace('li_chk_pds-', '')
            subject = content.xpath('td[@class="li_sbj"]/a/text()').extract_first()
            author = content.xpath('td[@class="li_icn"]/table/tbody/tr/td[2]/span/span/text()').extract_first()
            read = content.xpath('td[@class="li_und"]/text()').extract_first()
            link = content.xpath('td[@class="li_sbj"]/a/@href').extract_first()
            load_dttm = dt.now().strftime('%Y%m%d%H%M%S')

            if not author:
                author = content.xpath('td[@class="li_icn"]/table/tbody/tr/td[2]/span/span/span/text()').extract_first()

            item = HumorunivItem(
                community = self.name
                , cate = self.cate
                , no = no.strip() if no else no
                , subject = subject.strip() if subject else subject
                , author = author.strip() if author else author
                , read = ( read.strip() if read else read ).replace(',', '')
                , link = self.homeUrl + '/board/humor/' + ( link.strip() if link else link )
                , load_dttm = load_dttm
            )
            
            yield item


