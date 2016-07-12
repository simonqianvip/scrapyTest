# -*- coding: utf-8 -*-
import scrapy.cmdline

import logging
logger = logging.getLogger(__name__)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    # scrapy.cmdline.execute(argv=['scrapy','crawl','enaihuo','--set','LOG_FILE=‪C:\Users\simon\Desktop\scrapyTest-log'])
    scrapy.cmdline.execute(argv=['scrapy','crawl','enaihuo'])
