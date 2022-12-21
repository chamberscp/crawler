import scrapy
import sys
import mysql.connector

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']
    
    def parse(self, response):
        item = scrapy.Item()
    
        cnx = mysql.connector.connect(
            user= "admin", 
            password= "team2project", 
            host= "my-database.clh7uaufcnt6.us-east-1.rds.amazonaws.com",
            database= "CrawlerProject"
        )
        cursor = cnx.cursor()

        # Display all products in div card-body
        for products in response.css('div.card-body.purchase-ability.ratings-on.withoutTax '):
            #item['name'] = products.css('a::text').get()
            yield {
                'name': products.css('a::text').get(),
                'price': products.css('span.price.price--withoutTax::text').get(), 
                'link': products.css('a').attrib['href']
            }
            """
            query = "INSERT INTO products (name, price, link) VALUES (%s, %s, %s)"
            values = (products['name'], products['price'], products['link'])
            cursor.execute(query, values)
            """

            cnx.commit()
        cnx.close()
"""
            for links in url.css('a'):
                if 'href' in links.attrib and links.attrib['href'].startswith("http"):
                    yield response.follow(links, callback = self.parse)

"""
