# -*- coding: utf-8 -*-
import scrapy
from first.items import NextPageItem

class ImdbWithLoaderSpider(scrapy.Spider):
	name = 'imdb-with-tabs'
	allowed_domains = ['www.imdb.com']
	start_urls = ['http://www.imdb.com/']

	def parse(self, response):
		self.log('I just visited' + response.url)

		l = response.css('div.subNavListContainer > ul > li > a::attr(href)')[:4].extract()
		urls = [l[3]]
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url = url, callback= self.parse_detail)

	def parse_detail(self, response):
		self.log('I just visited 1' + response.url)
		for cont in response.css('table > tbody'):
			item = NextPageItem()
			item['Img_src']    = cont.css('tr  >td >div.image > a > div.zero-z-index > img::attr(src)').extract(),
			item['Title']        = cont.css('tr  >td.overview-top > h4 > a::text').extract(),
			item['Badges']       = cont.css('tr  >td.overview-top > p >span::text').extract(),
			item['Description']  = cont.css('tr  >td.overview-top > div.outline::text').extract(),
			item['Director']     = cont.css(' tr  >td.overview-top  > :nth-child(5) > span >a::text').extract(),
			item['Stars']        = cont.css(' tr  >td.overview-top  > :nth-child(6) >a::text').extract()    
			yield item
