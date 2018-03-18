# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import os
from urllib.parse import urlparse

class MatplotlibExamplesPipeline(object):
    def process_item(self, item, spider):
        return item


class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        return os.path.join(os.path.basename(os.path.dirname(path)), os.path.basename(path))
