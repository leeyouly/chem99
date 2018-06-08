# -*- coding: utf-8 -*-
import scrapy
import scrapy.http
from chem99.table import table_to_list
from chem99.items import t_ec_merey_oil_Item
import re
import datetime


class MereyOilSpider(scrapy.Spider):
    name = "spd_t_ec_merey_oil"
    allowed_domains = ["chem99.com"]
    start_urls = (
        'http://www.chem99.com/',
    )

    def parse(self, response):
        self.crawler.stats.set_value('spiderlog/source_name', u'卓创-马瑞原油贴水')
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
                artlistURL = 'http://oil.chem99.com/news/s128.html'
            else:
                artlistURL = 'http://oil.chem99.com/news/?page='+str(page)+'&sid=128'
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
            if u'马瑞原油' in artTitle:
                request = scrapy.http.FormRequest(url=artUrl, callback=self.parse_content,)
                request.meta['datadate'] = datadate
                yield request

    def parse_content(self, response):
        datadate = response.meta['datadate']

        data_table = response.xpath('//*[@id="Panel_News"]/div[1]/table')
        data_list = table_to_list(data_table)
        wti_date_range = re.findall(u'WTI均价（(.+)）',data_list[0][1])[0]
        for data in data_list[1:]:
            item = t_ec_merey_oil_Item()
            item['datadate'] = datadate
            item['datemonth'] = data[0]
            item['wti_price_avg'] = data[1]
            item['wti_date_range'] = wti_date_range
            item['discount_value'] = data[2]
            item['tongs_barrels_ratio'] = data[3]
            item['fx_rate'] = data[4]
            item['settle_prc'] = data[5]
            item['update_dt'] = datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S')
            item['source'] = response.url
            yield item

