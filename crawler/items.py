# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from scrapy.item import Field

# Django models import
from verticalsearch.models import GitHubUser

class GitHubUserItem(DjangoItem):
    django_model = GitHubUser
