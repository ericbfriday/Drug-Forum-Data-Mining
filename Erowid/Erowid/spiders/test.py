import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector

from Erowid.items import ErowidItem


class ExperiencesSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["www.erowid.org"]
    start_urls = ['https://www.erowid.org/experiences/subs/exp_aPVP.shtml']
    rules = [ 
        Rule(LinkExtractor(allow =('/experiences/exp.php?ID=[0-9]+')), callback = 'parse_item', follow = True)
    
    ]
    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        title = hxs.select('//@href')
        print title.extract