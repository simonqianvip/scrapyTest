# -*- coding: utf-8 -*-


from scrapy.item import Item, Field


class ScrapytestItem(Item):
    title = Field()
    link = Field()
    content = Field()
    # desc = Field()
