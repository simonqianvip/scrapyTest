# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapyTest.items import ScrapytestItem
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

import sys


# from scrapy import log
PAGE = "http://www.enaihuo.com/news/list-629.html"

class DmozSpider(scrapy.Spider):
    name = "enaihuo"
    allowed_domains = ["enaihuo.com"]
    start_urls = [
        "http://www.enaihuo.com/news/list-629.html",
        # "http://www.enaihuo.com/news/list-629-2.html",
        # "http://www.enaihuo.com/news/list-629-3.html",
        # "http://www.enaihuo.com/news/list-629-4.html",
        # "http://www.enaihuo.com/news/list-629-5.html",
    ]

    def parse(self, response):
        print('-----------parse------------do')
        sel = Selector(response)
        # //*[@id="destoon_previous"]
        sites = sel.xpath('//div/dl/dd/div[@class="pages"]')
        items = []
        for site in sites:
            item = ScrapytestItem()
            # 取出page的最后的一页
            page_url = site.xpath('input[@id="destoon_previous"]/@value').extract()
            # print(page_url)
            for p in page_url:
                if p:
                    splits = p.split("-")
                    # print(splits)
                    if splits:
                        lastWord = splits[len(splits) - 1]
                        # print(lastWord)
                        word_splits = lastWord.split(".")
                        # print(word_splits[0])
                        sum_page = word_splits[0]
                else:
                    print('nothing')

        sp = PAGE.split(".html")

        url_item = []
        for i in range(2, int(sum_page) + 1, 1):
            url = sp[0] + "-" + str(i) + ".html"
            # print(sp[0]+"-"+str(i)+".html")
            url_item.append(url)
        # print(url_item)
        #page_url集合
        for url in url_item:
            yield Request(url, callback=self.parse_url)
            break
            print('url=%s'%url)

    def parse_url(self, response):
        print('-----------parse_url------------do')
        sel = Selector(response)
        sites = sel.xpath('//div/dl/dd/div')
        items = []
        for site in sites:
            item = ScrapytestItem()
            title = site.xpath('h3/a/text()').extract()
            link = site.xpath('div/a/@href').extract()

            if len(link) == 0:
                print("it's none link")
            else:
                url = link[0]
            item['link'] = url.encode('utf-8')
            item['title'] = [t.encode('utf-8') for t in title]
            items.append(item)
        for item in items:
            yield Request(item['link'], meta={'item': item}, callback=self.parse_content)
            break
            print('link=%s'%item['link'])

    def parse_content(self, response):
        print('-----------parse_content------------do')
        hxs = HtmlXPathSelector(response)
        items = []
        content = hxs.select('//div/div/div/div/p/text()').extract()
        item = response.meta['item']
        item['content'] = [c.encode('utf-8') for c in content]
        items.append(item)
        return items

        # def parse(self, response):
        #     sel = Selector(response)
        #     sites = sel.xpath('//div/dl/dd/div')
        #     items = []
        #     for site in sites:
        #         item = ScrapytestItem()
        #         title = site.xpath('h3/a/text()').extract()
        #         link = site.xpath('div/a/@href').extract()
        #         previous_page_url = site.xpath('input[@id="destoon_previous"]/@value').extract()
        #
        #         if len(link)==0:
        #             print("it's none link")
        #         else:
        #             url = link[0]
        #         item['link'] = url.encode('utf-8')
        #         item['title'] = [t.encode('utf-8') for t in title]
        #         items.append(item)
        #     for item in items:
        #         yield Request(item['link'],meta={'item':item},callback=self.parse_url)

        # def parse_url(self,response):
        #     hxs =HtmlXPathSelector(response)
        #     items = []
        #     content = hxs.select('//div/div/div/div/p/text()').extract()
        #     item = response.meta['item']
        #     item['content'] = [c.encode('utf-8') for c in content]
        #     items.append(item)
        #     return items
