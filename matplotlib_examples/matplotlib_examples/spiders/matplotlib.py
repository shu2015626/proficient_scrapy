# -*- coding: utf-8 -*-
import scrapy


class MatplotlibSpider(scrapy.Spider):
    name = 'matplotlib'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/']

    def parse(self, response):
        pass
