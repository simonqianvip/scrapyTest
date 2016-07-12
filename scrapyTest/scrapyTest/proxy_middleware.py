# -*-coding:utf-8-*-
import random
import logging
import chardet

logger = logging.getLogger(__name__)


# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy_ip = random.choice(self.user_agent_ip_list)
        try:
            print(unicode(proxy_ip).encode("utf-8"))
            request.meta['proxy'] = proxy_ip
        except Exception,msg:
            logger.info(msg)
            pass
        logger.info('%s' % proxy_ip)

    user_agent_ip_list = ["http://101.200.192.2:8090",
                          "http://106.75.128.89:80",
                          "http://123.56.235.141:81"
                          ]
