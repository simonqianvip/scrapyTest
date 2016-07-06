import scrapy.cmdline

if __name__ == '__main__':
    # --set LOG_FILE=log
    scrapy.cmdline.execute(argv=['scrapy','crawl','enaihuo','--set','LOG_FILE=log'])
    # scrapy.cmdline.execute(argv=['scrapy','crawl','enaihuo'])