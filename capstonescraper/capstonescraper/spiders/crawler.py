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

        # Connect to the database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pancho12!",
            database="whiskyshopusa"
        )

        # Insert the extracted data into the products table
        for products in response.css('li.Even'):
            cursor.execute(
                "INSERT INTO products (name, price, link) VALUES (%s, %s, %s)",
                (products.css('a.pname::text').get()['name'], products.css('em.p-price::text').get()['price'], products.css('a').attrib['href']['link'])
            )
            
        # Get the cursor
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE whiskyshopusa")
        
        cursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255), link VARCHAR(255))")
        
        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()

