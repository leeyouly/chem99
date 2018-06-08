# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from chem99.spiders.sxsy import SxsySpider
import os
import logging

class SxsySpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = SxsySpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/sxsy.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://plas.chem99.com/news/20652890.html'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        title = u'绍兴三圆PP产销动态'
        trading_dt = '2016-03-02 09:12:41'
        tab_title = u'2月18日起出库价'
        
        items = list(items)
        self.assertEqual(len(items), 4)
        
        self.assertEqual(items[0]['produce_code'],u'T30S')
        self.assertEqual(items[0]['price'],u'6250')
        self.assertEqual(items[0]['rise_offset'],u'0')
        self.assertEqual(items[0]['remarks'],u'定价')
        self.assertEqual(items[0]['title'],title)
        self.assertEqual(items[0]['trading_dt'],trading_dt)
        self.assertEqual(items[0]['tab_title'],tab_title)
        self.assertIsNotNone(items[0]['datetime_stamp'])
        
        self.assertEqual(items[1]['produce_code'],u'F280F')
        self.assertEqual(items[1]['price'],u'6280')
        self.assertEqual(items[1]['rise_offset'],u'0')
        self.assertEqual(items[1]['remarks'],u'定价')
        self.assertEqual(items[1]['title'],title)
        self.assertEqual(items[1]['trading_dt'],trading_dt)
        self.assertEqual(items[1]['tab_title'],tab_title)
        self.assertIsNotNone(items[1]['datetime_stamp'])
        
        self.assertEqual(items[2]['produce_code'],u'Y16SY')
        self.assertEqual(items[2]['price'],u'6300')
        self.assertEqual(items[2]['rise_offset'],u'0')
        self.assertEqual(items[2]['remarks'],u'定价')
        self.assertEqual(items[2]['title'],title)
        self.assertEqual(items[2]['trading_dt'],trading_dt)
        self.assertEqual(items[2]['tab_title'],tab_title)
        self.assertIsNotNone(items[2]['datetime_stamp'])
        
        self.assertEqual(items[3]['produce_code'],u'Y26SY')
        self.assertEqual(items[3]['price'],u'6500')
        self.assertEqual(items[3]['rise_offset'],u'0')
        self.assertEqual(items[3]['remarks'],u'定价')
        self.assertEqual(items[3]['title'],title)
        self.assertEqual(items[3]['trading_dt'],trading_dt)
        self.assertEqual(items[3]['tab_title'],tab_title)
        self.assertIsNotNone(items[3]['datetime_stamp'])


        