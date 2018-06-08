# -*- coding: utf-8 -*-
import unittest
from scrapy.http import HtmlResponse
from chem99.spiders.propene_monomer import PropeneMonomerSpider
import os
import logging

class FactorypricePplasiSpiderTest(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.target = PropeneMonomerSpider()
        
    def test_parse(self):
        dir = os.path.dirname(os.path.realpath(__file__))
        data_file_path = os.path.join(dir, 'pages/propene_monomer.html')
        f = open(data_file_path)
        html_content = f.read()
        f.close()
        page_url = 'http://plas.chem99.com/news/20563180.html'
        title = u'PP粉料日评：稳中略有整理 实盘谨慎（20160222）'
        tab_title = u'表2　国内各地丙烯单体出厂价格一览'
        trading_dt = '20160222'
        response = HtmlResponse(url=page_url, body=html_content)
        items = self.target.parse_content(response)
        
        items = list(items)
        self.assertEqual(len(items), 2)
        
        self.assertEqual(items[0]['column_type'],u'价格')
        self.assertEqual(items[0]['sd_area'],u'5000-5050')
        self.assertEqual(items[0]['hb_area'],u'4450-4800')
        self.assertEqual(items[0]['hd_area'],u'4700-4800')
        self.assertEqual(items[0]['xb_area'],u'4400-4400')
        self.assertEqual(items[0]['db_area'],u'4450-4450')
        self.assertEqual(items[0]['hn_area'],u'4400-4400')
        self.assertEqual(items[0]['title'],title)
        self.assertEqual(items[0]['tab_title'],tab_title)
        self.assertEqual(items[0]['trading_dt'],trading_dt)
        
        self.assertEqual(items[1]['column_type'],u'涨跌')
        self.assertEqual(items[1]['sd_area'],u'50')
        self.assertEqual(items[1]['hb_area'],u'0')
        self.assertEqual(items[1]['hd_area'],u'0')
        self.assertEqual(items[1]['xb_area'],u'0')
        self.assertEqual(items[1]['db_area'],u'0')
        self.assertEqual(items[1]['hn_area'],u'0')
        self.assertEqual(items[1]['title'],title)
        self.assertEqual(items[1]['tab_title'],tab_title)
        self.assertEqual(items[1]['trading_dt'],trading_dt)

        