# -*- coding: utf-8 -*-
import platform
import os
import time
import pickle
import urllib

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request( self, request, spider ):
        mode = request.meta['mode'] if 'mode' in request.meta else 'html'

        if mode == 'html':
            url, body = next(self.request_html(request, spider))
        elif mode == 'data':
            url, body = next(self.request_data(request, spider))
        else:
            return None
            
        return HtmlResponse(url=url, body=body, encoding='utf-8', request=request)
            
    def request_html(self, request, spider):
        request.meta['driver'] = self.driver

        self.driver.get( request.url )

        parsedUrl = urllib.parse.urlparse( self.driver.current_url )
        if parsedUrl.path == request.meta['login_path']:

            spider.logger.info( '@@@@@@ Need to login => {0}'.format( request.meta["login_path"] ) )

            # 쿠키 가져오기 -> 로그인하기
            with open('./communities/config/cookies.pkl', 'rb') as reader:
                cookies = pickle.load(reader)

            for cookie in cookies:
                self.driver.add_cookie( cookie )

            self.driver.get( request.url )
            request.meta['adult'] = 1

        previousY = -1
        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(window.scrollY, window.scrollY+500);")

            # time.sleep(0.5)

            # Calculate new scroll height and compare with last scroll height
            currentY = self.driver.execute_script("return window.scrollY")
            if previousY == currentY:
                break
            previousY = currentY

        body = to_bytes( text=self.driver.page_source )
        
        yield ( self.driver.current_url, body )
        
    def request_data(self, request, spider):
        req = urllib.request.Request( request.url )
        body = urllib.request.urlopen( req ).read()

        yield ( request.url, body )
 
    def spider_opened(self, spider):
        PLATFORM = platform.system()

        CHROME_PATH = '/usr/bin/google-chrome'
        DIRVER_NAME = 'chromedriver_78' + ( '.exe' if PLATFORM == 'Windows' else '' )
        CHROMEDRIVER_PATH = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'drivers', DIRVER_NAME )
        WINDOW_SIZE = "1920,1080"

        chrome_options = Options()
        chrome_options.add_argument( "--headless" )
        chrome_options.add_argument( "--no-sandbox" )
        chrome_options.add_argument( "--disable-gpu" )
        chrome_options.add_argument( f"--window-size={ WINDOW_SIZE }" )

        driver = webdriver.Chrome( executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options )
        driver.implicitly_wait( 5 )

        self.driver = driver

    def spider_closed(self, spider):
        self.driver.close()


class SpiderMiddleware(object):
    pass
    
    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

