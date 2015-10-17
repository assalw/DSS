# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# This is an example template class
class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class RedditUserPipeline(object):
 
    def process_item(self, item, spider):
 
        if not item is None :
            item.save()

        return item