# -*- coding: utf-8 -*-
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com/movies-in-theaters/']
    start_urls = ['http://www.imdb.com/movies-in-theaters/']

    def parse(self, response):
        self.log('I just visited' + response.url)

        for cont in response.css('table > tbody'):
        	item = {
        			'href': cont.css('tr  >td >div.image > a::attr(href)').extract(),
        			'img-src':cont.css('tr  >td >div.image > a > div.zero-z-index > img::attr(src)').extract(),
        			'Title':cont.css('tr  >td.overview-top > h4 > a::text').extract(),
        			'badges':cont.css('tr  >td.overview-top > p >span::text').extract(),
        			'Description' :cont.css('tr  >td.overview-top > div.outline::text').extract(),
        			'Director':cont.css(' tr  >td.overview-top  > :nth-child(5) > span >a::text').extract(),
        			'Stars':cont.css(' tr  >td.overview-top  > :nth-child(6) >a::text').extract(),	
        	} 
        	yield item
