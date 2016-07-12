# -*- coding: utf-8 -*-
import json
import codecs
import logging

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = logging.getLogger(__name__)
class ScrapytestPipeline(object):
    def __init__(self):
        try:
            self.file = codecs.open('C:\Users\simon\Desktop\enaihuo.json', 'wb', encoding='utf-8')
        except IOError,msg:
            print(msg)
            raise

    def process_item(self, item, spider):
        logger.info('-----------process_item------------do')
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        # self.file.close()
        return item
