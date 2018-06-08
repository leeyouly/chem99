# -*- coding: utf-8 -*-
import scrapy
from chem99.table import table_to_list
import re
import logging
import urlparse
from scrapy.http.cookies import CookieJar

class FactorypriceLdpeSpider(scrapy.Spider):
    name = "factoryprice_ldpe_test"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://plas.chem99.com/',
    )
    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-国内LDPE出厂价')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PLASTIC'])
 
        request = scrapy.http.Request(url='http://plas.chem99.com/include/head.aspx', callback=self.parse_head)
        return [request]
        
    def parse_head(self, response):
        request = scrapy.http.FormRequest(response.url,
            formdata = {
                'SciName':'chaoschina',
                'SciPwd':'gyp888', 
                'IB_Login.x':'28',
                'IB_Login.y':'16'}, 
                callback = self.login_callback)
        return [request]
        
    def login_callback(self, response):
        cookiejar = CookieJar()
        cookiejar.extract_cookies(response, response.request)
        self.cookiejar = cookiejar

        logging.debug('enter login_callback')
        request = scrapy.http.Request(url='http://oil.chem99.com/news/28156799.html',
            callback = self.parse_content)
        return [request]
        
    def parse_index(self, response):
        for link in response.xpath('//div[@class="news_content"]/ul/li/a[@href]'):
            link_url = link.xpath('@href').extract_first()
            if link_url.strip() == '#':
                continue
            link_url = urlparse.urljoin(response.url, link_url)
            yield scrapy.http.Request(url = link_url, callback=self.parse_content)
            

    def parse_content(self, response):
        data_table = response.xpath('//*[@id="Panel_News"]/div[1]/table')
        data_list = table_to_list(data_table)

        a = 'aaa'