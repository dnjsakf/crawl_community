# -*- coding: utf-8 -*-
import scrapy
import os

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class YgosuSpider(scrapy.Spider):
    name = 'ygosu'
    allowed_domains = ['www.ygosu.com']
    start_urls = [
        'https://www.ygosu.com/community/yeobgi/?page=1'
    ]
    
    def start_requests( self ):
        for url in self.start_urls:
            yield scrapy.Request( url, self.parse )

    def parse( self, response ):
        
        contents = response.xpath('//*[@id="contain"]/div[2]/div[1]/div[2]/table/tbody/tr')

        for content in contents:
            # elements = {
            #     'no': content.css('.no::text').extract()
            #     , 'tit': content.css('.tit > a::text').extract()
            #     , 'name': content.css('.name > a::text').extract()
            #     , 'read': content.css('.read::text').extract()
            # }
            elements = {
                'no': content.xpath('td[@class="no"]/text()').extract()
                , 'tit': content.xpath('td[@class="tit"]/a/text()').extract()
                , 'name': content.xpath('td[@class="name"]/a/text()').extract()
                , 'read': content.xpath('td[@class="read"]/text()').extract()
                , 'href': content.xpath('td[@class="tit"]/a/@href').extract()
            }

            data = dict()
            for key in elements:
                data[key] = elements[key][0].strip() if len(elements[key]) > 0 else None
            
            if not data['no']: continue

            yield data


