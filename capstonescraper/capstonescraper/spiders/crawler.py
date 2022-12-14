import scrapy
import sys
import mysql.connector

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    allowed_domains = ['www.whiskyshopusa.com']
    start_urls = ['http://www.whiskyshopusa.com/']

    # Create a MySQL connection and cursor
    db = mysql.connector.connect(
        host="my-database.clh7uaufcnt6.us-east-1.rds.amazonaws.com",
        user="admin",
        password="team2project",
        database="CrawlerProject"
    )
    cursor = db.cursor()
    
    cursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255), link VARCHAR(255))")

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
            self.cursor.execute("INSERT INTO products (name, price, link) VALUES (%s, %s, %s)", (name, price, link))
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
            self.cursor.execute("INSERT INTO products (name, price, link) VALUES (%s, %s, %s)", (name, price, link))
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
