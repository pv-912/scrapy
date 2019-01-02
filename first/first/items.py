# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NextPageItem(scrapy.Item):
    Title = scrapy.Field(serializer=str)
    Director = scrapy.Field()
    Badges = scrapy.Field()
    Stars = scrapy.Field()
    Img_src = scrapy.Field()
    Description = scrapy.Field()

class NextPageItemWithLoader(scrapy.Item):
    Title = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst(),
    )
    Director = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst(),
    )
    Badges = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst(),
    )
    Stars = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst(),
    )
    Img_src = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst(),
    )
    Description = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=TakeFirst(),
    )

class ScrollPageLoader(scrapy.Item):
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
    Img_src = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )
    Description = scrapy.Field(
        input_processor=MapCompose(unicode.strip),
        output_processor=Join(),
    )