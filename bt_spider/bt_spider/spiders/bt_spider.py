import scrapy
import json

class bt_spider(scrapy.Spider):
    name = "bt_spider"
    allowed_domains = ["bornetelefonen.dk"]
    with open("btelefonen_urls_sample.csv", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        page = response.css('title::text').get()
        content = response.xpath('normalize-space(//*[@id="main"]/div[1]/div/div[1]/div/div/div/div[2]/div)').getall() 
        answer = response.xpath('normalize-space(//*[@id="main"]/div[1]/div/div[1]/div/div/div/div[3]/div[2]/div)').get() 
        yield {'page' : page,
               'content' : content,
               'answer' : answer,
               }
