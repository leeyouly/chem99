# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import FactoryPricePP
import re
import datetime
import logging
import lxml.html
import urlparse

class FactorypricePpfenSpider(scrapy.Spider):
    name = "factoryprice_ppfen"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://plas.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-PP粉料企业出厂价格')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PP_FACTORY_PRICE'])
 
        request = scrapy.http.Request(url='http://plas.chem99.com/include/head.aspx', callback=self.parse_head)
        return [request]
        
    def parse_head(self, response):
        request = scrapy.http.FormRequest.from_response(response, 
            formdata = {
                'SciName':'chaoschina',
                'SciPwd':'gyp888', 
                'IB_Login.x':'28',
                'IB_Login.y':'16'}, 
                callback = self.login_callback)
        return [request]
        
    def login_callback(self, response):
        request = scrapy.http.Request(url='http://plas.chem99.com/news/?cx=1&sname=PP%E7%B2%89%E6%96%99%E4%BC%81%E4%B8%9A', 
            callback = self.parse_index)
        return [request]
        
    def parse_index(self, response):
        for link in response.xpath('//div[@class="news_content"]/ul/li/a[@href]'):
            link_url = link.xpath('@href').extract_first()
            if link_url.strip() == '#':
                continue
            link_url = urlparse.urljoin(response.url, link_url)
            yield scrapy.http.Request(url = link_url, callback=self.parse_content)
            

    def parse_content(self, response):
        doc = lxml.html.document_fromstring(response.body_as_unicode())
        data_table2 = doc.xpath('//div[@id="PanelContent"]//table')[0]
        title = ''.join(response.xpath('//div[@class="news_content "]/h1//text()').extract()).strip()
        logging.debug(title)
        data_date = re.compile('(\d{8})').search(title).group(1)
        data_list = table_to_list(data_table2)
        
        for row in data_list[1:]:
            item = FactoryPricePP()
            item['area']            = row[0].strip()
            item['factory_name']    = row[1].strip()
            item['price']           = row[2].strip()
            item['rise_offset']     = row[3].strip()
            item['remarks']         = row[4].strip()
            item['title']           = title
            item['trading_dt']      = data_date
            item['datetime_stamp']  = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item
