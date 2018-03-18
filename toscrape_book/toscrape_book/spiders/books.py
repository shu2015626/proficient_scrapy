# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        '''
        解析页面中每本书的详细连接,以及下一页的连接
        :param response:
        :return:
        '''
        # 获取每本书的详细连接
        le = LinkExtractor(restrict_css='article.product_pod h3')
        links = le.extract_links(response)
        if links:
            for link in links:
                yield scrapy.Request(url=link.url, callback=self.parse_book)

        # 获取下一页的连接, 就一个链接
        le = LinkExtractor(restrict_xpaths='//li[@class="next"]/a')
        if le.extract_links(response):
            next_url = le.extract_links(response)[0].url
            yield scrapy.Request(url=next_url, callback=self.parse)

    def parse_book(self, response):
        '''
        解析书籍详细信息
        :param response:
        :return:
        '''
        book = BookItem()
        sel = response.css('div.product_main')
        book['name'] = sel.xpath(".//h1/text()").extract_first().strip()
        book['price'] = sel.css("p.price_color::text").extract_first().strip()
        book['review_rating'] = sel.xpath("./p[contains(@class,'star-rating')]/@class").re_first('star-rating (\w*)').strip()

        sel = response.xpath(".//table[@class='table table-striped']")
        book['upc'] = sel.css('tr')[0].css('td::text').extract_first().strip()
        book['review_num'] = sel.xpath("(.//tr)[last()]/td/text()").extract_first().strip()
        book['stock'] = sel.xpath("(.//tr)[last()-1]/td/text()").re_first('In stock \((\d+) available\)').strip()
        
        yield book

