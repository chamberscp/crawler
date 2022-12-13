import scrapy
import sys

class CrawlerSpider(scrapy.Spider):
    name = 'whiskyspider'
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']

    def parse(self, response):
        for products in response.css('li.Odd'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
        for products in response.css('li.Even'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
        for urls in response.css('div.SideCategoryListFlyout'):
            links = url.css('a').attrib['href']

#products.css('a')[0].attrib['href']

