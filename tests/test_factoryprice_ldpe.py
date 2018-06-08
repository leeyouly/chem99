# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from chem99.spiders.factoryprice_ldpe import FactorypriceLdpeSpider
import os
import logging

class GlobalmarketNaphthaSpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = FactorypriceLdpeSpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/factoryprice_ldpe.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://plas.chem99.com/news/20663022.html'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        items = list(items)
        self.assertEqual(len(items), 91)
        
        self.assertEqual(items[0]['region'],u'中石化华北')
        self.assertEqual(items[0]['produce_code'],u'1C7A')
        self.assertEqual(items[0]['produce_name'],u'燕山石化')
        self.assertEqual(items[0]['pre_price'],u'11000')
        self.assertEqual(items[0]['price'],u'11100')
        self.assertEqual(items[0]['rise_offset'],u'100')
        self.assertEqual(items[0]['remarks'],u'定价')
        self.assertEqual(items[0]['title'],u'国内LDPE出厂价格汇总（20160302）')
        self.assertEqual(items[0]['trading_dt'],u'20160302')
        
        self.assertEqual(items[1]['region'],u'中石化华北')
        self.assertEqual(items[1]['produce_code'],u'1C7A-1（H188）')
        self.assertEqual(items[1]['produce_name'],u'燕山石化')
        self.assertEqual(items[1]['pre_price'],u'11050')
        self.assertEqual(items[1]['price'],u'11150')
        self.assertEqual(items[1]['rise_offset'],u'100')
        self.assertEqual(items[1]['remarks'],u'定价')
        self.assertEqual(items[1]['title'],u'国内LDPE出厂价格汇总（20160302）')
        self.assertEqual(items[1]['trading_dt'],u'20160302')
        
        self.assertEqual(items[2]['region'],u'中石化华北')
        self.assertEqual(items[2]['produce_code'],u'LD150')
        self.assertEqual(items[2]['produce_name'],u'燕山石化')
        self.assertEqual(items[2]['pre_price'],u'--')
        self.assertEqual(items[2]['price'],u'--')
        self.assertEqual(items[2]['rise_offset'],u'--')
        self.assertEqual(items[2]['remarks'],u'--')
        self.assertEqual(items[2]['title'],u'国内LDPE出厂价格汇总（20160302）')
        self.assertEqual(items[2]['trading_dt'],u'20160302')

        