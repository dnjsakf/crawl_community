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
    load_dttm = scrapy.Field(serializer=str)

class YgosuItem(ContentItem):
    pass

class HumorunivItem(ContentItem):
    pass