# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapyTest.items import ScrapytestItem
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

import sys
import logging

reload(sys)
sys.setdefaultencoding('utf-8')
# from scrapy import log
PAGE = "http://www.enaihuo.com/news/list-629.html"

logger = logging.getLogger(__name__)
class DmozSpider(scrapy.Spider):
    name = "enaihuo"
    allowed_domains = ["enaihuo.com"]
    start_urls = [
        "http://www.enaihuo.com/news/list-629.html",
        # "http://www.enaihuo.com/news/list-629-2.html",
    ]

    def parse(self, response):
        '''
        解析主页面总的page，然后推算出所有的page列表
        '''
        logger.info('-----------parse------------do')
        sel = Selector(response)
        sites = sel.xpath('//div/dl/dd/div[@class="pages"]')
        items = []
        for site in sites:
            item = ScrapytestItem()
            # 取出page的最后的一页
            page_url = site.xpath('input[@id="destoon_previous"]/@value').extract()
            for p in page_url:
                if p:
                    splits = p.split("-")
                    if splits:
                        lastWord = splits[len(splits) - 1]
                        word_splits = lastWord.split(".")
                        sum_page = word_splits[0]
                else:
                    print('nothing')
        sp = PAGE.split(".html")
        url_item = []
        for i in range(2, int(sum_page) + 1, 1):
            url = sp[0] + "-" + str(i) + ".html"
            url_item.append(PAGE)
            url_item.append(url)
        #page_url集合
        i = 0
        for url in url_item:
            yield Request(url, callback=self.parse_url)
            i+=1
            if(i == 1):
                print('i=%s'%i)
                break
            print('url=%s'%url)

    def parse_url(self, response):
        """
        解析每个page页里所有文章的url
        """
        print(response.url)
        logger.info('-----------parse_url------------do')
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
        i = 0
        for item in items:
            yield Request(item['link'], meta={'item': item}, callback=self.parse_content)
            i+=1
            print('link=%s'%item['link'])
            if i==2:
                break

    def parse_content(self, response):
        """
        解析每个文章的内容
        :param response:
        :return:
        """
        logger.info('-----------parse_content------------do')
        hxs = HtmlXPathSelector(response)
        items = []
        content = hxs.select('//div/div/div/div/p/text()').extract()
        item = response.meta['item']
        item['content'] = [c.encode('utf-8') for c in content]
        items.append(item)
        return items

