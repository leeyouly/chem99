# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import RubbUSSThailand
import re
import datetime
import logging
import lxml.html
import urlparse
import urllib
from scrapy.http import HtmlResponse


class ThailandRubbUSSSpider(scrapy.Spider):
    name = "thailand_rubbuss"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://rubb.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-泰国三大中心市场USS原料交易行情')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_RUBBUSS_THAILAND'])

        request = scrapy.http.Request(url='http://rubb.chem99.com/include/loginhead.aspx', callback=self.parse_head)
        return [request]

    def parse_head(self, response):
        request = scrapy.http.FormRequest.from_response(
            response,
            formdata={
                'SciName': 'yhcy666',
                'SciPwd': '123789',
                'IB_Login.x': '23',
                'IB_Login.y': '14'},
            callback=self.login_callback)
        return [request]

    def login_callback(self, response):
        # for i in range(1, 27):
        #     url = 'http://rubb.chem99.com/news/?page={0}&sid=4299'.format(i)
        #     yield scrapy.http.Request(url=url, callback=self.parse_index)
        request = scrapy.http.Request(url='http://rubb.chem99.com/news/s4299.html',
                                      callback=self.parse_index)
        return [request]

    def parse_index(self, response):
        for link in response.xpath('//ul[@class="w700_list"]/li'):
            link_url = link.xpath('./a/@href').extract_first()
            link_url = urlparse.urljoin(response.url, link_url)
            title = ''.join(link.xpath('.//text()').extract()).strip()
            if u'泰国三大中心市场USS' in title:
                if u'泰国三大中心市场USS原料交易行情（2010115）' in title:
                    date = datetime.datetime(2016, 1, 15)
                else:
                    date = re.search('\d{8}', title).group()
                    date = datetime.datetime.strptime(date, '%Y%m%d')
                yield scrapy.http.Request(
                    url=link_url,
                    meta={'date': date, 'title': title,},
                    callback=self.parse_content)

    def parse_content(self, response):
        date = response.meta['date']
        title = response.meta['title']
        remark = ''.join(response.xpath('//div[@id="Panel1"]/p[1]//text()').extract()).strip()
        logging.debug(title)

        doc = lxml.html.document_fromstring(response.body_as_unicode())
        data_table = doc.xpath('//div[@id="Panel1"]//table')[0]
        data_list = table_to_list(data_table)
        if not (len(data_list[0]) == 11 or len(data_list[0]) == 7):
            raise Exception('RUBB.CHEM99----get table failed %s' % response.url)

        if len(data_list[0]) == 11:
            for row in data_list[2:]:
                item = RubbUSSThailand()
                item['product'] = row[0].strip()
                item['price'] = row[1].strip()
                item['price_3_5'] = row[2].strip()
                item['price_5_7'] = row[3].strip()
                item['price_7_10'] = row[4].strip()
                item['price_10_15'] = row[5].strip()
                item['volume'] = row[6].strip()
                item['volume_3_5'] = row[7].strip()
                item['volume_5_7'] = row[8].strip()
                item['volume_7_10'] = row[9].strip()
                item['volume_10_15'] = row[10].strip()
                item['remark'] = remark
                item['datadate'] = date
                item['update_dt'] = datetime.datetime.now()
                item['source'] = title
                yield item
        elif len(data_list[0]) == 7:
            for row in data_list[1:]:
                item = RubbUSSThailand()
                item['product'] = row[0].strip()
                item['price'] = row[1].strip()
                item['price_3_5'] = row[2].strip()
                item['price_5_7'] = row[3].strip()
                item['price_7_10'] = row[4].strip()
                item['price_10_15'] = row[5].strip()
                item['remark'] = remark
                item['datadate'] = date
                item['update_dt'] = datetime.datetime.now()
                item['source'] = title
                yield item