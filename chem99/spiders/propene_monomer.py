# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import PropeneMonomer
import re
import datetime
import logging
import lxml.html
import urlparse

class PropeneMonomerSpider(scrapy.Spider):
    name = "propene_monomer"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://www.chem99.com/',
    )
    index_page = 'http://plas.chem99.com/news/?cx=1&sname=PP%E7%B2%89%E6%96%99%E6%97%A5%E8%AF%84'

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-PP粉料日评-丙烯单体')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PROPENE_MONOMER'])
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
        data_table2 = doc.xpath('//div[@id="PanelContent"]//table')[1]
        title = ''.join(response.xpath('//div[@class="news_content "]/h1//text()').extract()).strip()
        auth_info = ''.join(response.xpath('//div[@class="news_title_b"]//text()').extract())
        pub_date = re.compile('(\d{8})').search(title).group(1)
        logging.debug(title)
        
        for p_text in response.xpath('//div[@id="PanelContent"]//p//text() | //div[@id="PanelContent"]//div//text()').extract():
            if (u'表' in p_text) and \
                (u'国内' in p_text) and \
                (u'丙烯' in p_text) and \
                (u'价格一览' in p_text):
                tab_title = p_text.strip()
        
        data_list = table_to_list(data_table2)
        
        item1 = PropeneMonomer()
        item1['column_type'] = u'价格'
        item1['sd_area'] = data_list[1][1].strip()
        item1['hb_area'] = data_list[1][2].strip()
        item1['hd_area'] = data_list[1][3].strip()
        item1['xb_area'] = data_list[1][4].strip()
        item1['db_area'] = data_list[1][5].strip()
        item1['hn_area'] = data_list[1][6].strip()
        item1['title'] = title
        item1['tab_title'] = tab_title
        item1['trading_dt'] = pub_date
        item1['datetime_stamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        item2 = PropeneMonomer()
        item2['column_type'] = u'涨跌'
        item2['sd_area'] = data_list[2][1].strip()
        item2['hb_area'] = data_list[2][2].strip()
        item2['hd_area'] = data_list[2][3].strip()
        item2['xb_area'] = data_list[2][4].strip()
        item2['db_area'] = data_list[2][5].strip()
        item2['hn_area'] = data_list[2][6].strip()
        item2['title'] = title
        item2['tab_title'] = tab_title
        item2['trading_dt'] = pub_date
        item2['datetime_stamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return [item1, item2]

