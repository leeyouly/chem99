# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from chem99.spiders.factoryprice_ppfen import FactorypricePpfenSpider
import os
import logging

class GlobalmarketNaphthaSpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = FactorypricePpfenSpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/factoryprice_ppfen.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://plas.chem99.com/news/20675227.html'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        title = u'PP粉料企业出厂价格汇总（20160303）'
        trading_dt = '20160303'
        
        items = list(items)
        self.assertEqual(len(items), 54)
        
        self.assertEqual(items[0]['area'],u'山东地区')
        self.assertEqual(items[0]['factory_name'],u'丰汇新材料')
        self.assertEqual(items[0]['price'],u'6000')
        self.assertEqual(items[0]['rise_offset'],u'0')
        self.assertEqual(items[0]['remarks'],u'停车')
        self.assertEqual(items[0]['title'],title)
        self.assertEqual(items[0]['trading_dt'],trading_dt)
        
        self.assertEqual(items[1]['area'],u'山东地区')
        self.assertEqual(items[1]['factory_name'],u'东明炼厂')
        self.assertEqual(items[1]['price'],u'6450')
        self.assertEqual(items[1]['rise_offset'],u'100')
        self.assertEqual(items[1]['remarks'],u'--')
        self.assertEqual(items[1]['title'],title)
        self.assertEqual(items[1]['trading_dt'],trading_dt)

        self.assertEqual(items[2]['area'],u'山东地区')
        self.assertEqual(items[2]['factory_name'],u'东明东方')
        self.assertEqual(items[2]['price'],u'6300')
        self.assertEqual(items[2]['rise_offset'],u'100')
        self.assertEqual(items[2]['remarks'],u'--')
        self.assertEqual(items[2]['title'],title)
        self.assertEqual(items[2]['trading_dt'],trading_dt)
        
        self.assertEqual(items[17]['area'],u'华北地区')
        self.assertEqual(items[17]['factory_name'],u'沧州炼厂')
        self.assertEqual(items[17]['price'],u'6050')
        self.assertEqual(items[17]['rise_offset'],u'0')
        self.assertEqual(items[17]['remarks'],u'定价')
        self.assertEqual(items[17]['title'],title)
        self.assertEqual(items[17]['trading_dt'],trading_dt)

        