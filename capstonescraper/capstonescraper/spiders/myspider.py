import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class myspider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://treeremoval.com'] 
    custom_settings = {'DOWNLOAD_DELAY': 0.2}
    
    rules = [Rule(LinkExtractor(deny = ('https://www.google.com', 'https://www.facebook.com', 'https://www.youtube.com', 'https://www.baidu.com', 'https://www.yahoo.com', 'https://www.amazon.com', 'https://www.wikipedia.org', 'https://www.qq.com', 'https://www.twitter.com', 'https://www.slashdot.org', 'https://www.google.co.in', 'https://www.taobao.com', 'https://www.live.com', 'https://www.sina.com.cn', 'https://www.yahoo.co.jp', 'https://www.linkedin.com', 'https://www.weibo.com', 'https://www.ebay.com', 'https://www.google.co.jp', 'https://www.yandex.ru', 'https://www.bing.com', 'https://www.vk.com', 'https://www.hao123.com', 'https://www.google.de', 'https://www.instagram.com', 'https://www.t.co', 'https://www.msn.com', 'https://www.amazon.co.jp', 'https://www.tmall.com', 'https://www.google.co.uk', 'https://www.pinterest.com', 'https://www.ask.com', 'https://www.reddit.com', 'https://www.wordpress.com', 'https://www.mail.ru', 'https://www.google.fr', 'https://www.blogspot.com', 'https://www.paypal.com', 'https://www.onclickads.net', 'https://www.google.com.br', 'https://www.tumblr.com', 'https://www.apple.com', 'https://www.google.ru', 'https://www.aliexpress.com', 'https://www.sohu.com', 'https://www.microsoft.com', 'https://www.imgur.com', 'https://www.xvideos.com', 'https://www.google.it', 'https://www.imdb.com', 'https://www.google.es', 'https://www.netflix.com', 'https://www.gmw.cn', 'https://www.amazon.de', 'https://www.fc2.com', 'https://www.360.cn', 'https://www.alibaba.com', 'https://www.go.com', 'https://www.stackoverflow.com', 'https://www.ok.ru', 'https://www.google.com.mx', 'https://www.google.ca', 'https://www.amazon.in', 'https://www.google.com.hk', 'https://www.tianya.cn', 'https://www.amazon.co.uk', 'https://www.craigslist.org', 'https://www.pornhub.com', 'https://www.rakuten.co.jp', 'https://www.naver.com', 'https://www.blogger.com', 'https://www.diply.com', 'https://www.google.com.tr', 'https://www.xhamster.com', 'https://www.flipkart.com', 'https://www.espn.go.com', 'https://www.soso.com', 'https://www.outbrain.com', 'https://www.nicovideo.jp', 'https://www.google.co.id', 'https://www.cnn.com', 'https://www.xinhuanet.com', 'https://www.dropbox.com', 'https://www.google.co.kr', 'https://www.googleusercontent.com', 'https://www.github.com', 'https://www.bongacams.com', 'https://www.ebay.de', 'https://www.kat.cr', 'https://www.bbc.co.uk', 'https://www.google.pl', 'https://www.google.com.au', 'https://www.pixnet.net', 'https://www.tradeadexchange.com', 'https://www.popads.net', 'https://www.googleadservices.com', 'https://www.ebay.co.uk', 'https://www.dailymotion.com', 'https://www.sogou.com', 'https://www.adnetworkperformance.com'), callback ='parse_func', follow = True))]

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
                        
                                         
                            
                        