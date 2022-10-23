import pkg_bloomberg.config_module as config_bbg
import datetime as dt
import pandas as pd
from xbbg import blp

class CLS_BBG_data():

    def __init__(self):
        self.bbg_data = pd.DataFrame()

    def init_default_tickers(self, list_tickers, list_PE):
        self.ticker_to_query_list = list_tickers
        self.ticker_to_query_PE_list = list_PE

    def query(self, query_start_dt, query_end_dt, ticker_to_query_list, ticker_to_query_PE_list=[]):
        try:
            price = blp.bdp(tickers='NVDA US Equity', flds='Security_Name')
            connection_bbg = True
        except:
            connection_bbg = False

        if connection_bbg == True:
            if ticker_to_query_list == 'tickers_default':
                ticker_to_query_list = self.ticker_to_query_list
                ticker_to_query_PE_list = self.ticker_to_query_PE_list
            
            #self.bbg_data = blp.bdh(tickers=ticker_to_query_list, flds=['PX_LAST'],start_date=query_start_dt, end_date=query_end_dt,Days='A')
            self.bbg_data = blp.bdh(tickers=ticker_to_query_list, flds=['PX_LAST'],start_date=query_start_dt, end_date=query_end_dt,Fill="B")
            self.bbg_data.columns = [col[0] for col in self.bbg_data.columns]
            #df_PX_LAST.to_csv("bbg_adjusted.csv")

            if len(ticker_to_query_PE_list) > 0:
                #df_trailing_PE = blp.bdh(tickers=ticker_to_query_PE_list, flds=['PE_RATIO'],start_date=query_start_dt, end_date=query_end_dt,Days='A')
                df_trailing_PE = blp.bdh(tickers=ticker_to_query_PE_list, flds=['PE_RATIO'],start_date=query_start_dt, end_date=query_end_dt,Fill="B")
                df_trailing_PE.columns = [(str(col[0])+'_PE_trailing') for col in df_trailing_PE.columns]
                #df_trailing_PE.to_csv("df_trailing_PE.csv")

                #df_forward_PE = blp.bdh(tickers=ticker_to_query_PE_list, flds=['EST_PE_NEXT_YR_AGGTE'],start_date=query_start_dt, end_date=query_end_dt,Days='A')
                df_forward_PE = blp.bdh(tickers=ticker_to_query_PE_list, flds=['EST_PE_NEXT_YR_AGGTE'],start_date=query_start_dt, end_date=query_end_dt,Fill="B")
                df_forward_PE.columns = [(str(col[0])+'_PE_forward') for col in df_forward_PE.columns]
                #df_forward_PE.to_csv("df_forward_PE.csv")

                df_joined = self.bbg_data.join(df_trailing_PE)
                df_joined = df_joined.join(df_forward_PE)
                #df_joined.to_csv("bbg_joined.csv")   
            
                self.bbg_data = df_joined

            self.bbg_data['Dates'] = self.bbg_data.index
            self.bbg_data.set_index('Dates', inplace=True)

            return self.bbg_data
            
    def save_file_local(self):
        try:
            now = dt.datetime.now()
            dt_now = now.strftime("%Y-%m-%d %H-%M-%S")
            self.bbg_data.to_excel(f"{config_bbg.path_output_folder}/query_bbg_{dt_now}.xlsx", sheet_name='query_rates')
            self.bbg_data.to_excel(f"{config_bbg.path_output_folder}/query_bbg.xlsx", sheet_name='query_rates')
        except:
            print("Could not save local file.")

    def save_file_remote(self):
        
        try:
            now = dt.datetime.now()
            dt_now = now.strftime("%Y-%m-%d %H-%M-%S")
            self.bbg_data.to_excel(f"{config_bbg.path_remote_output_folder}/query_bbg_{dt_now}.xlsx", sheet_name='query_rates')
            self.bbg_data.to_excel(f"{config_bbg.path_remote_output_folder}/query_bbg.xlsx", sheet_name='query_rates')
        except:
            print("Couldn't save in remote folder.")
        
        