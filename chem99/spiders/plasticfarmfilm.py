# -*- coding: utf-8 -*-
import scrapy
from chem99.table import table_to_list
from chem99.items import PlasticFarmFilm
import re
import datetime
import logging
import lxml.html
import urlparse

class PlasticFarmFilmSpider(scrapy.Spider):
    name = "plasticfarmfilm"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://plas.chem99.com/',
    )
    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-农膜日评')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PLASTIC_FARMFILM'])
 
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
        for i in range(1,2):
            request = scrapy.http.Request(url='http://plas.chem99.com/news/?page={0}&sid=4520&k=1&sname=%E6%97%A5%E8%AF%84'.format(i), 
                callback = self.parse_index)
            yield request
        
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

        title = ''.join(response.xpath('//div[@class="news_content "]/h1//text()').extract()).strip()
        logging.debug(title)
        data_date = datetime.datetime.strptime(re.compile('(\d{8})').search(title).group(1), '%Y%m%d')
        data_list = table_to_list(data_table2)
        
        if len(data_list) <= 1 or len(data_list[1]) < 4:
            raise 'CHEM99----get table failed %s' % response.url
        
        for row in data_list[1:]:
            for index in range(1, len(row)):
                item = PlasticFarmFilm()
                item['product'] = row[0].strip()
                item['area'] = data_list[0][index].strip()
                item['price'] = row[index].strip()
                item['datadate'] = data_date
                item['update_dt'] = datetime.datetime.now()
                item['source'] = title
                yield item
            
            
