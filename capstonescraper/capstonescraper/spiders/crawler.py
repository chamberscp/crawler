import scrapy
import sys
import mysql.connector

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']
    
    def parse(self, response):

        # Display all products in li Odd class
        for products in response.css('div.carousel-active'):
            for titles in products.css('h2.card-title'):
                yield{
                    'name': titles.css('a::text').get()
                }   
        for products in response.css('div.carousel-active'):
            yield {
                'price': products.css('span.price.price--withoutTax::text').get(), 
                'link': products.css('a').attrib['href']
            }
"""
        for url in response.css('div.SideCategoryListFlyout'):
            for links in url.css('a'):
                if 'href' in links.attrib and links.attrib['href'].startswith("http"):
                    yield response.follow(links, callback = self.parse)

"""
