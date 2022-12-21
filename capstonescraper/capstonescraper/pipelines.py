# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector


from itemadapter import ItemAdapter

class myspiderPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="my-database.clh7uaufcnt6.us-east-1.rds.amazonaws.com",
            user="admin",
            password="team2project",
            database="chamberstestdb"
        )
        # Create the cursor
        self.cur = self.conn.cursor()
        
        #Create table.  If it does not exist, prog will create it.
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS newtable (
            id int NOT NULL auto_increment, 
            keyword VARCHAR(64),
            times_mentioned int,
            url VARCHAR(255),
            PRIMARY KEY (id),
            unique (url, keyword)           
        )
        """)
    
    def process_item(self, item, spider):
        #Define the insert statement
        self.cur.execute("""insert ignore into newtable (keyword, times_mentioned, url) values (%s,%s,%s)""", (
            item["keyword"],
            item['times_mentioned'],
            item["url"]
        ))
        


        #insert data into db
        self.conn.commit()
        return item
        
    def close_spider(self, spider):
        #close cursor and connection to the db
        self.cur.close()
        self.conn.close()    

