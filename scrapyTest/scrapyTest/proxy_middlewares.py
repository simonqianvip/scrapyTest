# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random
import logging
# Start your middleware class

logger = logging.getLogger(__name__)
class ProxyMiddleware(object):
    # overwrite process request
    # def process_request(self, request, spider):
        # Set the location of the proxy
        # request.meta['proxy'] = "http://YOUR_PROXY_IP:PORT"
        # request.meta['proxy'] = "http://61.135.217.3:80"


        # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"

        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

    def process_request(self, request, spider):
        # Set the location of the proxy
        proxy_ip = random.choice(self.user_agent_ip_list)
        request.meta['proxy'] = proxy_ip
        # print '+'*8, 'the Current ip address is', proxy_ip, '+'*8
        logger.info('the Current ip address is %s' %proxy_ip)

    # ip from http://pachong.org/
    user_agent_ip_list = [\
        # "http://61.135.217.7:80",
        "http://101.200.192.2:8090",
        # "http://106.38.251.62:8088",
        "http://42.248.207.88:8888"
       ]