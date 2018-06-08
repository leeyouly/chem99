# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import t_ec_check_bitumenItem ,t_ec_rateofoperation_bitumenItem
import re
import datetime


class BitumenSpider(scrapy.Spider):
    name = "spd_t_ec_bitumen_operate"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://www.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-沥青装置开工率')
        self.crawler.stats.set_value('spiderlog/target_tables', ['t_ec_asphalt_operate'])

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

        for page in range(1,2,1):
            if page == 1 :
                artlistURL = 'http://oil.chem99.com/news/s4844.html'
            else:
                artlistURL = 'http://oil.chem99.com/news/?page='+str(page)+'&sid=4844'
            request = scrapy.http.Request(url=artlistURL, callback=self.parse_articleList)
            yield request


    def parse_articleList(self, response):
        artListHtml = response.xpath('.//div[@class="news_div_main_l"]/div[@class="div_news"]/div/ul[@class="ul_14"]/li')
        # pagecookie = {
        #
        #     'guid': '054a4412-f067-1793-d255-fbb0a9fbdd56',
        #     'isCloseOrderZHLayer': '0',
        #     'UM_distinctid': '163b3d88a2a381-0a59943b3dd3a1-8383667-1fa400-163b3d88a2b75a',
        #     'Hm_lvt_f80092420c79d7f5d2822acdb956aea2': '1527730714',
        #     'route': '5381fa73df88cce076c9e01d13c9b378',
        #     'ASP.NET_SessionId': '4yewrfzpdqwq555knqh0bkf5',
        #     'STATcUrl': '',
        #     'Hm_lvt_6ae6e5df26994111589a523f104d0cba': '1527073831,1527649721,1527730427,1527749525',
        #     'Hm_lpvt_6ae6e5df26994111589a523f104d0cba': '1527750517',
        #     'STATReferrerIndexId': '1',
        #
        # }
        for artList in artListHtml:

            datadate = artList.xpath('./span/text()').extract()[0].replace('[', '').replace(']', '')
            if len(datadate) < 4:
                datadate = artList.xpath('./span//text()').extract()[1].replace('[', '').replace(']', '')
            artTitle = artList.xpath('./a/text()').extract()[0]
            artUrl = response.urljoin(artList.xpath('./a/@href').extract()[0])
            datatype = 0
            if u'开工率' in artTitle:
                datatype = 1
            elif u'沥青装置检修' in artTitle:
                datatype = 2
                # print artUrl
            request = scrapy.http.FormRequest(url=artUrl, callback=self.parse_content,)
            request.meta['datadate'] = datadate
            request.meta['datatype'] = datatype
            yield request

    def parse_content(self, response):
        datadate = response.meta['datadate']
        datatype = response.meta['datatype']
        if datatype == 3 :
            print response.url
        if datatype == 1 :
            data_table = response.xpath('//*[@id="Panel_News"]/div[1]/table')
            data_list = table_to_list(data_table)
            last_week_date = datetime.datetime.strptime(datadate, '%Y-%m-%d') - datetime.timedelta(days=7)
            for data in data_list[1:]:
                item = t_ec_rateofoperation_bitumenItem()
                item['datadate'] = datadate
                item['area'] = data[0]
                item['current_week_date'] = datadate
                item['last_week_date'] = last_week_date.strftime( '%Y-%m-%d')
                item['current_week_value'] = data[1]
                item['last_week_value'] = data[2]
                item['change_situation'] = data[3]
                item['update_dt'] = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S')
                item['source'] = response.url
                yield item

        if datatype == 2 :

            data_table = response.xpath('//*[@id="Panel_News"]/div[1]/table')
            data_list = table_to_list(data_table)
            print data_list
            for data in data_list[1:]:
                item = t_ec_check_bitumenItem()
                if len(data[0])< 6:
                    item['area'] = data[0]
                    item['datadate'] = datadate
                    item['factory_name'] = data[1]
                    item['affiliation'] = data[2]
                    item['product'] = data[3]
                    item['status'] = data[4]
                    item['product_time'] = data[5]
                    item['update_dt'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    item['source'] = response.url
                    yield item
                else:
                    continue

