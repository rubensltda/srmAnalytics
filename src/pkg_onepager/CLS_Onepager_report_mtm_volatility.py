#import datetime as dt
#import numpy as np
import io
import base64    
from dateutil.relativedelta import relativedelta
import math
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, YearLocator
from matplotlib.ticker import FormatStrFormatter
from email.mime.image import MIMEImage
import datetime as dt

import pkg_onepager.config_module as config_onepager
import pkg_common.utils as ut
from scipy.interpolate import interp1d, splrep, splev


class CLS_Onepager_report_mtm_volatility():
    
    def __init__(self):
        #print("Class report initiated.")
        pass
        
    def generate_html_mtm_volatility(self, cls_df_rates, KRD_FV):
        
        print(f"Generating MTM Volatility")

        # KRDs - FV accounts ##############################################################################
        ###################################################################################################
        KRD_FV_01 = KRD_FV[0]
        KRD_FV_02 = KRD_FV[1]
        KRD_FV_03 = KRD_FV[2]
        KRD_FV_04 = KRD_FV[3]
        KRD_FV_05 = KRD_FV[4]
        KRD_FV_06 = KRD_FV[5]
        KRD_FV_07 = KRD_FV[6]
        KRD_FV_08 = KRD_FV[7]
        KRD_FV_09 = KRD_FV[8]
        KRD_FV_10 = KRD_FV[9]
        KRD_FV_11 = KRD_FV[10]
        KRD_FV_12 = KRD_FV[11]
        KRD_FV_13 = KRD_FV[12]
        KRD_FV_14 = KRD_FV[13]
        KRD_FV_15 = KRD_FV[14]
        KRD_FV_16 = KRD_FV[15]
        KRD_FV_17 = KRD_FV[16]
        KRD_FV_18 = KRD_FV[17]
        KRD_FV_19 = KRD_FV[18]
        KRD_FV_20 = KRD_FV[19]
        KRD_FV_25 = KRD_FV[20]
        KRD_FV_30 = KRD_FV[21]
        Total_KRD_FV = sum(KRD_FV)
        ###################################################################################################

        

        
        # Obtaining and interpolatin SOFR YC ##############################################################
        ###################################################################################################
        curve_query = "SOFR YC"
        curve_spec = config_onepager.ir_curves_dict[curve_query][0]
        tenors_list = []
        tickers_list = []
        rates_list = []
        previous_day_rates_list = []
        previous_quarter_rates_list = []
        
        for tenor in curve_spec:
            tenors_list.append(tenor[0])
            tickers_list.append(tenor[1])
            
            tenor_rate = cls_df_rates.get_mkt_price(tenor[1],config_onepager.today_dt)
            rates_list.append(tenor_rate[1])
            
            tenor_rate_previous_day = cls_df_rates.get_mkt_price(tenor[1],config_onepager.previous_dt)
            previous_day_rates_list.append(tenor_rate_previous_day[1])
            
            tenor_rate_previous_quarter = cls_df_rates.get_mkt_price(tenor[1],config_onepager.last_EOQ_dt)
            previous_quarter_rates_list.append(tenor_rate_previous_quarter[1])
        
        date0 = tenor_rate[0]
        date1 = tenor_rate_previous_day[0]
        date2 = tenor_rate_previous_quarter[0]

        plot_rates = {'Tenors': tenors_list, 'Rates':  rates_list}
        df_rates = pd.DataFrame(plot_rates)
        cubicspline_1 = splrep(df_rates['Tenors'], df_rates['Rates'])

        plot_previous_day_rates = {'Tenors': tenors_list, 'Rates':  previous_day_rates_list}
        df_previous_day_rates = pd.DataFrame(plot_previous_day_rates)
        cubicspline_2 = splrep(df_previous_day_rates['Tenors'], df_previous_day_rates['Rates'])

        plot_previous_quarter_rates = {'Tenors': tenors_list, 'Rates':  previous_quarter_rates_list}
        df_previous_quarter_rates = pd.DataFrame(plot_previous_quarter_rates)
        cubicspline_3 = splrep(df_previous_quarter_rates['Tenors'], df_previous_quarter_rates['Rates'])
        
        sofr_today_01Y = splev(1,cubicspline_1,der=0)
        sofr_today_02Y = splev(2,cubicspline_1,der=0)
        sofr_today_03Y = splev(3,cubicspline_1,der=0)
        sofr_today_04Y = splev(4,cubicspline_1,der=0)
        sofr_today_05Y = splev(5,cubicspline_1,der=0)
        sofr_today_06Y = splev(6,cubicspline_1,der=0)
        sofr_today_07Y = splev(7,cubicspline_1,der=0)
        sofr_today_08Y = splev(8,cubicspline_1,der=0)
        sofr_today_09Y = splev(9,cubicspline_1,der=0)
        sofr_today_10Y = splev(10,cubicspline_1,der=0)
        sofr_today_11Y = splev(11,cubicspline_1,der=0)
        sofr_today_12Y = splev(12,cubicspline_1,der=0)
        sofr_today_13Y = splev(13,cubicspline_1,der=0)
        sofr_today_14Y = splev(14,cubicspline_1,der=0)
        sofr_today_15Y = splev(15,cubicspline_1,der=0)
        sofr_today_16Y = splev(16,cubicspline_1,der=0)
        sofr_today_17Y = splev(17,cubicspline_1,der=0)
        sofr_today_18Y = splev(18,cubicspline_1,der=0)
        sofr_today_19Y = splev(19,cubicspline_1,der=0)
        sofr_today_20Y = splev(20,cubicspline_1,der=0)
        sofr_today_25Y = splev(25,cubicspline_1,der=0)
        sofr_today_30Y = splev(30,cubicspline_1,der=0)
        
        sofr_previous_01Y = splev(1,cubicspline_2,der=0)
        sofr_previous_02Y = splev(2,cubicspline_2,der=0)
        sofr_previous_03Y = splev(3,cubicspline_2,der=0)
        sofr_previous_04Y = splev(4,cubicspline_2,der=0)
        sofr_previous_05Y = splev(5,cubicspline_2,der=0)
        sofr_previous_06Y = splev(6,cubicspline_2,der=0)
        sofr_previous_07Y = splev(7,cubicspline_2,der=0)
        sofr_previous_08Y = splev(8,cubicspline_2,der=0)
        sofr_previous_09Y = splev(9,cubicspline_2,der=0)
        sofr_previous_10Y = splev(10,cubicspline_2,der=0)
        sofr_previous_11Y = splev(11,cubicspline_2,der=0)
        sofr_previous_12Y = splev(12,cubicspline_2,der=0)
        sofr_previous_13Y = splev(13,cubicspline_2,der=0)
        sofr_previous_14Y = splev(14,cubicspline_2,der=0)
        sofr_previous_15Y = splev(15,cubicspline_2,der=0)
        sofr_previous_16Y = splev(16,cubicspline_2,der=0)
        sofr_previous_17Y = splev(17,cubicspline_2,der=0)
        sofr_previous_18Y = splev(18,cubicspline_2,der=0)
        sofr_previous_19Y = splev(19,cubicspline_2,der=0)
        sofr_previous_20Y = splev(20,cubicspline_2,der=0)
        sofr_previous_25Y = splev(25,cubicspline_2,der=0)
        sofr_previous_30Y = splev(30,cubicspline_2,der=0)

        sofr_last_EOQ_01Y = splev(1,cubicspline_3,der=0)
        sofr_last_EOQ_02Y = splev(2,cubicspline_3,der=0)
        sofr_last_EOQ_03Y = splev(3,cubicspline_3,der=0)
        sofr_last_EOQ_04Y = splev(4,cubicspline_3,der=0)
        sofr_last_EOQ_05Y = splev(5,cubicspline_3,der=0)
        sofr_last_EOQ_06Y = splev(6,cubicspline_3,der=0)
        sofr_last_EOQ_07Y = splev(7,cubicspline_3,der=0)
        sofr_last_EOQ_08Y = splev(8,cubicspline_3,der=0)
        sofr_last_EOQ_09Y = splev(9,cubicspline_3,der=0)
        sofr_last_EOQ_10Y = splev(10,cubicspline_3,der=0)
        sofr_last_EOQ_11Y = splev(11,cubicspline_3,der=0)
        sofr_last_EOQ_12Y = splev(12,cubicspline_3,der=0)
        sofr_last_EOQ_13Y = splev(13,cubicspline_3,der=0)
        sofr_last_EOQ_14Y = splev(14,cubicspline_3,der=0)
        sofr_last_EOQ_15Y = splev(15,cubicspline_3,der=0)
        sofr_last_EOQ_16Y = splev(16,cubicspline_3,der=0)
        sofr_last_EOQ_17Y = splev(17,cubicspline_3,der=0)
        sofr_last_EOQ_18Y = splev(18,cubicspline_3,der=0)
        sofr_last_EOQ_19Y = splev(19,cubicspline_3,der=0)
        sofr_last_EOQ_20Y = splev(20,cubicspline_3,der=0)
        sofr_last_EOQ_25Y = splev(25,cubicspline_3,der=0)
        sofr_last_EOQ_30Y = splev(30,cubicspline_3,der=0)

        Daily_FV_MTM_01Y = (sofr_today_01Y-sofr_previous_01Y) * KRD_FV_01 * 100
        Daily_FV_MTM_02Y = (sofr_today_02Y-sofr_previous_02Y) * KRD_FV_02 * 100
        Daily_FV_MTM_03Y = (sofr_today_03Y-sofr_previous_03Y) * KRD_FV_03 * 100
        Daily_FV_MTM_04Y = (sofr_today_04Y-sofr_previous_04Y) * KRD_FV_04 * 100
        Daily_FV_MTM_05Y = (sofr_today_05Y-sofr_previous_05Y) * KRD_FV_05 * 100
        Daily_FV_MTM_06Y = (sofr_today_06Y-sofr_previous_06Y) * KRD_FV_06 * 100
        Daily_FV_MTM_07Y = (sofr_today_07Y-sofr_previous_07Y) * KRD_FV_07 * 100
        Daily_FV_MTM_08Y = (sofr_today_08Y-sofr_previous_08Y) * KRD_FV_08 * 100
        Daily_FV_MTM_09Y = (sofr_today_09Y-sofr_previous_09Y) * KRD_FV_09 * 100
        Daily_FV_MTM_10Y = (sofr_today_10Y-sofr_previous_10Y) * KRD_FV_10 * 100
        Daily_FV_MTM_11Y = (sofr_today_11Y-sofr_previous_11Y) * KRD_FV_11 * 100
        Daily_FV_MTM_12Y = (sofr_today_12Y-sofr_previous_12Y) * KRD_FV_12 * 100
        Daily_FV_MTM_13Y = (sofr_today_13Y-sofr_previous_13Y) * KRD_FV_13 * 100
        Daily_FV_MTM_14Y = (sofr_today_14Y-sofr_previous_14Y) * KRD_FV_14 * 100
        Daily_FV_MTM_15Y = (sofr_today_15Y-sofr_previous_15Y) * KRD_FV_15 * 100
        Daily_FV_MTM_16Y = (sofr_today_16Y-sofr_previous_16Y) * KRD_FV_16 * 100
        Daily_FV_MTM_17Y = (sofr_today_17Y-sofr_previous_17Y) * KRD_FV_17 * 100
        Daily_FV_MTM_18Y = (sofr_today_18Y-sofr_previous_18Y) * KRD_FV_18 * 100
        Daily_FV_MTM_19Y = (sofr_today_19Y-sofr_previous_19Y) * KRD_FV_19 * 100
        Daily_FV_MTM_20Y = (sofr_today_20Y-sofr_previous_20Y) * KRD_FV_20 * 100
        Daily_FV_MTM_25Y = (sofr_today_25Y-sofr_previous_25Y) * KRD_FV_25 * 100
        Daily_FV_MTM_30Y = (sofr_today_30Y-sofr_previous_30Y) * KRD_FV_30 * 100
        Total_Daily_FV_MTM = Daily_FV_MTM_01Y + Daily_FV_MTM_02Y + Daily_FV_MTM_03Y + Daily_FV_MTM_04Y + Daily_FV_MTM_05Y + Daily_FV_MTM_06Y + Daily_FV_MTM_07Y + Daily_FV_MTM_08Y + Daily_FV_MTM_09Y + Daily_FV_MTM_10Y + Daily_FV_MTM_11Y + Daily_FV_MTM_12Y + Daily_FV_MTM_13Y + Daily_FV_MTM_14Y + Daily_FV_MTM_15Y + Daily_FV_MTM_16Y + Daily_FV_MTM_17Y + Daily_FV_MTM_18Y + Daily_FV_MTM_19Y + Daily_FV_MTM_20Y  + Daily_FV_MTM_25Y + Daily_FV_MTM_30Y

        Quarter_FV_MTM_01Y = (sofr_today_01Y-sofr_last_EOQ_01Y) * KRD_FV_01 * 100
        Quarter_FV_MTM_02Y = (sofr_today_02Y-sofr_last_EOQ_02Y) * KRD_FV_02 * 100
        Quarter_FV_MTM_03Y = (sofr_today_03Y-sofr_last_EOQ_03Y) * KRD_FV_03 * 100
        Quarter_FV_MTM_04Y = (sofr_today_04Y-sofr_last_EOQ_04Y) * KRD_FV_04 * 100
        Quarter_FV_MTM_05Y = (sofr_today_05Y-sofr_last_EOQ_05Y) * KRD_FV_05 * 100
        Quarter_FV_MTM_06Y = (sofr_today_06Y-sofr_last_EOQ_06Y) * KRD_FV_06 * 100
        Quarter_FV_MTM_07Y = (sofr_today_07Y-sofr_last_EOQ_07Y) * KRD_FV_07 * 100
        Quarter_FV_MTM_08Y = (sofr_today_08Y-sofr_last_EOQ_08Y) * KRD_FV_08 * 100
        Quarter_FV_MTM_09Y = (sofr_today_09Y-sofr_last_EOQ_09Y) * KRD_FV_09 * 100
        Quarter_FV_MTM_10Y = (sofr_today_10Y-sofr_last_EOQ_10Y) * KRD_FV_10 * 100
        Quarter_FV_MTM_11Y = (sofr_today_11Y-sofr_last_EOQ_11Y) * KRD_FV_11 * 100
        Quarter_FV_MTM_12Y = (sofr_today_12Y-sofr_last_EOQ_12Y) * KRD_FV_12 * 100
        Quarter_FV_MTM_13Y = (sofr_today_13Y-sofr_last_EOQ_13Y) * KRD_FV_13 * 100
        Quarter_FV_MTM_14Y = (sofr_today_14Y-sofr_last_EOQ_14Y) * KRD_FV_14 * 100
        Quarter_FV_MTM_15Y = (sofr_today_15Y-sofr_last_EOQ_15Y) * KRD_FV_15 * 100
        Quarter_FV_MTM_16Y = (sofr_today_16Y-sofr_last_EOQ_16Y) * KRD_FV_16 * 100
        Quarter_FV_MTM_17Y = (sofr_today_17Y-sofr_last_EOQ_17Y) * KRD_FV_17 * 100
        Quarter_FV_MTM_18Y = (sofr_today_18Y-sofr_last_EOQ_18Y) * KRD_FV_18 * 100
        Quarter_FV_MTM_19Y = (sofr_today_19Y-sofr_last_EOQ_19Y) * KRD_FV_19 * 100
        Quarter_FV_MTM_20Y = (sofr_today_20Y-sofr_last_EOQ_20Y) * KRD_FV_20 * 100
        Quarter_FV_MTM_25Y = (sofr_today_25Y-sofr_last_EOQ_25Y) * KRD_FV_25 * 100
        Quarter_FV_MTM_30Y = (sofr_today_30Y-sofr_last_EOQ_30Y) * KRD_FV_30 * 100
        Total_Quarter_FV_MTM = Quarter_FV_MTM_01Y + Quarter_FV_MTM_02Y + Quarter_FV_MTM_03Y + Quarter_FV_MTM_04Y + Quarter_FV_MTM_05Y + Quarter_FV_MTM_06Y + Quarter_FV_MTM_07Y + Quarter_FV_MTM_08Y + Quarter_FV_MTM_09Y + Quarter_FV_MTM_10Y + Quarter_FV_MTM_11Y + Quarter_FV_MTM_12Y + Quarter_FV_MTM_13Y + Quarter_FV_MTM_14Y + Quarter_FV_MTM_15Y + Quarter_FV_MTM_16Y + Quarter_FV_MTM_17Y + Quarter_FV_MTM_18Y + Quarter_FV_MTM_19Y + Quarter_FV_MTM_20Y  + Quarter_FV_MTM_25Y + Quarter_FV_MTM_30Y
        #########################################################################################################
        


        # Creating HTML content
        ###########################################################################               
        filler = (len("As-of date")-3)*"&nbsp;"
        
        content_HTML = f"""
                                <table class='style_table2'>
                                    <tr>
                                        <td class='style_table_header2'>Tenor</td>
                                        <td class='style_table_header2'>KRD</td>
                                        <td class='style_table_header2'>YC ({ut.format_date_compact(config_onepager.today_dt)})</td>
                                        <td class='style_table_header2'>YC ({ut.format_date_compact(config_onepager.previous_dt)})</td>
                                        <td class='style_table_header2'>Daily change</td>
                                        <td class='style_table_header2'>Daily MTM</td>
                                        <td class='style_table_header2'>YC ({ut.format_date_compact(config_onepager.last_EOQ_dt)})</td>
                                        <td class='style_table_header2'>QTD change</td>
                                        <td class='style_table_header2'>QTD MTM</td>
                                    </tr>
                                    <tr class=''>
                                        <td class='style_table_content6'><div title=''>1Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_01)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_01Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_01Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_01Y-sofr_previous_01Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_01Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_01Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_01Y-sofr_last_EOQ_01Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_01Y)}</td>
                                    </tr>
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>2Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_02)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_02Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_02Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_02Y-sofr_previous_02Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_02Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_02Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_02Y-sofr_last_EOQ_02Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_02Y)}</td>                                    
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>3Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_03)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_03Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_03Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_03Y-sofr_previous_03Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_03Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_03Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_03Y-sofr_last_EOQ_03Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_03Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>4Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_04)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_04Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_04Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_04Y-sofr_previous_04Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_04Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_04Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_04Y-sofr_last_EOQ_04Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_04Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>5Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_05)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_05Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_05Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_05Y-sofr_previous_05Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_05Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_05Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_05Y-sofr_last_EOQ_05Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_05Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>6Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_06)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_06Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_06Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_06Y-sofr_previous_06Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_06Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_06Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_06Y-sofr_last_EOQ_06Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_06Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>7Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_07)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_07Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_07Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_07Y-sofr_previous_07Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_07Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_07Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_07Y-sofr_last_EOQ_07Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_07Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>8Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_08)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_08Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_08Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_08Y-sofr_previous_08Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_08Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_08Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_08Y-sofr_last_EOQ_08Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_08Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>9Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_09)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_09Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_09Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_09Y-sofr_previous_09Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_09Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_09Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_09Y-sofr_last_EOQ_09Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_09Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>10Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_10)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_10Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_10Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_10Y-sofr_previous_10Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_10Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_10Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_10Y-sofr_last_EOQ_10Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_10Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>11Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_11)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_11Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_11Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_11Y-sofr_previous_11Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_11Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_11Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_11Y-sofr_last_EOQ_11Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_11Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>12Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_12)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_12Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_12Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_12Y-sofr_previous_12Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_12Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_12Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_12Y-sofr_last_EOQ_12Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_12Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>13Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_13)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_13Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_13Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_13Y-sofr_previous_13Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_13Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_13Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_13Y-sofr_last_EOQ_13Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_13Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>14Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_14)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_14Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_14Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_14Y-sofr_previous_14Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_14Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_14Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_14Y-sofr_last_EOQ_14Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_14Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>15Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_15)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_15Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_15Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_15Y-sofr_previous_15Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_15Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_15Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_15Y-sofr_last_EOQ_15Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_15Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>16Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_16)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_16Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_16Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_16Y-sofr_previous_16Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_16Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_16Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_16Y-sofr_last_EOQ_16Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_16Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>17Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_17)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_17Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_17Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_17Y-sofr_previous_17Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_17Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_17Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_17Y-sofr_last_EOQ_17Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_17Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>18Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_18)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_18Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_18Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_18Y-sofr_previous_18Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_18Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_18Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_18Y-sofr_last_EOQ_18Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_18Y)}</td>
                                    </tr>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>19Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_19)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_19Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_19Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_19Y-sofr_previous_19Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_19Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_19Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_19Y-sofr_last_EOQ_19Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_19Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>20Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_20)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_20Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_20Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_20Y-sofr_previous_20Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_20Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_20Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_20Y-sofr_last_EOQ_20Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_20Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''>25Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_25)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_25Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_25Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_25Y-sofr_previous_25Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_25Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_25Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_25Y-sofr_last_EOQ_25Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_25Y)}</td>
                                    </tr> 
                                    <tr class='style_table_row'>
					                    <td class='style_table_content6'><div title=''>30Y</div></td>
                                        <td class='style_table_content6'>{ut.format_notional(KRD_FV_30)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_today_30Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_previous_30Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_30Y-sofr_previous_30Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Daily_FV_MTM_30Y)}</td>
                                        <td class='style_table_content6'>{ut.format_quote(sofr_last_EOQ_30Y,'rate')}</td>
                                        <td class='style_table_content6'>{ut.format_change_html(sofr_today_30Y-sofr_last_EOQ_30Y)}</td>
                                        <td class='style_table_content6'>{ut.format_notional(Quarter_FV_MTM_30Y)}</td>
                                    </tr>
                                    <tr class=''>
					                    <td class='style_table_content6'><div title=''><b>Total</b></div></td>
                                        <td class='style_table_content6'><b>{ut.format_notional(Total_KRD_FV)}</b></td>
                                        <td class='style_table_content6'></td>
                                        <td class='style_table_content6'></td>
                                        <td class='style_table_content6'></td>
                                        <td class='style_table_content6'><b>{ut.format_notional(Total_Daily_FV_MTM)}</b></td>
                                        <td class='style_table_content6'></td>
                                        <td class='style_table_content6'></td>
                                        <td class='style_table_content6'><b>{ut.format_notional(Total_Quarter_FV_MTM)}</b></td>
                                    </tr> 
                                </table>
                                <table>
                                    <tr>
                                        <td class='style_table_content7'>(*) <i> KRD represents the sensitivity for +1bp. </i></td>
                                    </tr>
                                    <tr>
                                        <td class='style_table_content7'>(*) <i> KRD from last end of quarter. Does not include intra-quarter transactions.</i></td>                                        
                                    </tr>
                                </table>
                                <br>
        """

        
        




        #content_HTML = content_HTML.replace("                            ","")
        return content_HTML
    


    