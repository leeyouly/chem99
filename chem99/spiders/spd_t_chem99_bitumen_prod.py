# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import t_chem99_bithumen_prod_Item
from scrapy.utils.project import get_project_settings
import re
from scrapy.http.cookies import CookieJar
import datetime


class BitumenSpider(scrapy.Spider):
    name = "spd_t_chem99_bitumen_prod"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://www.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-沥青产量分类统计表')
        self.crawler.stats.set_value('spiderlog/target_tables', ['t_chem99_bithumen_prod_f'])

        request = scrapy.http.Request(url='http://oil.chem99.com/include/loginframetop.aspx', callback=self.parse_head)
        return [request]

    def parse_head(self, response):
        request = scrapy.http.FormRequest.from_response(response,
                                                        formdata={
                                                            'chemname': 'kftz88',
                                                            'chempwd': 'kf2012',
                                                            'Btn_Login.x': '35',
                                                            'Btn_Login.y': '6'},
                                                        callback=self.login_callback)
        return [request]

    def login_callback(self, response):

        # artlistURL = 'http://oil.chem99.com/news/28156799.html'
        # request = scrapy.http.Request(url=artlistURL, callback=self.parse_content)
        # return [request]

        for page in range(1,2,1):
            if page == 1 :
                artlistURL = 'http://oil.chem99.com/news/s128-1-B2FAC1BF.html'
            else:
                artlistURL = 'http://oil.chem99.com/news/?page='+str(page)+'&sid=128&k=1&sname=%E4%BA%A7%E9%87%8F'
            request = scrapy.http.Request(url=artlistURL, callback=self.parse_articleList)
            yield request


    def parse_articleList(self, response):

        # pagecookie = {
        #     'UM_distinctid': '163b3d88a2a381-0a59943b3dd3a1-8383667-1fa400-163b3d88a2b75a',
        #     'Hm_lvt_f80092420c79d7f5d2822acdb956aea2': '1527730714',
        #     'guid': '054a4412-f067-1793-d255-fbb0a9fbdd56',
        #     'route': '5381fa73df88cce076c9e01d13c9b378',
        #     'ASP.NET_SessionId': 'uac02wdy1ysxd0cbnkylb1ca',
        #     'isCloseOrderZHLayer': '0',
        #     'STATcUrl': '',
        #     'Hm_lvt_6ae6e5df26994111589a523f104d0cba': '1527730427,1527749525,1527836816,1528182833',
        #     'Hm_lpvt_6ae6e5df26994111589a523f104d0cba': '1528204477',
        #     'STATReferrerIndexId': '1',
        # }
        artListHtml = response.xpath(
            '/html/body/div[6]/div[1]/div/div[1]/ul/li')
        for artList in artListHtml:
            datadate = artList.xpath('./span/text()').extract()[0].replace('[', '').replace(']', '')
            if len(datadate) < 4:
                datadate = artList.xpath('./span//text()').extract()[1].replace('[', '').replace(']', '')
            artTitle = artList.xpath('./a/text()').extract()[0]
            artUrl = ''
            datatype = 3
            if u'分地区' in artTitle:
                datatype = 1
                artUrl = response.urljoin(artList.xpath('./a/@href').extract()[0])
            if u'分集团' in artTitle:
                datatype = 2
                artUrl = response.urljoin(artList.xpath('./a/@href').extract()[0])
                # print artUrl
            if artUrl <> '':
                request = scrapy.http.FormRequest(url=artUrl, callback=self.parse_content,)
                request.meta['datadate'] = datadate
                request.meta['datatype'] = datatype
                yield request

    def parse_content(self, response):
        datadate = response.meta['datadate']
        datatype = response.meta['datatype']
        print datatype
        data_table = response.xpath('//*[@id="Panel_News"]/div[1]/table')
        data_list = table_to_list(data_table)
        if len(data_list[0]) > 7:
            datemonth =data_list[0][1]
            for data in data_list[1:]:
                item = t_chem99_bithumen_prod_Item()
                item['datadate'] = datadate
                item['datemonth'] = datemonth
                if datatype == 1:
                    item['cls_type'] = u'地区'
                elif datatype == 2:
                    item['cls_type'] = u'集团'
                item['item_name'] = data[0]
                item['curr_month_value'] = data[1]
                item['pre_month_value'] = data[2]
                item['mom'] = data[3]
                item['pre_year_value'] = data[4]
                item['yoy'] = data[5]
                item['cumu_value_y'] = data[6]
                item['pre_cumu_value_y'] = data[7]
                item['cumu_yoy'] = data[8]
                item['update_dt'] = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S')
                item['source'] = response.url
                yield item
