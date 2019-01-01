# -*- coding: utf-8 -*-
import scrapy


class ImdbWithTabsSpider(scrapy.Spider):
    name = 'imdb-with-tabs'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
       	self.log('I just visited' + response.url)

        # for cont in response.css('ul.list_tabs'):
        # 	item = {
        # 			'href': cont.css('li > a::attr(href)').extract(),
        # 	} 
        # 	yield item
       	l = response.css('div.subNavListContainer > ul > li > a::attr(href)')[:4].extract()
       	urls = [l[0], l[3]]
       	for url in urls:
	   		# self.log('3 '+url)
	   		url = response.urljoin(url)
	   		# self.log(' 2 '+ url)
	   		yield scrapy.Request(url = url, callback= self.parse_detail)

    def parse_detail(self, response):
    	self.log('I just visited 1' + response.url)
    	for cont in response.css('table > tbody'):
    		item = {
        			'Image Link': cont.css('tr  >td >div.image > a::attr(href)').extract(),
        			'Img - src':cont.css('tr  >td >div.image > a > div.zero-z-index > img::attr(src)').extract(),
        			'Title':cont.css('tr  >td.overview-top > h4 > a::text').extract(),
        			'Badges':cont.css('tr  >td.overview-top > p >span::text').extract(),
        			'Description' :cont.css('tr  >td.overview-top > div.outline::text').extract(),
        			'Director':cont.css(' tr  >td.overview-top  > :nth-child(5) > span >a::text').extract(),
        			'Stars':cont.css(' tr  >td.overview-top  > :nth-child(6) >a::text').extract()	
        	} 
        	yield item
