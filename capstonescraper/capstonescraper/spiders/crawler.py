#scrapy crawl crawler -O crawlerOutput.json


import scrapy
import sys

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']

    def parse(self, response):
        links = []
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
            """
        for urls in response.css('div.SideCategoryListFlyout'):
            for links in urls.css('a'):
                yield { 
                    'nextLink' : links.css('a').attrib['href']    
                        }
            """
        
        for urls in response.css('div.SideCategoryListFlyout'):
            for links in urls.css('a'):
                if 'href' in links.attrib and links.attrib['href'].startswith("http"):
                    yield response.follow(links, callback = self.parse)
        
#products.css('a')[0].attrib['href']

