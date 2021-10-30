import scrapy


class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['http://stockpage.10jqka.com.cn/600004/company/']
    start_urls = ['http://stockpage.10jqka.com.cn/600004/company/']

    def parse(self, response):
        #//*[@id="ml_001"]/table/tbody/tr[1]/td[1]/a
        res_selector=response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a")
        print(response)
        pass
