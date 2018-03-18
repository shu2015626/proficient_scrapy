# -*- coding:utf-8 -*-
__author__ = "sunsn"


from scrapy.cmdline import execute


if __name__ == "__main__":
    # execute(["scrapy", "crawl", "books"])
    execute(["scrapy", "crawl", "books", '-t', 'excel', '-o', './%(name)s/%(time)s.xls'])
