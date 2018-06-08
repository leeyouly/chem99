# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Chem99Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FactoryPrice(scrapy.Item):
    region              = scrapy.Field()
    produce_code        = scrapy.Field()
    produce_name        = scrapy.Field()
    pre_price           = scrapy.Field()
    price               = scrapy.Field()
    rise_offset         = scrapy.Field()
    remarks             = scrapy.Field()
    title               = scrapy.Field()
    trading_dt          = scrapy.Field()
    datetime_stamp      = scrapy.Field()
    
class FactoryPricePP(scrapy.Item):
    area                = scrapy.Field()
    factory_name        = scrapy.Field()
    price               = scrapy.Field()
    rise_offset         = scrapy.Field()
    remarks             = scrapy.Field()
    title               = scrapy.Field()
    trading_dt          = scrapy.Field()
    datetime_stamp      = scrapy.Field()
    
class MarketPricePP(scrapy.Item):
    materials           = scrapy.Field()
    product             = scrapy.Field()
    price               = scrapy.Field()
    rise_offset         = scrapy.Field()
    remarks             = scrapy.Field()
    datadate            = scrapy.Field()
    insert_dt           = scrapy.Field()
    update_dt           = scrapy.Field()
    source              = scrapy.Field()
    
class PriceSXSY(scrapy.Item):
    produce_code        = scrapy.Field()
    price               = scrapy.Field()
    rise_offset         = scrapy.Field()
    remarks             = scrapy.Field()
    title               = scrapy.Field()
    datetime_stamp      = scrapy.Field()
    trading_dt          = scrapy.Field()
    tab_title           = scrapy.Field()
    
class PropeneMonomer(scrapy.Item):
    column_type         = scrapy.Field()
    sd_area             = scrapy.Field()
    hb_area             = scrapy.Field()
    hd_area             = scrapy.Field()
    xb_area             = scrapy.Field()
    db_area             = scrapy.Field()
    hn_area             = scrapy.Field()
    title               = scrapy.Field()
    tab_title           = scrapy.Field()
    datetime_stamp      = scrapy.Field()
    trading_dt          = scrapy.Field()
    
class MarketReviewBitumen(scrapy.Item):
    area                 = scrapy.Field()
    pre_price            = scrapy.Field()
    price                = scrapy.Field()
    change               = scrapy.Field()
    changeratio          = scrapy.Field()
    unit                 = scrapy.Field()
    datadate             = scrapy.Field()
    insert_dt            = scrapy.Field()
    update_dt            = scrapy.Field()
    source               = scrapy.Field()
    
class PlasticFilm(scrapy.Item):
    product              = scrapy.Field()
    spec                 = scrapy.Field()
    price                = scrapy.Field()
    rise_offset          = scrapy.Field()
    than_lastweek        = scrapy.Field()
    than_lastmonth       = scrapy.Field()
    than_lastyear        = scrapy.Field()
    datadate             = scrapy.Field()
    insert_dt            = scrapy.Field()
    update_dt            = scrapy.Field()
    source               = scrapy.Field()
    
class PlasticFarmFilm(scrapy.Item):
    product              = scrapy.Field()
    area                 = scrapy.Field()
    price                = scrapy.Field()
    datadate             = scrapy.Field()
    insert_dt            = scrapy.Field()
    update_dt            = scrapy.Field()
    source               = scrapy.Field()

class RubbThailand(scrapy.Item):
    product              = scrapy.Field()
    price                = scrapy.Field()
    remark               = scrapy.Field()
    datadate             = scrapy.Field()
    insert_dt            = scrapy.Field()
    update_dt            = scrapy.Field()
    source               = scrapy.Field()

class RubbUSSThailand(scrapy.Item):
    product              = scrapy.Field()
    price                = scrapy.Field()
    price_3_5            = scrapy.Field()
    price_5_7            = scrapy.Field()
    price_7_10           = scrapy.Field()
    price_10_15          = scrapy.Field()
    volume               = scrapy.Field()
    volume_3_5           = scrapy.Field()
    volume_5_7           = scrapy.Field()
    volume_7_10          = scrapy.Field()
    volume_10_15         = scrapy.Field()
    remark               = scrapy.Field()
    datadate             = scrapy.Field()
    insert_dt            = scrapy.Field()
    update_dt            = scrapy.Field()
    source               = scrapy.Field()

class t_ec_chem_pvc_start_rateItem(scrapy.Item):
    datadate    = scrapy.Field()
    regions     = scrapy.Field()
    area        = scrapy.Field()
    factory     = scrapy.Field()
    technology  = scrapy.Field()
    pvc_number  = scrapy.Field()
    start_rate  = scrapy.Field()
    update_dt   = scrapy.Field()
    source      = scrapy.Field()


class t_ec_rateofoperation_bitumenItem(scrapy.Item):
    datadate = scrapy.Field()
    area = scrapy.Field()
    current_week_date = scrapy.Field()
    last_week_date = scrapy.Field()
    current_week_value = scrapy.Field()
    last_week_value = scrapy.Field()
    change_situation = scrapy.Field()
    update_dt = scrapy.Field()
    source = scrapy.Field()

class t_ec_check_bitumenItem(scrapy.Item):
    datadate = scrapy.Field()
    area = scrapy.Field()
    factory_name = scrapy.Field()
    affiliation = scrapy.Field()
    product = scrapy.Field()
    status = scrapy.Field()
    product_time = scrapy.Field()
    update_dt = scrapy.Field()
    source = scrapy.Field()

class t_ec_merey_oil_Item(scrapy.Item):
    datadate = scrapy.Field()
    datemonth = scrapy.Field()
    wti_price_avg = scrapy.Field()
    wti_date_range = scrapy.Field()
    discount_value = scrapy.Field()
    tongs_barrels_ratio = scrapy.Field()
    fx_rate = scrapy.Field()
    settle_prc = scrapy.Field()
    update_dt = scrapy.Field()
    source = scrapy.Field()

class t_chem99_bithumen_prod_Item(scrapy.Item):
    datadate = scrapy.Field()
    datemonth = scrapy.Field()
    cls_type = scrapy.Field()
    item_name = scrapy.Field()
    curr_month_value = scrapy.Field()
    pre_month_value = scrapy.Field()
    mom = scrapy.Field()
    pre_year_value = scrapy.Field()
    yoy = scrapy.Field()
    cumu_value_y = scrapy.Field()
    pre_cumu_value_y = scrapy.Field()
    cumu_yoy = scrapy.Field()
    update_dt = scrapy.Field()
    source = scrapy.Field()