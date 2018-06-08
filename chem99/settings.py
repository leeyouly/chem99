# -*- coding: utf-8 -*-
BOT_NAME = 'chem99'

SPIDER_MODULES = ['chem99.spiders']
NEWSPIDER_MODULE = 'chem99.spiders'

DUPEFILTER_CLASS = 'chem99.dupefilters.ChemDupeFilter'



USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
DOWNLOAD_DELAY=5
SPIDER_MIDDLEWARES = {
   # 'spiderlib.middlewares.IndexPageSaveMiddleware': 300,
}
EXTENSIONS = {
   'spiderlib.extensions.WriteEtlLog': 300,
}
ITEM_PIPELINES = {
   'chem99.pipelines.FactoryPriceSave': 300,
   'chem99.pipelines.FactoryPricePPSave': 300,
   'chem99.pipelines.MarketPricePPSave': 300,
   'chem99.pipelines.PriceSXSYSave': 300,
   'chem99.pipelines.PropeneMonomerSave': 300,
   'chem99.pipelines.MarketReviewBitumenSave': 300,
   'chem99.pipelines.PlasticFilmSave': 300,
   'chem99.pipelines.PlasticFarmFilmSave': 300,
   'chem99.pipelines.RubbThailandSave': 300,
   'chem99.pipelines.RubbUSSThailandSave': 300,
   'chem99.pipelines.t_ec_chem_pvc_start_rateSave': 300,
   'chem99.pipelines.t_bitumen_open_rateSave': 300,
   'chem99.pipelines.t_bitumen_eqpt_checkSave': 300,
   'chem99.pipelines.t_ec_merey_oil_checkSave': 300,
   # 'chem99.pipelines.t_chem99_bithumen_prodSave': 300,

}
LOG_LEVEL = 'INFO'

USERNAME = 'chaoschina'
PASSWORD = 'gyp888'

USERNAME_EC = 'kftz88'
PASSWORD_EC = 'kf2012'

DATABASE = 'oracle://stg:stg123@10.6.0.94:1521/?service_name=db'
