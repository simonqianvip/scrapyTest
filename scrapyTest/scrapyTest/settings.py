# -*- coding: utf-8 -*-

# Scrapy settings for scrapyTest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


# Scrapy项目实现的bot的名字(也为项目名称)。 这将用来构造默认 User-Agent，同时也用来log
BOT_NAME = 'scrapyTest'

# Scrapy搜索spider的模块列表,例如：SPIDER_MODULES = ['mybot.spiders_prod', 'mybot.spiders_dev']
SPIDER_MODULES = ['scrapyTest.spiders']

# 使用 genspider 命令创建新spider的模块
NEWSPIDER_MODULE = 'scrapyTest.spiders'

# Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值(默认100)
# CONCURRENT_ITEMS = 100

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 爬取的默认User-Agent
# USER_AGENT = 'scrapyTest (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 该中间件过滤所有robots.txt eclusion standard中禁止的request
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Scrapy downloader 并发请求(concurrent requests)的最大值
# CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度,减轻服务器压力,同时也支持小数:(默认是0)
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:

# 对单个网站进行并发请求的最大值。(默认是8)
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1

# 对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定， 使用该设定。 也就是说，并发限制将针对IP，而不是网站
# CONCURRENT_REQUESTS_PER_IP = 16
CONCURRENT_REQUESTS_PER_IP = 1

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# Scrapy HTTP Request使用的默认header。由 DefaultHeadersMiddleware 产生
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapyTest.middlewares.MyCustomSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapyTest.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'scrapyTest.Rotate_useragent.RotateUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    # 'scrapyTest.proxy_middleware.ProxyMiddleware': 100,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# 保存项目中启用的插件及其顺序的字典
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 不过值(value)习惯设定在0-1000范围内
# ITEM_PIPELINES = {
#    'scrapyTest.pipelines.SomePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# 自动限速(通过计算建立TCP连接到接收到HTTP包头(header)之间的时间来测量的)
AUTOTHROTTLE_ENABLED = True

# The initial download delay
# 初始下载延迟(默认单位为秒)
AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
# 在高延迟情况下最大的下载延迟(单位秒)
AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False
#起用AutoThrottle调试(debug)模式，展示每个接收到的response。 您可以通过此来查看限速参数是如何实时被调整的。
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 禁止cookies,防止被ban
COOKIES_ENABLED = False
# 爬取网站最大允许的深度(depth)值。如果为0，则没有限制
DEPTH_LIMIT = 2

ITEM_PIPELINES = {
    'scrapyTest.pipelines.ScrapytestPipeline': 300
}

# 整数值。用于根据深度调整request优先级。
# 如果为0，则不根据深度进行优先级调整
# DEPTH_PRIORITY(默认0)

# 是否收集最大深度数据(默认TRUE)
# DEPTH_STATS

# 是否收集详细的深度数据。如果启用，每个深度的请求数将会被收集在数据中
# DEPTH_STATS_VERBOSE(默认false)

# 降低log的级别
# LOG_LEVEL = 'INFO'

# 禁止重定向
# RETRY_ENABLED = False

# 启用"Ajax Crawlable Pages"爬取
# AJAXCRAWL_ENABLED = True

# 下载器超时时间(单位: 秒)(默认180秒)
DOWNLOAD_TIMEOUT = 180

# 默认的 (RFPDupeFilter) 过滤器基于 scrapy.utils.request.request_fingerprint 函数生成的请求fingerprint(指纹)。 如果您需要修改检测的方式，
# 您可以继承 RFPDupeFilter 并覆盖其 request_fingerprint 方法。 该方法接收 Request 对象并返回其fingerprint(一个字符串)。
# 用于检测过滤重复请求的类
# DUPEFILTER_CLASS='scrapy.dupefilter.RFPDupeFilter'

# 默认情况下， RFPDupeFilter 只记录第一次重复的请求。 设置 DUPEFILTER_DEBUG 为 True 将会使其记录所有重复的requests
# DUPEFILTER_DEBUG(默认False)


# 是否启用logging(默认true)
# LOG_ENABLED

# logging使用的编码。
# LOG_ENCODING
# 默认: 'utf-8'

# LOG_FILE
# 默认: None
# logging输出的文件名。如果为None，则使用标准错误输出(standard error)。
#
LOG_LEVEL = 'INFO'
# 默认: 'DEBUG'
# log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG。更多内容请查看 Logging 。
#
# LOG_STDOUT
# 默认: False
# 如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。例如， 执行 print 'hello' ，其将会在Scrapy log中显示。
#
# MEMUSAGE_LIMIT_MB
# 默认: 0
# 在关闭Scrapy之前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不做限制


# 如果启用，当从相同的网站获取数据时，Scrapy将会等待一个随机的值 (0.5到1.5之间的一个随机值 * DOWNLOAD_DELAY)。
# 该随机值降低了crawler被检测到(接着被block)的机会。某些网站会分析请求， 查找请求之间时间的相似性。
# RANDOMIZE_DOWNLOAD_DELAY

LOG_ENCODING = 'utf-8'
LOG_FILE='scrapyTest_log'
