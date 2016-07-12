# -*- coding: utf-8 -*-


from scrapy.item import Item, Field

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ScrapytestItem(Item):
    title = Field()
    link = Field()
    content = Field()
    # desc = Field()
