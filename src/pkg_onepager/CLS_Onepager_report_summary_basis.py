#import datetime as dt
#import numpy as np
import io
import base64    
from dateutil.relativedelta import relativedelta
import math

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, YearLocator
from matplotlib.ticker import FormatStrFormatter
from email.mime.image import MIMEImage
import datetime as dt

import config_module as config
import pkg_common.utils as ut



class CLS_Onepager_report_summary_basis():
    
    def __init__(self):
        #print("Class report initiated.")
        pass
        
    def generate_html_summary_basis(self, cls_df_rates):
        

        print(f"Generating Basis Summary")

        # Market Rates  ############################################################################
        ############################################################################################
        rate_index_1 = "Fed Funds"
        ticker_query_1 = config.assets_dict[rate_index_1][0]
        today_px_1 = cls_df_rates.get_mkt_price(ticker_query_1,config.today_dt)
        previous_px_1 = cls_df_rates.get_mkt_price(ticker_query_1,config.previous_dt)
        daily_change_px_1 = ut.calculate_change(today_px_1[1] , previous_px_1[1])
        ############################################################################################
        rate_index_2 = "SOFR O/N"
        ticker_query_2 = config.assets_dict[rate_index_2][0]
        today_px_2 = cls_df_rates.get_mkt_price(ticker_query_2,config.today_dt)
        previous_px_2 = cls_df_rates.get_mkt_price(ticker_query_2,config.previous_dt)
        daily_change_px_2 = ut.calculate_change(today_px_2[1] , previous_px_2[1])
        ############################################################################################
        rate_index_3 = "Libor 3M"
        ticker_query_3 = config.assets_dict[rate_index_3][0]
        today_px_3 = cls_df_rates.get_mkt_price(ticker_query_3,config.today_dt)
        previous_px_3 = cls_df_rates.get_mkt_price(ticker_query_3,config.previous_dt)
        daily_change_px_3 = ut.calculate_change(today_px_3[1] , previous_px_3[1])
        ############################################################################################
        rate_index_4 = "Libor 6M"
        ticker_query_4 = config.assets_dict[rate_index_4][0]
        today_px_4 = cls_df_rates.get_mkt_price(ticker_query_4,config.today_dt)
        previous_px_4 = cls_df_rates.get_mkt_price(ticker_query_4,config.previous_dt)
        daily_change_px_4 = ut.calculate_change(today_px_4[1] , previous_px_4[1])
        ############################################################################################
        rate_index_5 = "SOFR 90d comp."
        ticker_query_5 = config.assets_dict[rate_index_5][0]
        today_px_5 = cls_df_rates.get_mkt_price(ticker_query_5,config.today_dt)
        previous_px_5 = cls_df_rates.get_mkt_price(ticker_query_5,config.previous_dt)
        daily_change_px_5 = ut.calculate_change(today_px_5[1] , previous_px_5[1])
        ############################################################################################
        rate_index_6 = "SOFR 180d comp."
        ticker_query_6 = config.assets_dict[rate_index_6][0]
        today_px_6 = cls_df_rates.get_mkt_price(ticker_query_6,config.today_dt)
        previous_px_6 = cls_df_rates.get_mkt_price(ticker_query_6,config.previous_dt)
        daily_change_px_6 = ut.calculate_change(today_px_6[1] , previous_px_6[1])
        ############################################################################################
        rate_index_7 = "SOFR Term 3M"
        ticker_query_7 = config.assets_dict[rate_index_7][0]
        today_px_7 = cls_df_rates.get_mkt_price(ticker_query_7,config.today_dt)
        previous_px_7 = cls_df_rates.get_mkt_price(ticker_query_7,config.previous_dt)
        daily_change_px_7 = ut.calculate_change(today_px_7[1] , previous_px_7[1])
        ############################################################################################
        rate_index_8 = "SOFR Term 6M"
        ticker_query_8 = config.assets_dict[rate_index_8][0]
        today_px_8 = cls_df_rates.get_mkt_price(ticker_query_8,config.today_dt)
        previous_px_8 = cls_df_rates.get_mkt_price(ticker_query_8,config.previous_dt)
        daily_change_px_8 = ut.calculate_change(today_px_8[1] , previous_px_8[1])
       ############################################################################################
        rate_index_9 = "BSBY3M Index"
        ticker_query_9 = config.assets_dict[rate_index_9][0]
        today_px_9 = cls_df_rates.get_mkt_price(ticker_query_9,config.today_dt)
        previous_px_9 = cls_df_rates.get_mkt_price(ticker_query_9,config.previous_dt)
        daily_change_px_9 = ut.calculate_change(today_px_9[1] , previous_px_9[1])
        ############################################################################################
        rate_index_10 = "Libor 3M | -90d shift"
        ticker_query_10 = config.assets_dict["Libor 3M"][0]
        today_px_10 = cls_df_rates.get_mkt_price(ticker_query_10,config.last_3m_dt)
        ############################################################################################
        rate_index_11 = "SOFR Term 3M | -90d shift"
        ticker_query_11 = config.assets_dict["SOFR Term 3M"][0]
        today_px_11 = cls_df_rates.get_mkt_price(ticker_query_11,config.last_3m_dt)
        ############################################################################################
        rate_index_12 = "SOFR 90d | -10d shift"
        ticker_query_12 = config.assets_dict["SOFR 90d comp."][0]
        today_px_12 = cls_df_rates.get_mkt_price(ticker_query_12,config.today_dt + relativedelta(days=-10))


        # JAJO #####################################################################################
        ############################################################################################
        jajo_dt_1 = ut.find_previous_JAJO(config.today_dt)
        jajo_dt_2 = jajo_dt_1 + relativedelta(months=-3)
        jajo_dt_3 = jajo_dt_1 + relativedelta(months=-6)
        jajo_dt_4 = jajo_dt_1 + relativedelta(months=-9)
        jajo_dt_5 = jajo_dt_1 + relativedelta(months=-12)
        jajo_dt_6 = jajo_dt_1 + relativedelta(months=-15)
        jajo_dt_7 = jajo_dt_1 + relativedelta(months=-18)
        jajo_dt_8 = jajo_dt_1 + relativedelta(months=-21)
        
        
        libor3m_ticker = config.assets_dict["Libor 3M"][0]
        
        libo3M_jajo1_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_1)
        libo3M_jajo2_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_2)
        libo3M_jajo3_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_3)
        libo3M_jajo4_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_4)
        libo3M_jajo5_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_5)
        libo3M_jajo6_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_6)
        libo3M_jajo7_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_7)
        libo3M_jajo8_px = cls_df_rates.get_mkt_price(libor3m_ticker,jajo_dt_8)
        
        sofr90d_ticker = config.assets_dict["SOFR 90d comp."][0]
        if ((jajo_dt_1 + relativedelta(months=+3)) > config.today_dt):
            sofr90d_jajo1_90dfwd_px = (jajo_dt_1 + relativedelta(months=+3),'*')
            sofr90d_jajo1_diff = '*'
        else:
            sofr90d_jajo1_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_1 + relativedelta(months=+3))
            sofr90d_jajo1_diff = math.trunc(libo3M_jajo1_px[1]*100)/100 - math.trunc(sofr90d_jajo1_90dfwd_px[1]*100)/100

        sofr90d_jajo2_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_2 + relativedelta(months=+3))
        sofr90d_jajo3_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_3 + relativedelta(months=+3))
        sofr90d_jajo4_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_4 + relativedelta(months=+3))
        sofr90d_jajo5_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_5 + relativedelta(months=+3))
        sofr90d_jajo6_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_6 + relativedelta(months=+3))
        sofr90d_jajo7_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_7 + relativedelta(months=+3))
        sofr90d_jajo8_90dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_8 + relativedelta(months=+3))
        
        sofr90d_jajo2_diff = round(libo3M_jajo2_px[1],2) - round(sofr90d_jajo2_90dfwd_px[1],2)
        sofr90d_jajo3_diff = round(libo3M_jajo3_px[1],2) - round(sofr90d_jajo3_90dfwd_px[1],2)
        sofr90d_jajo4_diff = round(libo3M_jajo4_px[1],2) - round(sofr90d_jajo4_90dfwd_px[1],2)
        sofr90d_jajo5_diff = round(libo3M_jajo5_px[1],2) - round(sofr90d_jajo5_90dfwd_px[1],2)
        sofr90d_jajo6_diff = round(libo3M_jajo6_px[1],2) - round(sofr90d_jajo6_90dfwd_px[1],2)
        sofr90d_jajo7_diff = round(libo3M_jajo7_px[1],2) - round(sofr90d_jajo7_90dfwd_px[1],2)
        sofr90d_jajo8_diff = round(libo3M_jajo8_px[1],2) - round(sofr90d_jajo8_90dfwd_px[1],2)


        
        # not used anymore (sofr -10d shift)
        # sofr90d_ticker = config.assets_dict["SOFR 90d comp."][0]
        # if ((jajo_dt_1 + relativedelta(months=+3)+ relativedelta(days=-10)) > config.today_dt):
        #     sofr90d_jajo1_80dfwd_px = (jajo_dt_1 + relativedelta(months=+3)+ relativedelta(days=-10),'*')
        # else:
        #     sofr90d_jajo1_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_1 + relativedelta(months=+3)+ relativedelta(days=-10))        
        # sofr90d_jajo2_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_2 + relativedelta(months=+3) + relativedelta(days=-10))
        # sofr90d_jajo3_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_3 + relativedelta(months=+3) + relativedelta(days=-10))
        # sofr90d_jajo4_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_4 + relativedelta(months=+3) + relativedelta(days=-10))
        # sofr90d_jajo5_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_5 + relativedelta(months=+3) + relativedelta(days=-10))
        # sofr90d_jajo6_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_6 + relativedelta(months=+3) + relativedelta(days=-10))
        # sofr90d_jajo7_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_7 + relativedelta(months=+3) + relativedelta(days=-10))
        # sofr90d_jajo8_80dfwd_px = cls_df_rates.get_mkt_price(sofr90d_ticker,jajo_dt_8 + relativedelta(months=+3) + relativedelta(days=-10))
        
        
        
        #sofr90d_jajo1_px = cls_df_rates.get_mkt_price(sofr90d_ticker,config.today_dt)
        ############################################################################################


        # Creating HTML content
        ###########################################################################               
        filler = (len("As-of date")-3)*"&nbsp;"
        
        content_HTML = f"""
                                <table>
                                    <tr>
                                        <td class='style_title' title=''> Market's close </td>
                                    </tr>
                                </table>
                                <hr> <!--  -->
                                <table class='style_table'>
                                    <tr>
                                        <td  class='style_content_left'>
                                            <table class='style_table2'>
                                                <tr>
                                                    <td class='style_table_header'>Index</td>
                                                    <td class='style_table_header2' colspan='3'>Rate / Change</td>
                                                    <td class='style_table_header2' colspan='3'>As-of date{filler}</td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_1[0])} {today_px_1[1]} | {ut.format_date_compact(previous_px_1[0])} {previous_px_1[1]}'>{rate_index_1}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_1[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_1,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_1[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_2[0])} {today_px_2[1]} | {ut.format_date_compact(previous_px_2[0])} {previous_px_2[1]}'>{rate_index_2}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_2[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_2,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_2[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_3[0])} {today_px_3[1]} | {ut.format_date_compact(previous_px_3[0])} {previous_px_3[1]}'>{rate_index_3}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_3[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_3,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_3[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_4[0])} {today_px_4[1]} | {ut.format_date_compact(previous_px_4[0])} {previous_px_4[1]}'>{rate_index_4}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_4[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_4,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_4[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_5[0])} {today_px_5[1]} | {ut.format_date_compact(previous_px_5[0])} {previous_px_5[1]}'>{rate_index_5}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_5[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_5,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_5[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_6[0])} {today_px_6[1]} | {ut.format_date_compact(previous_px_6[0])} {previous_px_6[1]}'>{rate_index_6}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_6[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_6,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_6[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_7[0])} {today_px_7[1]} | {ut.format_date_compact(previous_px_7[0])} {previous_px_7[1]}'>{rate_index_7}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_7[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_7,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_7[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_8[0])} {today_px_8[1]} | {ut.format_date_compact(previous_px_8[0])} {previous_px_8[1]}'>{rate_index_8}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_8[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_8,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_8[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_9[0])} {today_px_9[1]} | {ut.format_date_compact(previous_px_9[0])} {previous_px_9[1]}'>{rate_index_9}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_9[1],'rate')}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(daily_change_px_9,'rate')}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_9[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_10[0])} {today_px_10[1]}'>{rate_index_10}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_10[1],'rate')}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_10[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_11[0])} {today_px_11[1]}'>{rate_index_11}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_11[1],'rate')}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_11[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date_compact(today_px_12[0])} {today_px_12[1]}'>{rate_index_12}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_12[1],'rate')}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_date_compact(today_px_12[0])}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                            </table>
                                            <br>
                                        </td>
                                        <td class='style_column_space'></td>
                                        <td class='style_content_right'>
                                            <table align='right'>
                                                <tr>
                                                    <td>
                                                        <table class='style_table2'>
                                                            <tr>
                                                                <td class='style_table_header5'>JAJO Reset</td>
                                                                <td class='style_table_header5'>LIBOR3M</td>
                                                                <td class='style_table_header5'>SOFR90d Arrears</td>
                                                                <td class='style_table_header5'>Difference</td>
                                                                
                                                            </tr>
                                                            <tr class=''>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_1)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo1_px[0])}'>{ut.format_quote(libo3M_jajo1_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo1_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo1_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo1_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class='style_table_row'>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_2)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo2_px[0])}'>{ut.format_quote(libo3M_jajo2_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo2_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo2_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo2_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class=''>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_3)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo3_px[0])}'>{ut.format_quote(libo3M_jajo3_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo3_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo3_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo3_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class='style_table_row'>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_4)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo4_px[0])}'>{ut.format_quote(libo3M_jajo4_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo4_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo4_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo4_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class=''>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_5)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo5_px[0])}'>{ut.format_quote(libo3M_jajo5_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo5_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo5_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo5_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class='style_table_row'>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_6)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo6_px[0])}'>{ut.format_quote(libo3M_jajo6_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo6_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo6_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo6_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class=''>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_7)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo7_px[0])}'>{ut.format_quote(libo3M_jajo7_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo7_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo7_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo7_diff)} </div></td>
                                                                
                                                            </tr>
                                                            <tr class='style_table_row'>
                                                                <td class='style_table_content6'>{ut.format_date_short(jajo_dt_8)}</td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(libo3M_jajo8_px[0])}'>{ut.format_quote(libo3M_jajo8_px[1])}</div> </td>
                                                                <td class='style_table_content6'><div title='{ut.format_date(sofr90d_jajo8_90dfwd_px[0])}'>{ut.format_quote(sofr90d_jajo8_90dfwd_px[1])} </div></td>
                                                                <td class='style_table_content6'><div title=''>{ut.format_quote(sofr90d_jajo8_diff)} </div></td>
                                                                
                                                            </tr>
                                                        </table>
                                                    </td>
                                                    <td>
                                                        <table>
                                                            <tr>
                                                                <td>
                                                                    &nbsp;&nbsp;&nbsp;&nbsp;
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                                    
                                            <br>
                                        
                                        </td>
                                    </tr>
                                </table>
                                <br>
        """

        #content_HTML = content_HTML.replace("                            ","")
        return content_HTML
    


    