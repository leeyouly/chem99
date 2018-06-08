# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import RubbThailand
import re
import datetime
import logging
import lxml.html
import urlparse
import urllib
from scrapy.http import HtmlResponse


class ThailandRubbSpider(scrapy.Spider):
    name = "thailand_rubb"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://rubb.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-泰国合艾市场原料')
        self.crawler.stats.set_value('spiderlog/target_tables', ['T_EC_CHEM_RUBB_THAILAND'])

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
            if u'泰国合艾市场' in title:
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
        if doc.xpath('//form[@id="frm_login"]'):
            raise Exception('Login error')

        if doc.xpath('//div[@id="Panel1"]//table'):
            data_table = doc.xpath('//div[@id="Panel1"]//table')[0]
            data_list = table_to_list(data_table)
            if len(data_list) <= 1 or len(data_list[0]) < 5:
                raise Exception('RUBB.CHEM99----get table failed %s' % response.url)

            row = data_list[len(data_list) - 1]
            for index in range(1, len(data_list[0])):
                item = RubbThailand()
                item['product'] = data_list[0][index].strip()
                item['price'] = row[index].strip()
                item['remark'] = remark
                try:
                    item['datadate'] = datetime.datetime.strptime(row[0].strip(), '%Y/%m/%d')
                except:
                    item['datadate'] = date
                item['update_dt'] = datetime.datetime.now()
                item['source'] = title
                yield item