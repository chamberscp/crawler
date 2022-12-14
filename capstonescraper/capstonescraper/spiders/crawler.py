import scrapy
import sys
import mysql.connector
import pymysql
import mariadb

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']

        # Connect to the MariaDB database
    cursor = mariadb.connect(
        user='user',
        password='password',
        host='host',
        database='database'
    )
    cursor = db.cursor()

    def parse(self, response):
        # Display all products in li Odd class
        for products in response.css('li.Odd'):
            yield {
                'name': products.css('a.pname::text').get(), 
                'price': products.css('em.p-price::text').get(), 
                'link': products.css('a').attrib['href']
            }
            name = products.css('a.pname::text').get(), 
            price = products.css('em.p-price::text').get(), 
            link = products.css('a').attrib['href']

            # Insert the scraped data into the "products" table in MySQL
            self.cursor.execute("ALTER INTO products (name, price, link) VALUES (%s, %s, %s)", (name, price, link))
            self.db.commit()

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
            
            # Insert the scraped data into the "products" table in MySQL
            self.cursor.execute("ALTER INTO products (name, price, link) VALUES (%s, %s, %s)", (name, price, link))
            self.db.commit()

        for url in response.css('div.SideCategoryListFlyout'):
            for links in url.css('a'):
                if 'href' in links.attrib and links.attrib['href'].startswith("http"):
                    yield response.follow(links, callback = self.parse)

        # Commit the changes to the database
        db.commit()
        
        # Close the cursor and database connection
        cursor.close()
        db.close()
