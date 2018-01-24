from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
from ScrapyScrape.items import ScrapscrapyItem

class ScrapscrapySpide(BaseSpider):
    name = "ss"
    allowed_domains = ["scrapy.org"]
    start_urls = ["http://scrapy.org"]

    def parse(self,response):
        sel = Selector (response)
        item = ScrapscrapyItem()
        item['Heading'] = sel.xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[2]/p/text()').extract()
        item['Content'] = sel.xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/span[2]').extract()
        item['Source'] = "http://scrapy.org"
        return item
