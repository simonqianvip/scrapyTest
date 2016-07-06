# -*- coding: utf-8 -*-
import json
import codecs

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapytestPipeline(object):
    def __init__(self):
        self.file = codecs.open('enaihuo.json', 'wb', encoding='utf-8')
        # self.file = codecs.open('enaihuo.json','wb')

    def process_item(self, item, spider):
        print('-----------process_item------------do')
        line = json.dumps(dict(item)) + '\n'
        # print line
        self.file.write(line.decode("unicode_escape"))
        return item
