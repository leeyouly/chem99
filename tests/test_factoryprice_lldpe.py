# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from chem99.spiders.factoryprice_lldpe import FactorypriceLldpeSpider
import os
import logging

class GlobalmarketNaphthaSpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = FactorypriceLldpeSpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/factoryprice_lldpe.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://plas.chem99.com/news/20662823.html'
        title = u'国内LLDPE出厂价格汇总（20160302）'
        trading_dt = '20160302'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        items = list(items)
        self.assertEqual(len(items), 67)
        
        self.assertEqual(items[0]['region'],u'中石化华北')
        self.assertEqual(items[0]['produce_code'],u'7042')
        self.assertEqual(items[0]['produce_name'],u'齐鲁石化')
        self.assertEqual(items[0]['pre_price'],u'8800')
        self.assertEqual(items[0]['price'],u'8800')
        self.assertEqual(items[0]['rise_offset'],u'0')
        self.assertEqual(items[0]['remarks'],u'定价')
        self.assertEqual(items[0]['title'],title)
        self.assertEqual(items[0]['trading_dt'],trading_dt)
        
        self.assertEqual(items[1]['region'],u'中石化华北')
        self.assertEqual(items[1]['produce_code'],u'7149U')
        self.assertEqual(items[1]['produce_name'],u'齐鲁石化')
        self.assertEqual(items[1]['pre_price'],u'9000')
        self.assertEqual(items[1]['price'],u'9000')
        self.assertEqual(items[1]['rise_offset'],u'0')
        self.assertEqual(items[1]['remarks'],u'定价')
        self.assertEqual(items[1]['title'],title)
        self.assertEqual(items[1]['trading_dt'],trading_dt)
        
        self.assertEqual(items[2]['region'],u'中石化华北')
        self.assertEqual(items[2]['produce_code'],u'QLLF30')
        self.assertEqual(items[2]['produce_name'],u'齐鲁石化')
        self.assertEqual(items[2]['pre_price'],u'8600')
        self.assertEqual(items[2]['price'],u'8600')
        self.assertEqual(items[2]['rise_offset'],u'0')
        self.assertEqual(items[2]['remarks'],u'定价')
        self.assertEqual(items[2]['title'],title)
        self.assertEqual(items[2]['trading_dt'],trading_dt)
        
        self.assertEqual(items[12]['region'],u'中石化华北')
        self.assertEqual(items[12]['produce_code'],u'6010')
        self.assertEqual(items[12]['produce_name'],u'天津联合')
        self.assertEqual(items[12]['pre_price'],u'9050')
        self.assertEqual(items[12]['price'],u'9050')
        self.assertEqual(items[12]['rise_offset'],u'0')
        self.assertEqual(items[12]['remarks'],u'定价')
        self.assertEqual(items[12]['title'],title)
        self.assertEqual(items[12]['trading_dt'],trading_dt)
        
        self.assertEqual(items[13]['region'],u'中石化华东')
        self.assertEqual(items[13]['produce_code'],u'7042')
        self.assertEqual(items[13]['produce_name'],u'扬子石化')
        self.assertEqual(items[13]['pre_price'],u'8900')
        self.assertEqual(items[13]['price'],u'8900')
        self.assertEqual(items[13]['rise_offset'],u'0')
        self.assertEqual(items[13]['remarks'],u'定价')
        self.assertEqual(items[13]['title'],title)
        self.assertEqual(items[13]['trading_dt'],trading_dt)
        