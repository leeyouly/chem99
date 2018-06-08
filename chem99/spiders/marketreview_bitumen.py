# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list, trans_table
from chem99.items import MarketReviewBitumen
import re
import datetime
import logging
import lxml.html
import urlparse
import urllib
from scrapy.http import HtmlResponse


class MarketReviewBitumenSpider(scrapy.Spider):
    name = "marketreview_bitumen"
    allowed_domains = ["chem99.com"]
    start_urls = (
            'http://oil.chem99.com/',
    )
    
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-沥青市场回顾和展望')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_BM_CHEM_BITUMEN_MARKET'])
        
        request = scrapy.http.Request(url='http://oil.chem99.com/include/loginframetop.aspx', callback=self.parse_head)
        return [request]

    def parse_head(self, response):
        request = scrapy.http.FormRequest.from_response(response, 
            formdata = {
                'chemname':'kftz88',
                'chempwd':'kf2012',
                'Btn_Login.x':'35',
                'Btn_Login.y':'6'}, 
                callback = self.login_callback)
        return [request]
        
    def login_callback(self, response):
        request = scrapy.http.Request(url='http://oil.chem99.com/news/?page=1&sid=127&sname=%E5%91%A8%E8%AF%84', 
            callback = self.parse_index)
        return [request]


    def parse_index(self, response):
        for link in response.xpath('//ul[@class="ul_14"][1]/li'):
            link_url = link.xpath('./a/@href').extract_first()
            data_date = link.xpath('./span/text()').extract_first()
            if link_url.strip() == '#' or data_date is None:
                continue
            data_date = data_date.strip('[').strip(']')
            link_url = urlparse.urljoin(response.url, link_url)
            yield scrapy.http.Request(url = link_url, 
                                      meta = {'data_date':data_date },
                                      callback=self.parse_content)
            

    def parse_content(self, response):
        doc = lxml.html.document_fromstring(response.body_as_unicode())
        data_table = doc.xpath('//div[@id="Panel_News"]//table')[0]
        title = ''.join(response.xpath('//div[@class="div_news"]/h1//text()').extract()).strip()
        logging.debug(title)
        data_date = datetime.datetime.strptime(response.meta['data_date'], '%Y-%m-%d')
        data_list = table_to_list(data_table)
        #行列转置，一共5列
        data_list = trans_table(data_list[0:5])
        
        if len(data_list) <= 1 or len(data_list[1]) < 5:
            logging.error('OIL.CHEM99----get table failed %s' % response.url)
        
        unit = None
        match = re.search(u'单位：(.*)', doc.xpath('//div[@id="Panel_News"]//p/text()')[1].strip())
        if match:
            unit = match.group(1)
 
        for row in data_list[1:]:
            item = MarketReviewBitumen()
            item['area'] = row[0].strip()
            item['pre_price'] = row[1].strip()
            item['price'] = row[2].strip()
            item['change'] = row[3].strip()
            item['changeratio'] = row[4].strip()
            if unit:
                item['unit'] = unit
            item['datadate'] = data_date
            item['update_dt'] = datetime.datetime.now()
            item['source'] = title
            yield item