# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ContentItem(scrapy.Item):
    community = scrapy.Field()
    cate = scrapy.Field()
    no = scrapy.Field(serializer=int)
    subject = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()
    read = scrapy.Field()
    adult = scrapy.Field(default=0)
    login_path = scrapy.Field(default='null')
    load_dttm = scrapy.Field(serializer=str)

class YgosuItem(ContentItem):
    pass

class HumorunivItem(ContentItem):
    pass

class ImageItem(scrapy.Item):
    images = scrapy.Field()
    image_urls = scrapy.Field()
    
class FileItem(scrapy.Item):
    _id = scrapy.Field()
    files = scrapy.Field()
    file_urls = scrapy.Field()
