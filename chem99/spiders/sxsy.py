# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import PriceSXSY
import re
import datetime
import logging
import lxml.html
import urlparse

class SxsySpider(scrapy.Spider):
    name = "sxsy"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://www.chem99.com/',
    )
    index_page = 'http://plas.chem99.com/news/?cx=1&sname=%E7%BB%8D%E5%85%B4%E4%B8%89%E5%9C%86PP'

    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-绍兴三圆PP')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PLASTIC_SXSY'])
 
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
        request = scrapy.http.Request(url=type(self).index_page, 
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
        auth_info = ''.join(response.xpath('//div[@class="news_title_b"]//text()').extract())
        pub_date = re.compile('(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})').search(auth_info).group(1)
        logging.debug(title)
        data_list = table_to_list(data_table2)
        tab_title = data_list[0][1].strip()
        for row in data_list[1:]:
            item = PriceSXSY()
            item['produce_code']        = row[0].strip()
            item['price']               = row[1].strip()
            item['rise_offset']         = row[2].strip()
            item['remarks']             = row[3].strip()
            item['title']               = title
            item['trading_dt']          = pub_date
            item['tab_title']           = tab_title
            item['datetime_stamp']      = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            yield item
