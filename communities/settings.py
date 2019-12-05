# -*- coding: utf-8 -*-

# Scrapy settings for communities project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'communities'

SPIDER_MODULES = ['communities.spiders']
NEWSPIDER_MODULE = 'communities.spiders'

FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 5
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = True

FILES_STORE = 'files'
IMAGES_STORE = 'files'
DEFAULT_FILES_URLS_FIELD = 'file_urls'
DEFAULT_FILES_RESULT_FIELD = 'files'

from communities.config import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION

DOWNLOADER_MIDDLEWARES = {
   'communities.middlewares.SeleniumMiddleware': 200,
}
'''
SPIDER_MIDDLEWARES = {
    'communities.middlewares.SpiderMiddleware': 543,
}
'''

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #'Accept-Language': 'en',
}

'''
ITEM_PIPELINES = {
   'communities.pipelines.MongoPipeline': 100,
   'communities.pipelines.TestPipeline': 200,
    'communities.pipelines.MediaFilePipeline': 1
}
'''

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'communities (+http://www.yourdomain.com)'

# Obey robots.txt rules

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'communities.middlewares.CommunitiesDownloaderMiddleware': 543,
#}


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'communities.pipelines.CommunitiesPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
