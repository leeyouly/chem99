# -*- coding: utf-8 -*-
import scrapy
from chem99.table import table_to_list
from chem99.items import MarketPricePP
import re
import datetime
import logging
import lxml.html
import urlparse

class MarketPricePPzaishengSpider(scrapy.Spider):
    name = "marketprice_ppzaisheng"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://www.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-再生PP普通杂料破碎料')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PP_MARKET_PRICE'])
 
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
        for i in range(1,3):
            request = scrapy.http.Request(url='http://plas.chem99.com/news/?page={0}&sid=4723&k=1&sname=%E6%99%AE%E9%80%9A%E6%9D%82%E6%96%99'.format(i), 
                callback = self.parse_index)
            yield request
        
    def parse_index(self, response):
        for link in response.xpath('//div[@class="news_content"]/ul/li'):
            link_title = link.xpath('./a[1]/text()').extract_first()
            link_url = urlparse.urljoin(response.url, link.xpath('./a/@href').extract_first())
            data_date = ''.join(link.xpath('./a[@class="date"]//text()').extract()).strip()
            data_date = data_date.strip('[').strip(']')
            if u'临沂再生PP普通杂料破碎料' in link_title:
                yield scrapy.http.Request(url = link_url, 
                                          meta = {'data_date':data_date},
                                          callback=self.parse_content)
            

    def parse_content(self, response):
        doc = lxml.html.document_fromstring(response.body_as_unicode())
        data_table2 = doc.xpath('//div[@id="PanelContent"]//table')[0]

        title = ''.join(response.xpath('//div[@class="news_content "]/h1//text()').extract()).strip()
        logging.debug(title)
        data_date = datetime.datetime.strptime(response.meta['data_date'][0:10], '%Y-%m-%d')
        data_list = table_to_list(data_table2)
        
        if len(data_list) <= 1 or len(data_list[1]) < 5:
            raise 'PLAS.CHEM99----get table failed %s' % response.url
        
        for row in data_list[1:]:
            item = MarketPricePP()
            item['materials'] = row[0].strip()
            item['product'] = row[1].strip()
            item['price'] = row[2].strip()
            item['rise_offset'] = row[3].strip()
            item['remarks'] = row[4].strip()
            item['datadate'] = data_date
            item['update_dt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['source'] = title
            yield item
