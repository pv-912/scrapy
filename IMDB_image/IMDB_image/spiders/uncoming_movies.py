import scrapy
from IMDB_image.items import ImageItem
from scrapy.loader import ItemLoader

class productionSpider(scrapy.Spider):
	name = 'imdb-with-tabs'
	allowed_domains = ['www.imdb.com']
	start_urls = ['http://www.imdb.com/']

	def parse(self, response):
		self.log('I just visited' + response.url)
		
		#input from users
		nextPage = 0
		prevPage = 0
		isNext = input("Want to fetch old or upcoming? Enter 0 for old and 1 for upcoming : ")
		if(isNext == 1):
			nextPage = input("Enter the number of months to get upcoming movies. : ")
		else:
			prevPage = input("Enter the number of old movie's month. : ")

		urls = response.css('div.subNavListContainer > ul > :nth-child(4) > a::attr(href) ').extract_first()
		url = response.urljoin(urls)
		yield scrapy.Request(url = url, callback= self.parse_detail,  meta={'countNext':nextPage, 'countPrev':prevPage})


	def parse_detail(self, response):
		self.log('I just visited 2' + response.url)

		# counts value from meta
		countNext = response.meta['countNext']
		countPrev = response.meta['countPrev']

		#crawling of url from response
		for cont in response.css('table > tbody'):
			il = ItemLoader(item = ImageItem(), selector=cont)
			il.add_css('image_urls','tr  >td >div.image > a > div.zero-z-index > img::attr(src)')
			il.add_css('Title','tr  >td.overview-top > h4 > a::text')
			il.add_css('Badges','tr  >td.overview-top > p >span::text')
			il.add_css('Description','tr  >td.overview-top > div.outline::text')
			il.add_css('Director',' tr  >td.overview-top  > :nth-child(5) > span >a::text')
			il.add_css('Stars',' tr  >td.overview-top  > :nth-child(6) >a::text')    
			yield il.load_item()

			#further url fetch for next
			if(countNext>0):

				urls = response.css('div.see-more > a::attr(href)')[1:].extract()

				self.log(urls)
				for url in urls:
					url = response.urljoin(url)
					yield scrapy.Request(url = url, callback= self.parse_detail,  meta={'countNext': countNext-1, 'countPrev': 0})

# 			#further url fetch for prev
			if(countPrev>0):

				urls = response.css('div.see-more > a::attr(href)').extract_first()

				self.log(urls)
				url = response.urljoin(urls)
				yield scrapy.Request(url = url, callback= self.parse_detail,  meta={'countPrev': countPrev-1, 'countNext':0})