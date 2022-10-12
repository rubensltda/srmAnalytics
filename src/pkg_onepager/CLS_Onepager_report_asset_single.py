#import datetime as dt
#import numpy as np
import io
import base64    

import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, YearLocator
from matplotlib.ticker import FormatStrFormatter
from email.mime.image import MIMEImage
import datetime as dt

import config_module as config
import pkg_common.utils as ut



class CLS_Onepager_report_asset():
    
    def __init__(self):
        #print("Class report initiated.")
        pass
        
    def generate_html_asset_summary(self, cls_df_rates, asset_query, long_period=False):
        
        asset_info = config.assets_dict[asset_query]
        ticker_query = asset_info[0]
        ticker_quote_type = asset_info[1]
        ticker_plot_color = asset_info[2]
        ticker_plot_linestyle = asset_info[3]
        #print(f"ticker_query:: {ticker_query} || ticker_rate_type:: {ticker_query} ||  ticker_plot_style:: {ticker_plot_color} ||  ticker_plot_style:: {ticker_plot_linestyle}")
        
        print(f"Generating Single asset report: {ticker_query}, long_period={long_period}")
        
        # historical data
        ###########################################################################
        today_px = cls_df_rates.get_mkt_price(ticker_query,config.today_dt)
        previous_px = cls_df_rates.get_mkt_price(ticker_query,config.previous_dt)
        last_EOW_px = cls_df_rates.get_mkt_price(ticker_query,config.last_EOW_dt)
        last_EOM_px = cls_df_rates.get_mkt_price(ticker_query,config.last_EOM_dt)
        last_EOQ_px = cls_df_rates.get_mkt_price(ticker_query,config.last_EOQ_dt)
        last_EOY_px = cls_df_rates.get_mkt_price(ticker_query,config.last_EOY_dt)
        
        if long_period == True:
            last_period1 = '1-year'
            last_period1_px = cls_df_rates.get_mkt_price(ticker_query,config.last_12m_dt)
            last_period2 = '5-years'
            last_period2_px = cls_df_rates.get_mkt_price(ticker_query,config.last_5y_dt)
            last_period3 = '10-years'
            last_period3_px = cls_df_rates.get_mkt_price(ticker_query,config.last_10y_dt)
        else:
            last_period1 = '1-month'
            last_period1_px = cls_df_rates.get_mkt_price(ticker_query,config.last_1m_dt)
            last_period2 = '3-months'
            last_period2_px = cls_df_rates.get_mkt_price(ticker_query,config.last_3m_dt)
            last_period3 = '12-months'
            last_period3_px = cls_df_rates.get_mkt_price(ticker_query,config.last_12m_dt)
        
        if 'RATE' in ticker_quote_type.upper():
            previous_spread = ut.calculate_change(today_px[1],previous_px[1])
            last_EOW_spread = ut.calculate_change(today_px[1],last_EOW_px[1])
            last_EOM_spread = ut.calculate_change(today_px[1],last_EOM_px[1])
            last_EOQ_spread = ut.calculate_change(today_px[1],last_EOQ_px[1])
            last_EOY_spread = ut.calculate_change(today_px[1],last_EOY_px[1])
            last_period1__spread = ut.calculate_change(today_px[1],last_period1_px[1])
            last_period2__spread = ut.calculate_change(today_px[1],last_period2_px[1])
            last_period3__spread = ut.calculate_change(today_px[1],last_period3_px[1])
        else:
            previous_spread = ut.calculate_change_pct(today_px[1],previous_px[1])
            last_EOW_spread = ut.calculate_change_pct(today_px[1],last_EOW_px[1])
            last_EOM_spread = ut.calculate_change_pct(today_px[1],last_EOM_px[1])
            last_EOQ_spread = ut.calculate_change_pct(today_px[1],last_EOQ_px[1])
            last_EOY_spread = ut.calculate_change_pct(today_px[1],last_EOY_px[1])
            last_period1__spread = ut.calculate_change_pct(today_px[1],last_period1_px[1])
            last_period2__spread = ut.calculate_change_pct(today_px[1],last_period2_px[1])
            last_period3__spread = ut.calculate_change_pct(today_px[1],last_period3_px[1])

        ###########################################################################
       
        # Statistics
        ###########################################################################
        if long_period == True:
            #period_start_dt = config.last_10y_dt
            period_start_dt = dt.date(config.last_10y_dt.year, 1, 1)
            period_stats_1 = '5-years'
            period_stats_2 = '10-years'
            period_start_stats1_dt = config.last_5y_dt
            period_start_stats2_dt = config.last_10y_dt

        else:
            period_start_dt = config.last_EOQ_back8_dt
            period_stats_1 = '3-months'
            period_stats_2 = '12-months'
            period_start_stats1_dt = config.last_3m_dt
            period_start_stats2_dt = config.last_12m_dt

        period_end_dt = config.today_dt

        df_historic = cls_df_rates.get_mkt_price_period(ticker_query,period_start_dt,period_end_dt)
        #df_historic.to_csv(f"df_historic_{ticker_query}.csv")
        
        df_historic_p1 = cls_df_rates.get_mkt_price_period(ticker_query,period_start_stats1_dt,period_end_dt)
        average_p1 = df_historic_p1.iloc[:, 0].mean()
        median_p1 = df_historic_p1.iloc[:, 0].median()
        min_p1 = df_historic_p1.iloc[:, 0].min()
        max_p1 = df_historic_p1.iloc[:, 0].max()
        config.last_p1_dt = df_historic_p1.index.min()
        
        df_historic_p1['daily_return'] = df_historic_p1.iloc[:, 0] - df_historic_p1.iloc[:, 0].shift(1)
        #vol_1d_p1 = df_historic_p1['daily_return'].std() * 2.33
        percentile_p1 = df_historic_p1.iloc[:, 0].quantile([0.01 , 0.99])
        #df_historic_p1.to_csv(f"df_historic_3m_{ticker_query}.csv")
        
        df_historic_p2 = cls_df_rates.get_mkt_price_period(ticker_query,period_start_stats2_dt,period_end_dt)
        average_p2 = df_historic_p2.iloc[:, 0].mean()
        median_p2 = df_historic_p2.iloc[:, 0].median()
        min_p2 = df_historic_p2.iloc[:, 0].min()
        max_p2 = df_historic_p2.iloc[:, 0].max()
        config.last_p2_dt = df_historic_p2.index.min()
        
        df_historic_p2['daily_return'] = df_historic_p2.iloc[:, 0] - df_historic_p2.iloc[:, 0].shift(1)
        #vol_1d_p2 = df_historic_p2['daily_return'].std() * 2.33
        percentile_p2 = df_historic_p2.iloc[:, 0].quantile([.01, .99])
        #df_historic_p2.to_csv(f"df_historic_12m_{ticker_query}.csv")
        ###########################################################################
        
        # Chart
        ###########################################################################
        buffer = io.BytesIO()
        #ax1 = df_historic.plot(figsize=(5.6,3.6), x_compat=True, color=ticker_plot_style, linestyle='--')
        df_historic.fillna(method="bfill", inplace=True)
        #ax1 = df_historic.plot(figsize=(6,4.4), x_compat=True, color=ticker_plot_color, linestyle=ticker_plot_linestyle)
        ax1 = df_historic.plot(figsize=(6,4.6), x_compat=True, color=ticker_plot_color, linestyle=ticker_plot_linestyle)
        
        if long_period == True:
            plot_ticks = YearLocator(month=1,day=1)
            plot_ticks_format = DateFormatter('%Y')
            ax1.set_xlim(xmin=(period_start_dt - dt.timedelta(days=2)))
            ax1.set_xlim(xmax=(config.next_EOY_dt + dt.timedelta(days=1)))
            img_space = "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdj+P///38ACfsD/QVDRcoAAAAASUVORK5CYII=' width='5px' height='1px'>"
        else:
            plot_ticks = MonthLocator((3,6,9,12),bymonthday=-1)
            plot_ticks_format = DateFormatter('%b%y')
            ax1.set_xlim(xmin=period_start_dt)
            ax1.set_xlim(xmax=config.this_EOQ_dt)
            img_space = ''
        
        #plot_ticks = MonthLocator(interval=3,bymonthday=-1)
        ax1.grid(which='major', axis='both', linestyle='--')
        ax1.xaxis.set_minor_locator(plot_ticks)
        ax1.xaxis.set_major_locator(plot_ticks)
        ax1.xaxis.set_major_formatter(plot_ticks_format)
                
        #ax1.xaxis.set_label_text('Dates')
        ax1.xaxis.label.set_visible(False)
        ax1.yaxis.set_major_formatter(ut.format_axis_label(ticker_quote_type))
        
        plt.xticks(rotation=0, ha='center')
        #plt.legend(loc='upper left')
        #plt.legend([f"{asset_query}"],loc='upper left')
        plt.legend([f"{asset_query}"], fontsize=9)

        #plt.yticks(np.arange(df_historic.iloc[:, 0].min(), df_historic.iloc[:, 0].max(), 5))
        plt.savefig(buffer, format='png', bbox_inches = 'tight', pad_inches = 0.01)
        #plt.savefig(f'chart.png', bbox_inches = 'tight', pad_inches = 0.1)
        
        buffer.seek(0)
        img_plot = base64.b64encode(buffer.read()).decode('ascii')
        ###########################################################################


        # Creating HTML content
        ###########################################################################               
        #not used anymore
        #img_filler = "<img src='data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII='>"
        #generated in the website: https://png-pixel.com/
        if (('RATE' in ticker_quote_type.upper()) and ('RATE_SPREAD' not in ticker_quote_type.upper())):
            label_column = 'Rate  '
        elif 'RATE_SPREAD' in ticker_quote_type.upper():
            label_column = 'Spread'
        elif 'PRICE' in ticker_quote_type.upper():
            label_column = 'Price '
        else:
            #label_column = ticker_quote_type
            label_column = '-'
        
        filler = (len(ut.format_quote(today_px[1],ticker_quote_type))-3)*"&nbsp;"
        
        
        content_HTML = f"""
                                <table>
                                    <tr>
                                        <td class='style_title' title='{ticker_query} - {ut.format_date(today_px[0])}'><div>{asset_query} </div></td>
                                    </tr>
                                </table>
                                <hr> <!--  -->
                                <table class='style_table'>
                                    <tr>
                                        <td  class='style_content_left'>
                                            <table class='style_table2' border='0'>
                                                <tr>
                                                    <td class='style_table_header'>Historical</td>
                                                    <td class='style_table_header2' colspan='3'>{label_column} {filler}</td>
                                                    <td class='style_table_header2' colspan='3'>Change {filler}</td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(today_px[0])}'>Last close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(today_px[1],ticker_quote_type)} </td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'></td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(previous_px[0])}'>Previous close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(previous_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(previous_spread,ticker_quote_type)}  </td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOW_px[0])}'>Last week's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOW_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_EOW_spread,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOM_px[0])}'>Last month's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOM_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_EOM_spread,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOQ_px[0])}'>Last quarter's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOQ_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_EOQ_spread,ticker_quote_type)} </td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOY_px[0])}'>Last year's close</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_EOY_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_EOY_spread,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_period1_px[0])}'>{last_period1}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period1_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_period1__spread,ticker_quote_type)} </td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_period2_px[0])}'>{last_period2}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period2_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_period2__spread,ticker_quote_type)} </td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_period3_px[0])}'>{last_period3}</div></td>
                                                    <td class='style_table_content2'>{ut.format_quote(last_period3_px[1],ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_change_html(last_period3__spread,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                            </table>
                                            <br>
                                            <table class='style_table2'>
                                                <tr class=''>                 
                                                    <td class='style_table_header'>Statistics</td>
                                                    <td class='style_table_header2' colspan='3'><b><div title='{ut.format_date(period_start_stats1_dt)} -> {ut.format_date(period_end_dt)}'>{period_stats_1} {filler}</div></b></td>
                                                    <td class='style_table_header2' colspan='3'><b><div title='{ut.format_date(period_start_stats2_dt)} -> {ut.format_date(period_end_dt)}'>{period_stats_2} {filler}</div></b></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'>Median</td>
                                                    <td class='style_table_content2'>{ut.format_quote(median_p1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(median_p2,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'>Average</td>
                                                    <td class='style_table_content2'>{ut.format_quote(average_p1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(average_p2,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                </tr>
                                                <tr  class=''>
                                                    <td class='style_table_content'>Max</td>
                                                    <td class='style_table_content2'>{ut.format_quote(max_p1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(max_p2,ticker_quote_type)}</td>
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
                                                    <td class='style_table_content2'>{ut.format_quote(min_p1,ticker_quote_type)}</td>
                                                    <td class='style_table_content3'></td>
                                                    <td class='style_table_content4'></td>
                                                    <td class='style_table_content2'>{ut.format_quote(min_p2,ticker_quote_type)}</td>
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
    


    