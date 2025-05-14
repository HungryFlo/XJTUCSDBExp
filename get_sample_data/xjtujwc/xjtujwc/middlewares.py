# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

def get_cookies():
    cookies_str = "_WEU=Z8r1LyyDGteOvAVYa23D9td6zushL4gZ1S2RRT3luioQgKM4ndYDOZTNPd_illym*vePQillyytjIB7lxqVcJvqfWVUji*9jxCjxl9Lz_U7tpJpQ1OpXuRhC4yJrnXgJUOqTLLF9o30foEnVn2*3v5ON7W62YFqVH5sbuUZhSN5fn1dU*LYHc52rTRdBWGRi; EMAP_LANG=zh; THEME=cherry; JSESSIONID=0XDPbBvEIhLGnGuvvx5F0bu_9mQ8Ux8GBEWhK44ZULLPO7vBl3Qz!989385591; route=8b9256afce303b2bfefa79284f0e767c; MOD_AMP_AUTH=MOD_AMP_8d6e1249-8d69-4312-aa09-de71ac253b15; amp.locale=undefined; asessionid=3d4dc8bc-3a22-440d-9309-60aa959ffedd; CASTGC=plXj2hpTFptwjb0yWXiaOcOFpxYOtGreIrx4mws9xLnpHfr3TlXLNw==; CASTGC=TGT-2613947-EkZDccBzXg1QOzsJ5AqVghrRnJkStJAxfpiQvsXqbtWqnvNaJT-gdscas01"
    cookies = {}
    item = cookies_str.split("; ")
    for i in item:
        print(i)
        key, value = i.split("=", maxsplit=1)
        cookies.update({key: value})
    return cookies

COOKIES = get_cookies()

class XjtujwcSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class XjtujwcDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        request.cookies = COOKIES
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
