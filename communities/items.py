# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class YgosuItem(scrapy.Item):
    cate = scrapy.Field()
    no = scrapy.Field(serializer=int)
    tit = scrapy.Field()
    name = scrapy.Field()
    read = scrapy.Field()
    href = scrapy.Field()
    load_dttm = scrapy.Field(serializer=str)