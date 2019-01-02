# -*- coding: utf-8 -*-
import scrapy
from first.items import NextPageItem, ScrollPageLoader
from scrapy.loader import ItemLoader

class ImdbWithItemLoaderSpider(scrapy.Spider):

		name = 'imdb-with-tabs'
		allowed_domains = ['www.imdb.com']
		start_urls = ['http://www.imdb.com/']


		def parse(self, response):

				self.log('I just visited' + response.url)

				urls = response.css('div.subNavListContainer > ul > :nth-child(4) > a::attr(href) ').extract_first()
				url = response.urljoin(urls)
				yield scrapy.Request(url = url, callback= self.parse_detail_with_item_loader,  meta={'counts':0})



		def parse_detail_with_item_loader(self, response):
				
				self.log('I just visited ' + response.url)


				# counts value from meta
				counts = response.meta['counts']
				self.log(counts)

				#crawling of url from response
				for cont in response.css('table > tbody'):
						il = ItemLoader(item = ScrollPageLoader(), selector=cont)
						il.add_css('Img_src','tr  >td >div.image > a > div.zero-z-index > img::attr(src)')
						il.add_css('Title','tr  >td.overview-top > h4 > a::text')
						il.add_css('Badges','tr  >td.overview-top > p >span::text')
						il.add_css('Description','tr  >td.overview-top > div.outline::text')
						il.add_css('Director',' tr  >td.overview-top  > :nth-child(5) > span >a::text')
						il.add_css('Stars',' tr  >td.overview-top  > :nth-child(6) >a::text')    
						yield il.load_item()

				#further url fetch for next
				if(counts<2):
					urls = response.css('div.see-more > a::attr(href)')[1:].extract();
					for url in urls:
						url = response.urljoin(url)
						yield scrapy.Request(url = url, callback= self.parse_detail_with_item_loader,  meta={'counts': counts+1})


