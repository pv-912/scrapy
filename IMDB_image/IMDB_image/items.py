# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


class ImdbImageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def filter_price(value):
    l =  value.encode('utf-8')
    return l

class ImageItem(scrapy.Item):
    image_urls = scrapy.Field(
        input_processor=MapCompose(remove_tags,filter_price),
    )
    Title = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )
    Director = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )
    Badges = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )
    Stars = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )
    Description = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )
    images = scrapy.Field()