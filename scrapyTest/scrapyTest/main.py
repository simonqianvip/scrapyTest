# -*- coding: utf-8 -*-
import scrapy.cmdline

import logging
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # --set LOG_FILE=log
    # scrapy.cmdline.execute(argv=['scrapy','crawl','enaihuo','--set','LOG_FILE=‪C:\Users\simon\Desktop\scrapyTest-log'])
    logger.info('cmd scrapy crawl enaihuo')
    scrapy.cmdline.execute(argv=['scrapy','crawl','enaihuo'])
