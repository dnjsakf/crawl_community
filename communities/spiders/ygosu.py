# -*- coding: utf-8 -*-
import scrapy
import os
from urllib.parse  import urlparse

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from datetime import datetime as dt

class YgosuSpider(scrapy.Spider):
    name = 'ygosu'
    allowed_domains = ['www.ygosu.com']
    
    def __init__( self, *args, **kargs ):
        super(YgosuSpider, self).__init__( *args, **kargs )

        self.cate = kargs['cate'] if 'cate' in kargs else 'yeobgi'
        self.page = kargs['page'] if 'page' in kargs else 1

        self.collection = self.cate
        self.loginPath = '/login/common_login.yg'
        self.start_urls = [
            f'https://www.ygosu.com/community/{ self.cate }/?page={ self.page }'
        ]
    
    def start_requests( self ):
        cookies = [
            {
                'name': 'YGSESSID'
                , 'value': 'upe81t6pnm101340dep823r0e7rbcocugn2b08if301qlomkucle8rkjute4vfc8l453ecjt1rjtv5tapokmrfoipktcm785a9o2131'
            },
            {
                'name': '_ga'
                , 'value': 'GA1.2.1065198482.1572761827'
            },
            {
                'name': '_gid'
                , 'value': 'GA1.2.280814446.1572761827'
            },
            {
                'name': 'user_identify'
                , 'value': '88c2041764535be6ecee139efeaba83f'
            },
            {
                'name': 'login_autologin2_v2'
                , 'value': 'b6pKkX%2FKKVJvCKLUSNxS7KxKKL%2Fr1Wbw3zavS%2FcFxtk%3D'
            },
            {
                'name': 'login_autologin_v2'
                , 'value': 'b1092497d36454006771c38986b1c6ca'
            }
        ]

        for url in self.start_urls:
            print( f'request_url => { url }' )
            yield scrapy.Request( url, callback=self.parse_data, cookies=cookies)


    def check_login( self, response ):
        parsed_url = urlparse( response.url )

        if parsed_url.path == self.loginPath:
            yield scrapy.FormRequest.from_response(
                    response
                    , method = 'POST'
                    , formid = 'login_form'
                    , formdata = {
                        'login_id': 'vvve12'
                        , 'login_pwd': 'wjddns1'
                    }
                    , callback = self.after_login
                    , cb_kwargs = { 'after_url': response.request.url }
                )
        else:
            yield self.parse_data( response )

    def after_login( self, response, after_url=None ):
        yield scrapy.Request( f'{ after_url }&logined=true', callback=self.parse_data )

    def parse_data( self, response ):
        print( f'after_response => { response }' )
        contents = response.xpath('//*[@id="contain"]/div[2]/div[1]/div[2]/table/tbody/tr')

        for content in contents:
            elements = {
                'no': content.xpath('td[@class="no"]/text()').extract()
                , 'tit': content.xpath('td[@class="tit"]/a/text()').extract()
                , 'name': content.xpath('td[@class="name"]/a/text()').extract()
                , 'read': content.xpath('td[@class="read"]/text()').extract()
                , 'href': content.xpath('td[@class="tit"]/a/@href').extract()
                , 'load_dttm': dt.now().strftime('%Y%m%d%H%M%S')
            }

            data = dict()
            for key in elements:
                data[key] = elements[key][0].strip() if len(elements[key]) > 0 else None
            
            if not data['no']: continue

            yield data


