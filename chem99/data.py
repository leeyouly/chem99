from spiderlib.data import DataStorage
import PyDB


class FactoryPriceStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PLASTIC'
        self.db.set_metadata(self.table_name, [
                               PyDB.StringField("region", is_key=True),
                               PyDB.StringField("produce_code", is_key=True),
                               PyDB.StringField("produce_name", is_key=True),
                               PyDB.StringField("trading_dt", is_key=True),
                               PyDB.StringField("title", is_key=True),
                               PyDB.StringField("pre_price"),
                               PyDB.StringField("price"),
                               PyDB.StringField("rise_offset"),
                               PyDB.StringField("remarks"),
                               PyDB.StringField("datetime_stamp"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
                               
class FactoryPricePPStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PP_FACTORY_PRICE'
        self.db.set_metadata(self.table_name, [
                               PyDB.StringField("area", is_key=True),
                               PyDB.StringField("factory_name", is_key=True),
                               PyDB.StringField("trading_dt", is_key=True),
                               PyDB.StringField("price"),
                               PyDB.StringField("rise_offset"),
                               PyDB.StringField("remarks"),
                               PyDB.StringField("title"),
                               PyDB.StringField("datetime_stamp"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
        
class MarketPricePPStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PP_MARKET_PRICE'
        self.db.set_metadata(self.table_name, [
                               PyDB.StringField("materials", is_key=True),
                               PyDB.StringField("product", is_key=True),
                               PyDB.DateField("datadate", is_key=True),
                               PyDB.StringField("price"),
                               PyDB.StringField("rise_offset"),
                               PyDB.StringField("remarks"),
                               PyDB.DateField("update_dt"),
                               PyDB.StringField("source"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
                               
class PriceSXSYStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PLASTIC_SXSY'
        self.db.set_metadata(self.table_name, [
                               PyDB.StringField("produce_code", is_key=True),
                               PyDB.StringField("title", is_key=True),
                               PyDB.StringField("trading_dt", is_key=True),
                               PyDB.StringField("tab_title", is_key=True),
                               PyDB.StringField("price"),
                               PyDB.StringField("rise_offset"),
                               PyDB.StringField("remarks"),
                               PyDB.StringField("datetime_stamp"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
                               
class PromeneMonomerStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PROPENE_MONOMER'
        self.db.set_metadata(self.table_name, [
                               PyDB.StringField("column_type", is_key=True),
                               PyDB.StringField("title", is_key=True),
                               PyDB.StringField("trading_dt", is_key=True),
                               PyDB.StringField("tab_title", is_key=True),
                               PyDB.StringField("sd_area"),
                               PyDB.StringField("hb_area"),
                               PyDB.StringField("hd_area"),
                               PyDB.StringField("xb_area"),
                               PyDB.StringField("db_area"),
                               PyDB.StringField("hn_area"),
                               PyDB.StringField("datetime_stamp"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
        
class MarketReviewBitumenStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_BM_CHEM_BITUMEN_MARKET'
        self.db.set_metadata(self.table_name, [
                               PyDB.DateField("datadate", is_key=True),
                               PyDB.StringField("source", is_key=True),
                               PyDB.StringField("area", is_key=True),
                               PyDB.StringField("pre_price"),
                               PyDB.StringField("price"),
                               PyDB.StringField("change"),
                               PyDB.StringField("changeratio"),
                               PyDB.StringField("unit"),
                               PyDB.DateField("insert_dt"),
                               PyDB.DateField("update_dt"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
        
class PlasticFilmStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PLASTIC_FILM'
        self.db.set_metadata(self.table_name, [
                               PyDB.DateField("datadate", is_key=True),
                               PyDB.StringField("source", is_key=True),
                               PyDB.StringField("product", is_key=True),
                               PyDB.StringField("spec"),
                               PyDB.StringField("price"),
                               PyDB.StringField("rise_offset"),
                               PyDB.StringField("than_lastweek"),
                               PyDB.StringField("than_lastmonth"),
                               PyDB.StringField("than_lastyear"),
                               PyDB.DateField("insert_dt"),
                               PyDB.DateField("update_dt"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 
        
class PlasticFarmFilmStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_PLASTIC_FARMFILM'
        self.db.set_metadata(self.table_name, [
                               PyDB.DateField("datadate", is_key=True),
                               PyDB.StringField("source", is_key=True),
                               PyDB.StringField("product", is_key=True),
                               PyDB.StringField("area", is_key=True),
                               PyDB.StringField("price"),
                               PyDB.DateField("insert_dt"),
                               PyDB.DateField("update_dt"),
                               ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item) 
        self.db.commit() 

class RubbThailandStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_RUBB_THAILAND'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("product", is_key=True),
            PyDB.StringField("price"),
            PyDB.StringField("remark"),
            PyDB.DateField("datadate", is_key=True),
            PyDB.DateField("insert_dt"),
            PyDB.DateField("update_dt"),
            PyDB.StringField("source"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()

class RubbUSSThailandStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_EC_CHEM_RUBBUSS_THAILAND'
        self.db.set_metadata(self.table_name, [
            PyDB.StringField("product", is_key=True),
            PyDB.StringField("price"),
            PyDB.StringField("price_3_5"),
            PyDB.StringField("price_5_7"),
            PyDB.StringField("price_7_10"),
            PyDB.StringField("price_10_15"),
            PyDB.StringField("volume"),
            PyDB.StringField("volume_3_5"),
            PyDB.StringField("volume_5_7"),
            PyDB.StringField("volume_7_10"),
            PyDB.StringField("volume_10_15"),
            PyDB.StringField("remark"),
            PyDB.DateField("datadate", is_key=True),
            PyDB.DateField("insert_dt"),
            PyDB.DateField("update_dt"),
            PyDB.StringField("source"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class t_ec_chem_pvc_start_rateStorage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 't_ec_chem_pvc_start_rate'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate", is_key=True),
            PyDB.StringField("regions", is_key=True),
            PyDB.StringField("area", is_key=True),
            PyDB.StringField("factory", is_key=True),
            PyDB.StringField("technology", is_key=True),
            PyDB.StringField("pvc_number", is_key=True),
            PyDB.StringField("start_rate"),
            PyDB.DatetimeField("update_dt"),
            PyDB.StringField("source"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class t_bitumen_eqpt_check_Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_BITUMEN_EQPT_CHECK'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate", is_key=True),
            PyDB.StringField("area", is_key=True),
            PyDB.StringField("factory_name", is_key=True),
            PyDB.StringField("affiliation", is_key=True),
            PyDB.StringField("product"),
            PyDB.StringField("status"),
            PyDB.StringField("product_time"),
            PyDB.DatetimeField("update_dt"),
            PyDB.StringField("source"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class t_bitumen_open_rate_Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_BITUMEN_OPEN_RATE'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate", is_key=True),
            PyDB.StringField("area", is_key=True),
            PyDB.DateField("current_week_date", is_key=True),
            PyDB.DateField("last_week_date"),
            PyDB.StringField("current_week_value"),
            PyDB.StringField("last_week_value"),
            PyDB.StringField("change_situation"),
            PyDB.StringField("source"),
            PyDB.DatetimeField("update_dt"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()

class t_ec_merey_oil_Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_CHEM99_MEREY_OIL_F'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate", is_key=True),
            PyDB.StringField("datemonth", is_key=True),
            PyDB.StringField("wti_price_avg"),
            PyDB.StringField("wti_date_range"),
            PyDB.StringField("discount_value"),
            PyDB.StringField("tongs_barrels_ratio"),
            PyDB.StringField("fx_rate"),
            PyDB.StringField("settle_prc"),
            PyDB.StringField("source"),
            PyDB.DatetimeField("update_dt"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()


class t_chem99_bithumen_prod_Storage(DataStorage):
    def __init__(self, db_url):
        self.db = self.build_connection(db_url)
        self.table_name = 'T_CHEM99_BITHUMEN_PROD_F'
        self.db.set_metadata(self.table_name, [
            PyDB.DateField("datadate", is_key=True),
            PyDB.StringField("datemonth", is_key=True),
            PyDB.StringField("cls_type", is_key=True),
            PyDB.StringField("item_name", is_key=True),
            PyDB.StringField("curr_month_value"),
            PyDB.StringField("pre_month_value"),
            PyDB.StringField("mom"),
            PyDB.StringField("pre_year_value"),
            PyDB.StringField("yoy"),
            PyDB.StringField("cumu_value_y"),
            PyDB.StringField("pre_cumu_value_y"),
            PyDB.StringField("cumu_yoy"),
            PyDB.StringField("source"),
            PyDB.DatetimeField("update_dt"),
        ])
    def save_or_update(self, item):
        self.db.save_or_update(self.table_name, item)
        self.db.commit()
