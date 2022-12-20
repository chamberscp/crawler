import scrapy
import re

class myspider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://treeremoval.com'] 
    blocked_domains = [blocked_domains.txt]
    custom_settings = {'DOWNLOAD_DELAY': 0.2}
    
    def parse(self, response):
        allWords = {}
        
        if 'content-type' in response.headers and b'text/html' in response.headers['content-type']:
            for title in response.css('.mw-page-title-main'):
                print({'title': title.css('::text').get()})
                
            for s in response.css("body p::text").getall():
                for w in filter(None, re.split("[ \t\n\-\xA0-]+", s)):
                    w = w.casefold()
                    w = w.strip().strip(".,?:[]()\"")
                    w = w.removesuffix("'s")
                    w = w.strip("'")
                    
                    if len(w) >= 3 and w not in ["the", "and"]:
                        if w in allWords:
                            allWords[w] += 1
                        else:
                            allWords[w] = 1
                            
            for w in sorted(allWords, key=allWords.get):
                print(w, allWords[w])

                yield {'url': response.url, 'keyword': w, 'times_mentioned': allWords[w]}
                
            for next_page in response.css('a'):
                if 'href' in next_page.attrib and next_page.attrib['href'].startswith("http"):
                    yield response.follow(next_page, self.parse)
                        
                                         
                            
                        