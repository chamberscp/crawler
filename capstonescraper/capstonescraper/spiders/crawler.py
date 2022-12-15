import scrapy
import sys
import mysql.connector

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']


    def parse(self, response):
    
        # Create a MySQL connection and cursor
        db = mysql.connector.connect(
            host="my-database.clh7uaufcnt6.us-east-1.rds.amazonaws.com",
            user="admin",
            password="team2project",
            database="CrawlerProject"
        )
        cursor = db.cursor()

        # Display all products in li Odd class
        for products in response.css('li.Odd'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
            names = products.css('a.pname::text').get(), 
            prices = products.css('em.p-price::text').get(), 
            links = products.css('a').attrib['href']

            # Insert the scraped data into the "products" table in MySQL
            query = ("INSERT INTO products(name, price, link) VALUES (%s, %s, %s)", (names, prices, links))
            cursor.execute(query)
            #cursor.commit()

        # Display all products in li Even class
        for products in response.css('li.Even'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
            names = products.css('a.pname::text').get(), 
            price = products.css('em.p-price::text').get(), 
            link = products.css('a').attrib['href']

        for url in response.css('div.SideCategoryListFlyout'):
            for links in url.css('a'):
                if 'href' in links.attrib and links.attrib['href'].startswith("http"):
                    yield response.follow(links, callback = self.parse)

        # Commit the changes to the database
        db.commit()
        
        # Close the cursor and database connection
        cursor.close()
        db.close()
