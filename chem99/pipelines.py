# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from chem99.data import FactoryPriceStorage, FactoryPricePPStorage, \
    PriceSXSYStorage, PromeneMonomerStorage, MarketReviewBitumenStorage, \
    PlasticFilmStorage, PlasticFarmFilmStorage, MarketPricePPStorage, RubbThailandStorage, RubbUSSThailandStorage,t_ec_chem_pvc_start_rateStorage,\
    t_bitumen_eqpt_check_Storage,t_bitumen_open_rate_Storage, t_ec_merey_oil_Storage,t_chem99_bithumen_prod_Storage
from chem99.items import FactoryPrice, FactoryPricePP, \
    PriceSXSY, PropeneMonomer, MarketReviewBitumen, \
    PlasticFilm, PlasticFarmFilm, MarketPricePP, RubbThailand, RubbUSSThailand,t_ec_chem_pvc_start_rateItem, \
    t_ec_check_bitumenItem, t_ec_rateofoperation_bitumenItem, t_ec_merey_oil_Item,t_chem99_bithumen_prod_Item
from scrapy.utils.project import get_project_settings

class Chem99Pipeline(object):
    def process_item(self, item, spider):
        return item

class FactoryPriceSave(object):
    def __init__(self):
        self.storage = FactoryPriceStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, FactoryPrice):
            if not self.storage.exist(item):           
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
        
class FactoryPricePPSave(object):
    def __init__(self):
        self.storage = FactoryPricePPStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, FactoryPricePP):
            self.storage.save(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
    
class MarketPricePPSave(object):
    def __init__(self):
        self.storage = MarketPricePPStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, MarketPricePP):
            if not self.storage.exist(item):           
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
        
class PriceSXSYSave(object):
    def __init__(self):
        self.storage = PriceSXSYStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, PriceSXSY):
            self.storage.save(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
        
class PropeneMonomerSave(object):
    def __init__(self):
        self.storage = PromeneMonomerStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, PropeneMonomer):
            self.storage.save(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
    
class MarketReviewBitumenSave(object):
    def __init__(self):
        self.storage = MarketReviewBitumenStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, MarketReviewBitumen):
            if not self.storage.exist(item):           
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
    
class PlasticFilmSave(object):
    def __init__(self):
        self.storage = PlasticFilmStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, PlasticFilm):
            if not self.storage.exist(item):           
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item
    
class PlasticFarmFilmSave(object):
    def __init__(self):
        self.storage = PlasticFarmFilmStorage(get_project_settings().get('DATABASE'))
    
    def process_item(self, item, spider):
        if isinstance(item, PlasticFarmFilm):
            if not self.storage.exist(item):           
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
            
        return item


class RubbThailandSave(object):
    def __init__(self):
        self.storage = RubbThailandStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, RubbThailand):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')

        return item


class RubbUSSThailandSave(object):
    def __init__(self):
        self.storage = RubbUSSThailandStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, RubbUSSThailand):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')

        return item

class t_ec_chem_pvc_start_rateSave(object):
    def __init__(self):
        self.storage = t_ec_chem_pvc_start_rateStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, t_ec_chem_pvc_start_rateItem):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


class t_bitumen_open_rateSave(object):
    def __init__(self):
        self.storage = t_bitumen_open_rate_Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, t_ec_rateofoperation_bitumenItem):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


class t_bitumen_eqpt_checkSave(object):
    def __init__(self):
        self.storage = t_bitumen_eqpt_check_Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, t_ec_check_bitumenItem):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


class t_ec_merey_oil_checkSave(object):
    def __init__(self):
        self.storage = t_ec_merey_oil_Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, t_ec_merey_oil_Item):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
        return item


class t_chem99_bithumen_prodSave(object):
    def __init__(self):
        self.storage = t_chem99_bithumen_prod_Storage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, t_chem99_bithumen_prod_Item):
            self.storage.save_or_update(item)
            spider.crawler.stats.inc_value('spiderlog/save_count')
        return item