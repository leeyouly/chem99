# -*- coding: utf-8 -*-
import scrapy
#from chem99.table import table_to_list
from chem99.table2 import table_to_list,table_to_list2
from chem99.items import t_ec_chem_pvc_start_rateItem
from scrapy.utils.project import get_project_settings
import re
import datetime
import logging
import lxml.html
import urlparse

class PlasticFarmFilmSpider(scrapy.Spider):
    name = "spd_t_chem_pvc_start_rate"
    allowed_domains = ["chem99.com", "sci99.com"]
    start_urls = (
        'http://ca.chem99.com/',
    )
    ignore_page_incremental = True
    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创周度PVC企业开工率')
        self.crawler.stats.set_value('spiderlog/target_tables', ['t_chem_pvc_start_rate'])

        request = scrapy.http.Request(url='http://ca.chem99.com/include/login.aspx', callback=self.parse_head)
        return [request]

    def parse_head(self, response):
        request = scrapy.http.FormRequest.from_response(
            response,
            formdata = {
                "chemname": "chaoschina",
                "chempwd": "gyp888",
                "fl1": "0",
                "ImageButton1.x": "27",
                "ImageButton1.y": "25"
            },
            callback = self.login_callback)
        return [request]

    def login_callback(self, response):
        for pages in range(2,51):
            urls='http://ca.chem99.com/news/?page=%d&sid=3267'%(pages)
            #urls ='http://ca.chem99.com/channel/pvc/'
            request = scrapy.http.Request(url=urls,
                callback = self.parse_index)
            yield request

    def parse_index(self, response):
        datalist = response.xpath('/html/body/div/div[@class="div_main_l w706"]/div[@class="news_content"]/ul/li')
        datatime = response.xpath('/html/body/div/div[@class="div_main_l w706"]/div[@class="news_content"]/ul/li/span/text()').extract()
        datatitle  = response.xpath('/html/body/div/div[@class="div_main_l w706"]/div[@class="news_content"]/ul/li/a/text()').extract()
        dataurl = response.xpath('/html/body/div/div[@class="div_main_l w706"]/div[@class="news_content"]/ul/li/a/@href').extract()
        # request = scrapy.http.Request(url='http://ca.chem99.com/news/27188348.html',callback=self.parse_content)
        # yield request

        for link in range(0,len(datalist)):
            datadate = datatime[link].replace('[','').replace(']','')
            title = datatitle[link].replace('\r\n', '').replace(' ', '')
            link_url = 'http://ca.chem99.com/news/'+dataurl[link]
            if  u'本周PVC企业开工率' in title:
                yield scrapy.http.Request(url = link_url, meta={'datadate':datadate,'title':title},callback=self.parse_content)


    def parse_content(self, response):
        print response.url
        print 111
        print 222
        data_table = table_to_list(response.xpath('//*[@id="zoom"]/table'))
        for row in range(1,len(data_table)):
            item = t_ec_chem_pvc_start_rateItem()
            item['datadate'] = response.meta['datadate']
            item['regions'] = data_table[row][0]
            item['area'] = data_table[row][1]
            item['factory'] = data_table[row][2]
            item['technology'] = data_table[row][3]
            item['pvc_number'] = data_table[row][4]
            item['start_rate'] = data_table[row][5]
            item['update_dt'] = datetime.datetime.now()
            item['source'] = response.meta['title']
            yield item

        # for row in range(1,len(data_table)+1):
        #     data_table.xpath('./td')


        # title = ''.join(response.xpath('//div[@class="news_content "]/h1//text()').extract()).strip()
        # logging.debug(title)
        # data_date = datetime.datetime.strptime(re.compile('(\d{8})').search(title).group(1), '%Y%m%d')
        # #data_list = table_to_list(data_table2)
        #
        # if len(data_list) <= 1 or len(data_list[1]) < 4:
        #     raise 'CHEM99----get table failed %s' % response.url
        #
        # for row in data_list[1:]:
        #     for index in range(1, len(row)):
        #         item = PlasticFarmFilm()
        #         item['product'] = row[0].strip()
        #         item['area'] = data_list[0][index].strip()
        #         item['price'] = row[index].strip()
        #         item['datadate'] = data_date
        #         item['update_dt'] = datetime.datetime.now()
        #         item['source'] = title
        #         yield item
        #
            
