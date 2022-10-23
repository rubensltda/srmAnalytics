#import datetime as dt
#import numpy as np
import io
import base64
from tokenize import group    
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, YearLocator
from matplotlib.ticker import FormatStrFormatter
from email.mime.image import MIMEImage

import pkg_onepager.config_module as config_onepager
import pkg_common.utils as ut

class CLS_Onepager_report_group():
    
    def __init__(self):
        #print("Class report initiated.")
        pass
        
    def generate_html_group_summary(self, cls_df_rates, group_query, long_period=False, showtable=[0,1]):
                
        show_table_index1 = showtable[0]
        asset_show_1 = config_onepager.groups_dict[group_query][show_table_index1]
        ticker_show_1 = config_onepager.assets_dict[asset_show_1][0]
        ticker_type_1 =  config_onepager.assets_dict[asset_show_1][1]
        ticker_quote_type = ticker_type_1
        
        show_table_index2 = showtable[1]
        asset_show_2 = config_onepager.groups_dict[group_query][show_table_index2]
        ticker_show_2 = config_onepager.assets_dict[asset_show_2][0]
        ticker_type_2 =  config_onepager.assets_dict[asset_show_2][1]
        
        #print(f"{asset_show_1} | {asset_show_2}")
        print(f"Generating group report: {ticker_show_1} | {ticker_show_2}, long_period={long_period}")
        
        #print(df_historic_group)
        ##############################################################
        assets_list = config_onepager.groups_dict[group_query]
        tickers_list = []
        rate_type_list = []
        colors_list = []
        linestyle_list = []
        for asset in assets_list:
            #print(f"{asset} - {config_onepager.assets_dict[asset][0]}")
            tickers_list.append(config_onepager.assets_dict[asset][0])
            rate_type_list.append(config_onepager.assets_dict[asset][1])
            colors_list.append(config_onepager.assets_dict[asset][2])
            linestyle_list.append(config_onepager.assets_dict[asset][3])
               
        #print(f"ticker_show_1:: {ticker_show_1} || ticker_rate_type:: {ticker_show_1} ||  ticker_plot_style:: {ticker_plot_color} ||  ticker_plot_style:: {ticker_plot_linestyle}")
        
        # historical data | Ticker1
        ###########################################################################
                
        today_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.today_dt)
        previous_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.previous_dt)
        last_EOW_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_EOW_dt)
        last_EOM_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_EOM_dt)
        last_EOQ_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_EOQ_dt)
        last_EOY_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_EOY_dt)
               
        # last_1m_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_1m_dt)
        # last_3m_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_3m_dt)
        # last_12m_px_1 = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_12m_dt)
        
        if long_period == True:
            last_period1 = '1-year'
            last_period1_ticker1_px = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_12m_dt)
            last_period2 = '5-years'
            last_period2_ticker1_px = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_5y_dt)
            last_period3 = '10-years'
            last_period3_ticker1_px = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_10y_dt)
        else:
            last_period1 = '1-month'
            last_period1_ticker1_px = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_1m_dt)
            last_period2 = '3-months'
            last_period2_ticker1_px = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_3m_dt)
            last_period3 = '12-months'
            last_period3_ticker1_px = cls_df_rates.get_mkt_price(ticker_show_1,config_onepager.last_12m_dt)
        
        
        if 'RATE' in ticker_type_1.upper():
            previous_spread_1 = ut.calculate_change(today_px_1[1] , previous_px_1[1])
            last_EOW_spread_1 = ut.calculate_change(today_px_1[1] , last_EOW_px_1[1])
            last_EOM_spread_1 = ut.calculate_change(today_px_1[1] , last_EOM_px_1[1])
            last_EOQ_spread_1 = ut.calculate_change(today_px_1[1] , last_EOQ_px_1[1])
            last_EOY_spread_1 = ut.calculate_change(today_px_1[1] , last_EOY_px_1[1])
            last_period1_spread_ticker1 = ut.calculate_change(today_px_1[1] , last_period1_ticker1_px[1])
            last_period2_spread_ticker1 = ut.calculate_change(today_px_1[1] , last_period2_ticker1_px[1])
            last_period3_spread_ticker1 = ut.calculate_change(today_px_1[1] , last_period3_ticker1_px[1])
        else:
            previous_spread_1 = ut.calculate_change_pct(today_px_1[1] , previous_px_1[1])
            last_EOW_spread_1 = ut.calculate_change_pct(today_px_1[1] , last_EOW_px_1[1])
            last_EOM_spread_1 = ut.calculate_change_pct(today_px_1[1] , last_EOM_px_1[1])
            last_EOQ_spread_1 = ut.calculate_change_pct(today_px_1[1] , last_EOQ_px_1[1])
            last_EOY_spread_1 = ut.calculate_change_pct(today_px_1[1] , last_EOY_px_1[1])
            last_period1_spread_ticker1 = ut.calculate_change_pct(today_px_1[1] , last_period1_ticker1_px[1])
            last_period2_spread_ticker1 = ut.calculate_change_pct(today_px_1[1] , last_period2_ticker1_px[1])
            last_period3_spread_ticker1 = ut.calculate_change_pct(today_px_1[1] , last_period3_ticker1_px[1])
        ###########################################################################
       
       # historical data | Ticker2
        ###########################################################################
        today_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.today_dt)
        previous_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.previous_dt)
        last_EOW_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_EOW_dt)
        last_EOM_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_EOM_dt)
        last_EOQ_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_EOQ_dt)
        last_EOY_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_EOY_dt)
        
        # last_1m_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_1m_dt)
        # last_3m_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_3m_dt)
        # last_12m_px_2 = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_12m_dt)
                
        if long_period == True:
            last_period1_ticker2_px = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_12m_dt)
            last_period2_ticker2_px = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_5y_dt)
            last_period3_ticker2_px = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_10y_dt)
        else:
            last_period1_ticker2_px = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_1m_dt)
            last_period2_ticker2_px = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_3m_dt)
            last_period3_ticker2_px = cls_df_rates.get_mkt_price(ticker_show_2,config_onepager.last_12m_dt)
        
        
        if 'RATE' in ticker_type_1.upper():
            previous_spread_2 = ut.calculate_change(today_px_2[1] , previous_px_2[1])
            last_EOW_spread_2 = ut.calculate_change(today_px_2[1] , last_EOW_px_2[1])
            last_EOM_spread_2 = ut.calculate_change(today_px_2[1] , last_EOM_px_2[1])
            last_EOQ_spread_2 = ut.calculate_change(today_px_2[1] , last_EOQ_px_2[1])
            last_EOY_spread_2 = ut.calculate_change(today_px_2[1] , last_EOY_px_2[1])
            last_period1_spread_ticker2 = ut.calculate_change(today_px_2[1] , last_period1_ticker2_px[1])
            last_period2_spread_ticker2 = ut.calculate_change(today_px_2[1] , last_period2_ticker2_px[1])
            last_period3_spread_ticker2 = ut.calculate_change(today_px_2[1] , last_period3_ticker2_px[1])
        else:
            previous_spread_2 = ut.calculate_change_pct(today_px_2[1] , previous_px_2[1])
            last_EOW_spread_2 = ut.calculate_change_pct(today_px_2[1] , last_EOW_px_2[1])
            last_EOM_spread_2 = ut.calculate_change_pct(today_px_2[1] , last_EOM_px_2[1])
            last_EOQ_spread_2 = ut.calculate_change_pct(today_px_2[1] , last_EOQ_px_2[1])
            last_EOY_spread_2 = ut.calculate_change_pct(today_px_2[1] , last_EOY_px_2[1])
            last_period1_spread_ticker2 = ut.calculate_change_pct(today_px_2[1] , last_period1_ticker2_px[1])
            last_period2_spread_ticker2 = ut.calculate_change_pct(today_px_2[1] , last_period2_ticker2_px[1])
            last_period3_spread_ticker2 = ut.calculate_change_pct(today_px_2[1] , last_period3_ticker2_px[1])
        ###########################################################################
       
       
        # Statistics
        ###########################################################################
        
        if long_period == True:
            period_stats = '5Y'
            period_start_dt = dt.date(config_onepager.last_10y_dt.year, 1, 1)    #for plot
            period_start_stats_dt = config_onepager.last_5y_dt                   #for calculation
        else:
            period_stats = '12M'
            period_start_dt = config_onepager.last_EOQ_back8_dt  #for plot
            period_start_stats_dt = config_onepager.last_12m_dt  #for calculation
            

        period_end_dt = config_onepager.today_dt
        #df_historic = cls_df_rates.get_mkt_price_period(ticker_show_1,period_start_dt,period_end_dt)
        df_historic = cls_df_rates.get_mkt_price_period(tickers_list,period_start_dt,period_end_dt)
        #df_historic.to_csv(f"df_historic_{ticker_show_1}.csv")
        
        df_historic_stats_1 = cls_df_rates.get_mkt_price_period(ticker_show_1,period_start_stats_dt,period_end_dt)
        average_stats_1 = df_historic_stats_1.iloc[:, 0].mean()
        median_stats_1 = df_historic_stats_1.iloc[:, 0].median()
        min_stats_1 = df_historic_stats_1.iloc[:, 0].min()
        max_stats_1 = df_historic_stats_1.iloc[:, 0].max()
        #config_onepager.last_12m_dt = df_historic_12m_1.index.min()
        
        df_historic_stats_1['daily_return'] = df_historic_stats_1.iloc[:, 0] - df_historic_stats_1.iloc[:, 0].shift(1)
        #vol_12m_1 = df_historic_stats_1['daily_return'].std() * 2.33
        percentile_p1 = df_historic_stats_1.iloc[:, 0].quantile([0.01 , 0.99])

        #df_historic_12m_1.to_csv(f"df_historic_12m_1_{ticker_show_1}.csv")
        
        #########
        
        df_historic_stats_2 = cls_df_rates.get_mkt_price_period(ticker_show_2,period_start_stats_dt,period_end_dt)
        average_stats_2 = df_historic_stats_2.iloc[:, 0].mean()
        median_stats_2 = df_historic_stats_2.iloc[:, 0].median()
        min_stats_2 = df_historic_stats_2.iloc[:, 0].min()
        max_stats_2 = df_historic_stats_2.iloc[:, 0].max()
        config_onepager.last_stats_dt = df_historic_stats_1.index.min()
        
        df_historic_stats_2['daily_return'] = df_historic_stats_2.iloc[:, 0] - df_historic_stats_2.iloc[:, 0].shift(1)
        #vol_12m_2 = df_historic_stats_2['daily_return'].std() * 2.33
        percentile_p2 = df_historic_stats_2.iloc[:, 0].quantile([0.01 , 0.99])
        
        
        ###########################################################################
        
        # Chart
        ###########################################################################
        buffer = io.BytesIO()
        #ax1 = df_historic.plot(figsize=(5.6,3.6), x_compat=True, color=ticker_plot_style, linestyle='--')
        #ax1 =  df_historic.plot(figsize=(5.6,3.6), x_compat=True, color=colors_list, linestyle='-')
        df_historic.fillna(method="bfill", inplace=True)
        #ax1 =  df_historic.plot(figsize=(6,4.4), x_compat=True, color=colors_list, style=linestyle_list)
        ax1 =  df_historic.plot(figsize=(6,4.6), x_compat=True, color=colors_list, style=linestyle_list)
                
        if long_period == True:
            plot_ticks = YearLocator(month=1,day=1)
            plot_ticks_format = DateFormatter('%Y')
            ax1.set_xlim(xmin=(period_start_dt - dt.timedelta(days=2)))
            ax1.set_xlim(xmax=(config_onepager.next_EOY_dt + dt.timedelta(days=1)))
            img_space = "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdj+P///38ACfsD/QVDRcoAAAAASUVORK5CYII=' width='5px' height='1px'>"
        else:
            plot_ticks = MonthLocator((3,6,9,12),bymonthday=-1)
            plot_ticks_format = DateFormatter('%b%y')
            ax1.set_xlim(xmin=period_start_dt)
            ax1.set_xlim(xmax=config_onepager.this_EOQ_dt)
            img_space = ''        
        
        ax1.grid(which='major', axis='both', linestyle='--')
        ax1.xaxis.set_minor_locator(plot_ticks)
        ax1.xaxis.set_major_locator(plot_ticks)
        ax1.xaxis.set_major_formatter(plot_ticks_format)
        #ax1.set_ylim(ymin=5)
        #ax1.set_ylim(ymax=35)
        #ax1.xaxis.set_label_text('Dates')
        ax1.xaxis.label.set_visible(False)
        #ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        ax1.yaxis.set_major_formatter(ut.format_axis_label(ticker_quote_type))
        
        plt.xticks(rotation=0, ha='center')
        #plt.legend(assets_list,loc='upper left', fontsize=9)
        plt.legend(assets_list, fontsize=9)

        #plt.yticks(np.arange(df_historic.iloc[:, 0].min(), df_historic.iloc[:, 0].max(), 5))
        plt.savefig(buffer, format='png', bbox_inches = 'tight', pad_inches = 0.01)
        #plt.savefig(f'chart.png', bbox_inches = 'tight', pad_inches = 0.01)
                
        buffer.seek(0)
        img_plot = base64.b64encode(buffer.read()).decode('ascii')
        ###########################################################################


        # Creating HTML content
        ###########################################################################               
        spacing_for_alignment = '&nbsp;' # not used anymore
        content_HTML = f"""
                                <table>
                                    <tr>
                                        <td class='style_title' title='{group_query} - {ut.format_date(today_px_1[0])}'><div>{group_query} </div></td>
                                    </tr>
                                </table>
                                <hr> <!--  -->
                                <table class='style_table'>
                                    <tr>
                                        <td class='style_content_left'>
                                            <table class='style_table2'>
                                                <tr>
                                                    <td class='style_table_header'>Historical</td>
                                                    <td class='style_table_header2' colspan='3'>{asset_show_1}</td>
                                                    <td class='style_table_header2' colspan='3'>{asset_show_2}</td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(today_px_1[0])} | {ut.format_date(today_px_2[0])}'>Last close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_1[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px_2[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(previous_px_1[0])} | {ut.format_date(previous_px_2[0])}'>Previous close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(previous_px_1[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(previous_spread_1,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(previous_px_2[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(previous_spread_2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOW_px_1[0])} | {ut.format_date(last_EOW_px_2[0])}'>Last week's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOW_px_1[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOW_spread_1,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOW_px_2[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOW_spread_2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOM_px_1[0])} | {ut.format_date(last_EOM_px_2[0])}'>Last month's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOM_px_1[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOM_spread_1,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOM_px_2[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOM_spread_2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOQ_px_1[0])} | {ut.format_date(last_EOQ_px_2[0])}'>Last quarter's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOQ_px_1[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOQ_spread_1,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOQ_px_2[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOQ_spread_2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOY_px_1[0])} | {ut.format_date(last_EOY_px_2[0])}'>Last year's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOY_px_1[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOY_spread_1,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOY_px_2[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_EOY_spread_2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_period1_ticker1_px[0])} | {ut.format_date(last_period1_ticker2_px[0])}'>{last_period1}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period1_ticker1_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_period1_spread_ticker1 ,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period1_ticker2_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_period1_spread_ticker2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_period2_ticker1_px[0])} | {ut.format_date(last_period2_ticker2_px[0])}'>{last_period2}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period2_ticker1_px [1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_period2_spread_ticker1 ,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period2_ticker2_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_period2_spread_ticker2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_period3_ticker1_px[0])} | {ut.format_date(last_period3_ticker2_px[0])}'>{last_period3}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period3_ticker1_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_period3_spread_ticker1 ,ticker_type_1)}</td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period3_ticker2_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'>{ut.format_change_html_small(last_period3_spread_ticker2,ticker_type_2)}</td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                            </table>
                                            <br>
                                            <table class='style_table2'>
                                                <tr class=''>                 
                                                    <td class='style_table_header'>Statistics {period_stats}</td>
                                                    <td class='style_table_header2' colspan='3'><b><div title='{ut.format_date(period_start_stats_dt)} -> {ut.format_date(period_end_dt)}'>{asset_show_1}</div></b></td>
                                                    <td class='style_table_header2' colspan='3'><b><div title='{ut.format_date(period_start_stats_dt)} -> {ut.format_date(period_end_dt)}'>{asset_show_2}</div></b></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'>Median</td>
                                                    <td class='style_table_content2'>{ut.format_quote(median_stats_1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(median_stats_2,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'>Average</td>
                                                    <td class='style_table_content2'>{ut.format_quote(average_stats_1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(average_stats_2,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr  class=''>
                                                    <td class='style_table_content'>Max</td>
                                                    <td class='style_table_content2'>{ut.format_quote(max_stats_1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(max_stats_2,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'>Percentile 99%</td>
                                                    <td class='style_table_content2'>{ut.format_quote(percentile_p1[0.99],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(percentile_p2[0.99],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'>Min</td>
                                                    <td class='style_table_content2'>{ut.format_quote(min_stats_1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(min_stats_2,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'>Percentile 1%</td>
                                                    <td class='style_table_content2'>{ut.format_quote(percentile_p1[0.01],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(percentile_p2[0.01],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                            </table>
                                        </td>
                                        <td class='style_column_space'></td>
                                        <td class='style_content_right'>
                                            <table border='0' align='right'>
                                                <tr>
                                                    <td class='style_content_chart'>
                                                        <img src='data:image/png;base64,{img_plot}'>                                                    
                                                    </td>
                                                    <td>
                                                        {img_space}
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                <br>
        """

        #content_HTML = content_HTML.replace("                            ","")
        return content_HTML
    

