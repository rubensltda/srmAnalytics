import datetime as dt
import pkg_bloomberg.config_module as config_bbg
from pkg_bloomberg.CLS_BBG_data import CLS_BBG_data


def run_bbg_query():
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Starting obtaining BBG...")
    
    
    query_start_dt = '2011-01-01'
    query_end_dt = dt.date.today() 
        
    bbg = CLS_BBG_data()
    bbg.init_default_tickers(config_bbg.tickers_list,config_bbg.PE_list)
    bbg.query(query_start_dt, query_end_dt,'tickers_default')
    bbg.save_file_local()
    bbg.save_file_remote()
    
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Finished obtaining BBG.")

########################################################################################################################################################################
########################################################################################################################################################################
if __name__ == "__main__":
    run_bbg_query()
    