# -*- coding: utf-8 -*-
import scrapy
from chem99.table import table_to_list
from chem99.items import FactoryPrice
import re
import datetime
import logging
import lxml.html
import urlparse

class FactorypriceLldpeSpider(scrapy.Spider):
    name = "factoryprice_lldpe"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://plas.chem99.com/',
    )

    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-国内LLDPE出厂价')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PLASTIC'])
 
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
        request = scrapy.http.Request(url='http://plas.chem99.com/news/?cx=1&sname=%E5%9B%BD%E5%86%85LLDPE%E5%87%BA%E5%8E%82', 
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
        data_table = response.xpath('//div[@id="PanelContent"]//table')[0]
        doc = lxml.html.document_fromstring(response.body_as_unicode())
        data_table2 = doc.xpath('//div[@id="PanelContent"]//table')[0]
        #logging.debug(data_table2)
        #logging.debug(lxml.html.tostring(data_table2))
        title = ''.join(response.xpath('//div[@class="news_content "]/h1//text()').extract()).strip()
        logging.debug(title)
        data_date = re.compile('(\d{8})').search(title).group(1)
        data_list = table_to_list(data_table2)
        
        for row in data_list[1:]:
            item = FactoryPrice()
            item['region'] = row[0].strip()
            item['produce_code'] = row[1].strip()
            item['produce_name'] = row[2].strip()
            item['pre_price'] = row[3].strip()
            item['price'] = row[4].strip()
            item['rise_offset'] = row[5].strip()
            if len(row) >= 7:
                item['remarks'] = row[6].strip()
                item['remarks'] = row[6].strip()
            item['title'] = title
            item['trading_dt'] = data_date
            item['datetime_stamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item
