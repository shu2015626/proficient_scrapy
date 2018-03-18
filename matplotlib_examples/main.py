# -*- coding:utf-8 -*-
__author__ = "sunsn"

from scrapy.cmdline import execute

if __name__ =="__main__":
    # execute(["scrapy", "crawl", "mpl_examples"])
    execute(["scrapy", "crawl", "mpl_examples", '-o', 'examples.json'])

