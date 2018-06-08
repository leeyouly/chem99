# -*- coding: utf-8 -*-
import scrapy
from chem99.table import table_to_list
from chem99.items import PlasticFilm
import re
import datetime
import logging
import lxml.html
import urlparse

class PlasticFilmSpider(scrapy.Spider):
    name = "plasticfilm"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://plas.chem99.com/',
    )
    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-塑膜收盘价格表')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_PLASTIC_FILM'])
 
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
            request = scrapy.http.Request(url='http://plas.chem99.com/news/so.aspx?page={0}&sname=%E5%A1%91%E8%86%9C%E6%94%B6%E7%9B%98%E4%BB%B7%E6%A0%BC%E8%A1%A8'.format(i), 
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

        data_list = table_to_list(data_table2)
        
        if len(data_list) <= 1 or len(data_list[1]) < 7:
            raise 'CHEM99----get table failed %s' % response.url

        datematch = re.search('(\d{8})', title)
        if datematch:
            data_date = datetime.datetime.strptime(datematch.group(1), '%Y%m%d')
        else:
            year = re.search('(\d{7})', title).group(1)[0:4]
            monday = re.search(u'(\d+)月(\d+)日', data_list[0][2])
            month = monday.group(1)
            day = monday.group(2)
            data_date = datetime.datetime(int(year), int(month), int(day))

        for row in data_list[1:]:
            item = PlasticFilm()
            item['product'] = row[0].strip()
            item['spec'] = row[1].strip()
            item['price'] = row[2].strip()
            item['rise_offset'] = row[3].strip()
            item['than_lastweek'] = row[4].strip()
            item['than_lastmonth'] = row[5].strip()
            item['than_lastyear'] = row[6].strip()
            item['datadate'] = data_date
            item['update_dt'] = datetime.datetime.now()
            item['source'] = title
            yield item
            
            
