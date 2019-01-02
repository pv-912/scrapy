# -*- coding: utf-8 -*-
import scrapy
from main.items import NextPageItem, NextPageItemWithLoader
from scrapy.loader import ItemLoader

class ImdbWithItemLoaderSpider(scrapy.Spider):
    name = 'imdb-with-tabs'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
       	self.log('I just visited' + response.url)

       	l = response.css('div.subNavListContainer > ul > li > a::attr(href)')[:4].extract()
       	urls = [l[3]]
       	for url in urls:
	   		url = response.urljoin(url)
	   		yield scrapy.Request(url = url, callback= self.parse_detail_with_item_loader)

    def parse_detail_with_item_loader(self, response):
        self.log('I just visited 1' + response.url)
        for cont in response.css('table > tbody'):
            il = ItemLoader(item = NextPageItemWithLoader(), selector=cont)
            il.add_css('Img_src','tr  >td >div.image > a > div.zero-z-index > img::attr(src)')
            il.add_css('Title','tr  >td.overview-top > h4 > a::text')
            il.add_css('Badges','tr  >td.overview-top > p >span::text')
            il.add_css('Description','tr  >td.overview-top > div.outline::text')
            il.add_css('Director',' tr  >td.overview-top  > :nth-child(5) > span >a::text')
            il.add_css('Stars',' tr  >td.overview-top  > :nth-child(6) >a::text')    
            yield il.load_item()
