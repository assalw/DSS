# -*- coding: utf-8 -*-
import scrapy
from ..items import GitHubUserItem


class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = (
        'http://www.github.com/',
    )

    def parse(self, response):
        return GitHubUserItem(username = 'test')
