# -*- coding: utf-8 -*-
import scrapy
from ..items import RedditUserItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class RedditSpider(CrawlSpider):
    name = "reddit"
    allowed_domains = ["reddit.com"]
    start_urls = (
        'https://www.reddit.com',
    )

    rules = (
        Rule(SgmlLinkExtractor(allow=[r'\\?count=.+']), follow=True),
        Rule(SgmlLinkExtractor(allow=[r'user/.+']), callback='parse_item')
    )    

    def parse_item(self, response):
    	hxs = Selector(response)
        item = RedditUserItem()

        username = hxs.xpath('//*[@class="titlebox"]/h1/text()').extract()
        print username
        if username: 
        	item['username'] = username[0]
        else:
        	item = None

        return item    
