import scrapy

#Item, Price, URL

class KeywordSpider(scrapy.Spider):
    name = "keywords"
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']

    def parse(self, response):
        
        # Search for the string "product" on the page
        yield {
            'product': response.body.count(b"product")
        }
        

