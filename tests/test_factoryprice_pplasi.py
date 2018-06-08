# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from chem99.spiders.factoryprice_pplasi import FactorypricePplasiSpider
import os
import logging

class FactorypricePplasiSpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = FactorypricePplasiSpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/factoryprice_pplasi.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://plas.chem99.com/news/20663334.html'
        title = u'国内PP拉丝出厂价格汇总（20160302）'
        trading_dt = '20160302'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        items = list(items)
        self.assertEqual(len(items), 57)
        
        self.assertEqual(items[0]['region'],u'中石化华北')
        self.assertEqual(items[0]['produce_code'],u'S1003')
        self.assertEqual(items[0]['produce_name'],u'燕山石化')
        self.assertEqual(items[0]['pre_price'],u'6300')
        self.assertEqual(items[0]['price'],u'6300')
        self.assertEqual(items[0]['rise_offset'],u'0')
        self.assertEqual(items[0]['remarks'],u'定价')
        self.assertEqual(items[0]['title'],title)
        self.assertEqual(items[0]['trading_dt'],trading_dt)
        
        self.assertEqual(items[1]['region'],u'中石化华北')
        self.assertEqual(items[1]['produce_code'],u'T30S')
        self.assertEqual(items[1]['produce_name'],u'齐鲁石化')
        self.assertEqual(items[1]['pre_price'],u'6400')
        self.assertEqual(items[1]['price'],u'6400')
        self.assertEqual(items[1]['rise_offset'],u'0')
        self.assertEqual(items[1]['remarks'],u'定价')
        self.assertEqual(items[1]['title'],title)
        self.assertEqual(items[1]['trading_dt'],trading_dt)
        
        self.assertEqual(items[2]['region'],u'中石化华北')
        self.assertEqual(items[2]['produce_code'],u'T30S(PPH-T03)')
        self.assertEqual(items[2]['produce_name'],u'济南炼厂')
        self.assertEqual(items[2]['pre_price'],u'6300')
        self.assertEqual(items[2]['price'],u'6300')
        self.assertEqual(items[2]['rise_offset'],u'0')
        self.assertEqual(items[2]['remarks'],u'定价')
        self.assertEqual(items[2]['title'],title)
        self.assertEqual(items[2]['trading_dt'],trading_dt)
        
        self.assertEqual(items[7]['region'],u'中石化华东')
        self.assertEqual(items[7]['produce_code'],u'T300')
        self.assertEqual(items[7]['produce_name'],u'上海石化')
        self.assertEqual(items[7]['pre_price'],u'6450')
        self.assertEqual(items[7]['price'],u'6600')
        self.assertEqual(items[7]['rise_offset'],u'150')
        self.assertEqual(items[7]['remarks'],u'定价')
        self.assertEqual(items[7]['title'],title)
        self.assertEqual(items[7]['trading_dt'],trading_dt)