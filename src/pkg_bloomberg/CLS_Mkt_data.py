import pkg_bloomberg.config_module as config
from pkg_bloomberg import CLS_BBG_data 
import pandas as pd
import datetime as dt
import numpy as np
from dateutil.relativedelta import relativedelta


class CLS_Mkt_data():

    def __init__(self):
        self.pd_mkt_data = pd.DataFrame()
    
    
    def load_prices(self):
        #old bloomberg file with formula
        #self.pd_mkt_data = pd.read_excel(config.path_mkt_file, sheet_name='query_rates', header=3)
        #self.pd_mkt_data = self.pd_mkt_data.set_index('Dates')
        self.pd_mkt_data = pd.read_excel(config.path_mkt_file, sheet_name='query_rates', header=0)

    
    def shift_series(self, rate_index,rate_index_shifted,lag_months):
        first_date = min(self.pd_mkt_data['Dates'])
        
        self.pd_mkt_data[rate_index_shifted] = ''
        
        for index, row in self.pd_mkt_data.iterrows():
            shift_count = 0
            found_value = False

            shifted_date = row['Dates'] + relativedelta(months=lag_months)
            shifted_date = shifted_date + relativedelta(days=+1)
            while(found_value == False and shifted_date > first_date and shift_count < 10):
                shifted_date = shifted_date + relativedelta(days=-1)
                shift_count += 1
                shifted_value = self.pd_mkt_data[self.pd_mkt_data['Dates']==shifted_date]
                if (len(shifted_value[rate_index]) != 0):
                    if(~np.isnan(shifted_value[rate_index].iloc[0])):
                        found_value = True
                        self.pd_mkt_data.loc[index, rate_index_shifted] = shifted_value[rate_index].iloc[0]
        return True
    
    
    def calculate_spreads(self):
        self.pd_mkt_data['Spread_T2_10'] = (self.pd_mkt_data['GT10 Govt'] - self.pd_mkt_data['GT2 Govt'])
    
    
    def shift_and_calculate_basis_spreads(self):
        # format basis swap format
        self.pd_mkt_data['USSRVL1 Curncy decimals'] = (self.pd_mkt_data['USSRVL1 Curncy']/100)

        # create column with shifted series
        ########### Old #######################
        #########################################################################################################
        # self.pd_mkt_data['US0003M Index_90d_back'] = self.pd_mkt_data['US0003M Index'].shift(65)
        #self.pd_mkt_data['US0006M Index_180d_back'] = self.pd_mkt_data['US0006M Index'].shift(130)
        #self.pd_mkt_data['TSFR3M Index_90d_back'] = self.pd_mkt_data['TSFR3M Index'].shift(65)
        #########################################################################################################
        #self.pd_mkt_data['US0003M Index_90d_back'] = ''
        self.shift_series('US0003M Index', 'US0003M Index_90d_back', -3)
        self.shift_series('US0006M Index', 'US0006M Index_180d_back', -6)
        self.shift_series('TSFR3M Index',  'TSFR3M Index_90d_back', -3)
        self.shift_series('TSFR6M Index',  'TSFR6M Index_180d_back', -6)
        #########################################################################################################
        
        # calculate spreads
        self.pd_mkt_data['Spread_Libor3M_Sofr3MTerm'] = (self.pd_mkt_data['US0003M Index'] - self.pd_mkt_data['TSFR3M Index'])
        self.pd_mkt_data['Spread_Libor3Mshifted_SOFR90dcomp'] = (self.pd_mkt_data['US0003M Index_90d_back'] - self.pd_mkt_data['SOFR90A Index'])
        self.pd_mkt_data['Spread_Libor6Mshifted_SOFR180dcomp'] = (self.pd_mkt_data['US0006M Index_180d_back'] - self.pd_mkt_data['SOFR180A Index'])
        self.pd_mkt_data['Spread_SOFRT3Mshifted_SOFR90dcomp'] = (self.pd_mkt_data['TSFR3M Index_90d_back'] - self.pd_mkt_data['SOFR90A Index'])
        self.pd_mkt_data['Spread_SOFRT6Mshifted_SOFR180dcomp'] = (self.pd_mkt_data['TSFR6M Index_180d_back'] - self.pd_mkt_data['SOFR180A Index'])
        
        
    def export_data_csv(self):
        #self.pd_mkt_data.to_csv("mkt_data.csv", index=False)
        now = dt.datetime.now()
        dt_now = now.strftime("%Y-%m-%d %H-%M-%S")
        self.pd_mkt_data.fillna(method="bfill", inplace=True)
        self.pd_mkt_data.to_csv(f"{config.path_output_folder}/mkt_data_{dt_now}.csv", index=False)
       
        
    def get_mkt_price(self, ticker_query, date_query):
        
        price = ''
        try:
            date_query_str = date_query.strftime("%Y-%m-%d")
            df_data_col = self.pd_mkt_data[['Dates', ticker_query]]
            df_result = df_data_col[df_data_col['Dates'] == date_query_str]

            if df_result.empty or np.isnan(df_result.iloc[0,1]):
                while df_result.empty or np.isnan(df_result.iloc[0,1]) :
                    date_query = date_query - dt.timedelta(days=1)
                    date_query_str = date_query.strftime("%Y-%m-%d")
                    df_result = df_data_col[df_data_col['Dates'] == date_query_str]
            
            #price = df_result.iloc[0,0],round(df_result.iloc[0,1],2)
            price = [df_result.iloc[0,0],df_result.iloc[0,1]]
        except:
            price = [date_query_str,'-']

        # return Price and Date of the price (date needed because of the shiffting)
        return (price)
        
        
    def get_mkt_price_period(self, tickers_query, date_init_query, date_end_query):
        date_init_query_str = date_init_query.strftime("%Y-%m-%d")
        date_end_query_str = date_end_query.strftime("%Y-%m-%d")

        query_cols = ['Dates']
        if isinstance(tickers_query, str):
            query_cols.append(tickers_query)
        elif isinstance(tickers_query, list): 
            query_cols = query_cols + tickers_query
        else:
            pass
        
        
        df_data_col = self.pd_mkt_data[query_cols]
        df_result = df_data_col[(df_data_col.Dates >= date_init_query_str) & (df_data_col.Dates <= date_end_query_str)]


        df_result = df_result.set_index('Dates')

        return df_result
    
    def get_last_available_date(self):
        
        #x = self.get_mkt_price('FEDL01 Index',dt.date.today())
        y = self.get_mkt_price('SPX Index',dt.date.today())
        w = self.get_mkt_price('USOSFR5 BGN Curncy',dt.date.today())
        z = self.get_mkt_price('USSWAP5 Curncy',dt.date.today())
        
        #last_available_date = min(x[0],y[0],w[0],z[0])
        last_available_date = min(y[0],w[0],z[0])
        last_available_date = last_available_date.date()
        
        return last_available_date