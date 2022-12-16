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
        
        #Create Chamberstestdb.  If it does not exist, prog will create it.
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS chamberstestdb (
            id int NOT NULL auto_increment,
            keyword,
            times mentioned,
            url VARCHAR(255),
            PRIMARY KEY (id)            
        )
        """)
    
    def process_item(self, item, spider):
        #Define the insert statement
        self.cur.execute("""insert into chamberstestdb (keyword, times mentioned, url) values (%s,%s,%s)""", (
            item["keyword"],
            str(item['times mentioned']),
            item["url"]
        ))
        
        #insert data into db
        self.conn.commit()
        
    def close_spider(self, spider):
        
        #close cursor and connection to the db
        self.cur.close()
        self.conn.close()    
        
class CapstonescraperPipeline:
    def process_item(self, item, spider):
        return item
