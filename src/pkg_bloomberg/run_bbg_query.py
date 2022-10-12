import config_module as config
import datetime as dt
import CLS_BBG_data as cls_bbg

query_start_dt = '2011-01-01'
query_end_dt = dt.date.today() 
    
bbg = cls_bbg.CLS_BBG_data()
bbg.init_default_tickers(config.tickers_list,config.PE_list)
bbg.query(query_start_dt, query_end_dt,'tickers_default')
bbg.save_file()

