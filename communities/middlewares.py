# -*- coding: utf-8 -*-
import os
import time
import pickle

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from urllib.parse import urlparse

class SeleniumMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request( self, request, spider ):
        # 쿠키 저장
        # with open('./cookies.pkl', 'wb') as writor:
        #     pickle.dump( request.cookies, writor )

        # 쿠키 가져오기
        with open('./communities/config/cookies.pkl', 'rb') as reader:
            cookies = pickle.load(reader)
        print( f'cookies => { cookies }' )

        request.meta['driver'] = self.driver  # to access driver from response

        self.driver.get( request.url )

        parsedUrl = urlparse( self.driver.current_url )
        if parsedUrl.path == spider.loginPath:
            print( f'Need to login => { parsedUrl.path }' )
            for cookie in cookies:
                self.driver.add_cookie( cookie )
            self.driver.get( request.url )

        body = to_bytes( text=self.driver.page_source )

        time.sleep( 1 )
        
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def spider_opened(self, spider):
        CHROME_PATH = '/usr/bin/google-chrome'
        CHROMEDRIVER_PATH = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'drivers/chromedriver_78' )
        WINDOW_SIZE = "1920,1080"

        chrome_options = Options()
        chrome_options.add_argument( "--headless" )
        chrome_options.add_argument( f"--window-size={ WINDOW_SIZE }" )

        driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
        driver.implicitly_wait( 3 )

        self.driver = driver

    def spider_closed(self, spider):
        self.driver.close()