# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import SchoolItem

class LagouSpider(CrawlSpider):
    name = 'edusoho'
    allowed_domains = ['edusoho.com']
    start_urls = ['http://www.edusoho.com/cases']

    rules = (
        Rule(LinkExtractor(allow=r'cases'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for sel in response.xpath('//div[@class="case-item-content plm"]'):
            school_item = SchoolItem();
            school_item['title'] = sel.xpath('div[1]/a/text()').extract()
            school_item['link'] = sel.xpath('div[6]/span[1]/a/@href').extract()
            yield school_item
