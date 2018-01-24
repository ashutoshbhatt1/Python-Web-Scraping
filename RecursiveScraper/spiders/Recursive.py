from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from RecursiveScraper.items import RecursivescraperItem


class RecursiveScraperSpider(CrawlSpider):
    name = "rs"
    allowed_domains = ["deepakkumarsangit.com"]
    start_urls = ["http://deepakkumarsangit.com/index.html"]

    rules = (
        Rule(SgmlLinkExtractor(allow=("http://deepakkumarsangit\.com/*.",)), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = RecursivescraperItem()
        item['URL'] = response.request.url
        print response.request.url
        item['content'] = sel.xpath('/html/body/div[1]/div[2]/div/div[1]/div[1]/div[3]/p[1]/text()').extract()
        return item
