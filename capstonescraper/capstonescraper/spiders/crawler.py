#scrapy crawl crawler -O crawlerOutput.json

import scrapy
import sys
import mysql.connector

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']
    
    def parse(self, response):
    
        # Display all products in li Odd class
        for products in response.css('li.Odd'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
        # Display all products in li Even class
        for products in response.css('li.Even'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
            name = products.css('a.pname::text').get(), 
            price = products.css('em.p-price::text').get(), 
            link = products.css('a').attrib['href']
        
        # Go to next page in this div class
        for url in response.css('div.SideCategoryListFlyout'):
            for links in url.css('a'):
                if 'href' in links.attrib and links.attrib['href'].startswith("http"):
                    yield response.follow(links, callback = self.parse)
        


