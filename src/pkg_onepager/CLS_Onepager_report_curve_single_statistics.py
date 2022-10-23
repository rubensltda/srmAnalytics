#import datetime as dt
#import numpy as np
import io
import base64
from logging import NullHandler
from tokenize import group    

import pandas as pd
import numpy as np
from scipy.interpolate import interp1d, splrep, splev
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter
from matplotlib.ticker import FormatStrFormatter
from email.mime.image import MIMEImage

import pkg_onepager.config_module as config_onepager
import pkg_common.utils as ut
import pkg_onepager.functions_curves as ut_curves



class CLS_Onepager_report_curve_statistics():
    
    def __init__(self):
        #
        # ("Class report initiated.")
        pass
        
    def generate_html_curve_summary(self, cls_df_rates, curve_query, showtable_tenors=[2,5,10,20,30]):
                
        date0 = config_onepager.today_dt
        date1 = config_onepager.previous_dt
        date2 = config_onepager.last_EOQ_dt
        
                
        #print(f"{asset_show_1} | {asset_show_2}")
        print(f"Generating curve report with statistics: {curve_query}")
        
        tickers_list = [ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve_query, showtable_tenors[0]),
                        ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve_query, showtable_tenors[1]),
                        ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve_query, showtable_tenors[2]),
                        ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve_query, showtable_tenors[3]),
                        ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve_query, showtable_tenors[4])
                        ]
        #print(tickers_list)
        
        today_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.today_dt),
                     cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.today_dt),
                     cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.today_dt),
                     cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.today_dt),
                     cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.today_dt)
                     ]
        #print(today_px)        

        previous_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.previous_dt),
                        cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.previous_dt),
                        cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.previous_dt),
                        cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.previous_dt),
                        cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.previous_dt)
                     ]
        #print(previous_px)      
        date1 = previous_px[0][0]  

        last_EOW_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOW_dt),
                        cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOW_dt),
                        cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOW_dt),
                        cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOW_dt),
                        cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOW_dt)
                     ]
        #print(last_EOW_px)        

        last_EOM_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOM_dt),
                        cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOM_dt),
                        cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOM_dt),
                        cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOM_dt),
                        cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOM_dt)
                ]
        #print(last_EOM_px)        

        last_EOQ_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOQ_dt),
                        cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOQ_dt),
                        cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOQ_dt),
                        cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOQ_dt),
                        cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOQ_dt)
                ]
        #print(last_EOQ_px)        
        date2 = last_EOQ_px[0][0]  

        last_EOY_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOY_dt),
                        cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOY_dt),
                        cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOY_dt),
                        cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOY_dt),
                        cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOY_dt)
                ]
        #print(last_EOY_px)        

        last_1m_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_1m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_1m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_1m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_1m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_1m_dt)
                ]
        #print(last_1m_px)        

        last_3m_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_3m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_3m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_3m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_3m_dt),
                       cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_3m_dt)
                ]
        #print(last_3m_px)        

        last_12m_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_12m_dt),
                        cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_12m_dt),
                        cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_12m_dt),
                        cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_12m_dt),
                        cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_12m_dt)
                ]
        #print(last_12m_px)        
        
        
        # Statistics
        ###########################################################################
        period_start_dt = config_onepager.last_EOQ_back8_dt
        period_end_dt = config_onepager.today_dt
        
        #df_historic = cls_df_rates.get_mkt_price_period(tickers_list,period_start_dt,period_end_dt)
        df_historic_12m_0 = cls_df_rates.get_mkt_price_period(tickers_list[0],config_onepager.last_12m_dt,period_end_dt)
        df_historic_12m_1 = cls_df_rates.get_mkt_price_period(tickers_list[1],config_onepager.last_12m_dt,period_end_dt)
        df_historic_12m_2 = cls_df_rates.get_mkt_price_period(tickers_list[2],config_onepager.last_12m_dt,period_end_dt)
        df_historic_12m_3 = cls_df_rates.get_mkt_price_period(tickers_list[3],config_onepager.last_12m_dt,period_end_dt)
        df_historic_12m_4 = cls_df_rates.get_mkt_price_period(tickers_list[4],config_onepager.last_12m_dt,period_end_dt)
        #df_historic_12m_0.to_csv(f"df_historic_{ticker_show_1}.csv")

        average_12M = [ df_historic_12m_0.iloc[:, 0].mean(),
                        df_historic_12m_1.iloc[:, 0].mean(),
                        df_historic_12m_2.iloc[:, 0].mean(),
                        df_historic_12m_3.iloc[:, 0].mean(),
                        df_historic_12m_4.iloc[:, 0].mean(),
                       ]
        median_12M = [  df_historic_12m_0.iloc[:, 0].median(),
                        df_historic_12m_1.iloc[:, 0].median(),
                        df_historic_12m_2.iloc[:, 0].median(),
                        df_historic_12m_3.iloc[:, 0].median(),
                        df_historic_12m_4.iloc[:, 0].median(),
                      ]
        min_12M = [ df_historic_12m_0.iloc[:, 0].min(),
                    df_historic_12m_1.iloc[:, 0].min(),
                    df_historic_12m_2.iloc[:, 0].min(),
                    df_historic_12m_3.iloc[:, 0].min(),
                    df_historic_12m_4.iloc[:, 0].min(),
                   ]
        
        max_12M = [ df_historic_12m_0.iloc[:, 0].max(),
                    df_historic_12m_1.iloc[:, 0].max(),
                    df_historic_12m_2.iloc[:, 0].max(),
                    df_historic_12m_3.iloc[:, 0].max(),
                    df_historic_12m_4.iloc[:, 0].max(),
                   ]
        
        df_historic_12m_0['daily_return'] = df_historic_12m_0.iloc[:, 0] - df_historic_12m_0.iloc[:, 0].shift(1)
        df_historic_12m_1['daily_return'] = df_historic_12m_1.iloc[:, 0] - df_historic_12m_0.iloc[:, 0].shift(1)
        df_historic_12m_2['daily_return'] = df_historic_12m_2.iloc[:, 0] - df_historic_12m_0.iloc[:, 0].shift(1)
        df_historic_12m_3['daily_return'] = df_historic_12m_3.iloc[:, 0] - df_historic_12m_0.iloc[:, 0].shift(1)
        df_historic_12m_4['daily_return'] = df_historic_12m_4.iloc[:, 0] - df_historic_12m_0.iloc[:, 0].shift(1)
            
        vol_12m = [ df_historic_12m_0['daily_return'].std() * 2.33,
                    df_historic_12m_1['daily_return'].std() * 2.33,
                    df_historic_12m_2['daily_return'].std() * 2.33,
                    df_historic_12m_3['daily_return'].std() * 2.33,
                    df_historic_12m_4['daily_return'].std() * 2.33
                   ]
        
        config_onepager.last_12m_dt = df_historic_12m_0.index.min()
        ###########################################################################
        
        # Chart
        ###########################################################################
        # For plot
        ###########################################################################
        curve_spec = config_onepager.ir_curves_dict[curve_query][0]
        tenors_list = []
        rates_list = []
        previous_day_rates_list = []
        previous_quarter_rates_list = []
        
        for tenor in curve_spec:
            tenors_list.append(tenor[0])
            
            tenor_rate = cls_df_rates.get_mkt_price(tenor[1],date0)
            rates_list.append(tenor_rate[1])
            
            tenor_rate_previous_day = cls_df_rates.get_mkt_price(tenor[1],date1)
            previous_day_rates_list.append(tenor_rate_previous_day[1])
            
            tenor_rate_previous_quarter = cls_df_rates.get_mkt_price(tenor[1],date2)
            previous_quarter_rates_list.append(tenor_rate_previous_quarter[1])
        
        plot_rates = {'Tenors': tenors_list, 'Rates':  rates_list}
        df_rates = pd.DataFrame(plot_rates)
        cubicspline_1 = splrep(df_rates['Tenors'], df_rates['Rates'])
        x_rates_interpolated = np.linspace(df_rates['Tenors'].min(), df_rates['Tenors'].max(), 100)
        y_rates_interpolated = splev(x_rates_interpolated,cubicspline_1)

        plot_previous_day_rates = {'Tenors': tenors_list, 'Rates':  previous_day_rates_list}
        df_previous_day_rates = pd.DataFrame(plot_previous_day_rates)
        cubicspline_2 = splrep(df_previous_day_rates['Tenors'], df_previous_day_rates['Rates'])
        x_previous_day_rates_interpolated = np.linspace(df_previous_day_rates['Tenors'].min(), df_previous_day_rates['Tenors'].max(), 100)
        y_previous_day_rates_interpolated = splev(x_previous_day_rates_interpolated, cubicspline_2)

        plot_previous_quarter_rates = {'Tenors': tenors_list, 'Rates':  previous_quarter_rates_list}
        df_previous_quarter_rates = pd.DataFrame(plot_previous_quarter_rates)
        cubicspline_3 = splrep(df_previous_quarter_rates['Tenors'], df_previous_quarter_rates['Rates'])
        x_previous_quarter_rates_interpolated = np.linspace(df_previous_quarter_rates['Tenors'].min(), df_previous_quarter_rates['Tenors'].max(), 100)
        y_previous_quarter_rates_interpolated = splev(x_previous_quarter_rates_interpolated, cubicspline_3)

        buffer = io.BytesIO()

        color_plot_curve = config_onepager.ir_curves_dict[curve_query][1]
        color_plot_marker = config_onepager.ir_curves_dict[curve_query][1]

        fig1, ax1 = plt.subplots(figsize=(6,3.85))
        #fig1, ax1 = plt.subplots(figsize=(6,4.4))
                
        ax1.plot(x_rates_interpolated, y_rates_interpolated, '-', color=color_plot_curve)
        ax1.plot(x_previous_day_rates_interpolated, y_previous_day_rates_interpolated, '--', color=color_plot_curve, linewidth=1)
        #ax1.plot(x_previous_quarter_rates_interpolated, y_previous_quarter_rates_interpolated, ':', color=color_plot_curve, linewidth=1)
        ax1.plot(x_previous_quarter_rates_interpolated, y_previous_quarter_rates_interpolated, '-', color='gray', linewidth=1)
                        
        plt.legend([f'{curve_query}: {ut.format_date(date0)}',f'{curve_query}: {ut.format_date(date1)}',f'{curve_query}: {ut.format_date(date2)}'], fontsize=9)
        
        ax1.plot(plot_rates['Tenors'], plot_rates['Rates'], '+', color=color_plot_marker)
        ax1.plot(plot_previous_day_rates['Tenors'], plot_previous_day_rates['Rates'], '+', color=color_plot_marker)
        #ax1.plot(plot_previous_quarter_rates['Tenors'], plot_previous_quarter_rates['Rates'], '+', color=color_plot_marker)
        ax1.plot(plot_previous_quarter_rates['Tenors'], plot_previous_quarter_rates['Rates'], '+', color='gray')
        
        ax1.grid(which='major', axis='both', linestyle='--')
        
        # ax1.set_xlabel("Yrs")
        # x_cord = max(plot_rates['Tenors']) + 0.5
        # ticklab = ax1.xaxis.get_ticklabels()[0]
        # ax1.xaxis.set_label_coords(x_cord, 0, transform=ticklab.get_transform())

        ax1.set_xlim(xmax=(max(tenors_list)+1))
        ax1.xaxis.label.set_visible(True)
        
        ax1.yaxis.label.set_visible(False)
        ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        

        plt.xticks(rotation=0, ha='center')
        #plt.legend(assets_list,loc='upper left', fontsize=9)

        
        #plt.yticks(np.arange(df_historic.iloc[:, 0].min(), df_historic.iloc[:, 0].max(), 5))
        plt.savefig(buffer, format='png', bbox_inches = 'tight', pad_inches = 0.01)
        #plt.savefig(f'chart.png', bbox_inches = 'tight', pad_inches = 0.01)
        
        buffer.seek(0)
        img_plot = base64.b64encode(buffer.read()).decode('ascii')
        #img_space = "<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdj+P///38ACfsD/QVDRcoAAAAASUVORK5CYII=' width='22px' height='1px'>"
        img_space = "<img src=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAIAAABL1vtsAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAjSURBVDhPY/hPMRg1AgFGjUCAUSMQYNQIBBg1AgEoNuL/fwDRkqagQgCH/QAAAABJRU5ErkJggg== width=22px height=1px>"
 
        ###########################################################################


        # Creating HTML content
        ###########################################################################               
        spacing_for_alignment = '&nbsp;' # not used anymore
        content_HTML = f"""
                                <table>
                                    <tr>
                                        <td class='style_title' title='{curve_query} - {ut.format_date(today_px[0][0])}'><div>{curve_query} </div></td>
                                    </tr>
                                </table>
                                <hr> <!--  -->
                                <table class='style_table'>
                                    <tr>
                                        <td class='style_content_left'>
                                            <table class='style_table2'>
                                                <tr>
                                                    <td class='style_table_header'>Curve</td>
                                                    <td class='style_table_header3' title='{tickers_list[0]}'><b>{str(showtable_tenors[0]) + 'Y'}</b></td>
                                                    <td class='style_table_header3' title='{tickers_list[1]}'><b>{str(showtable_tenors[1]) + 'Y'}</b></td>
                                                    <td class='style_table_header3' title='{tickers_list[2]}'><b>{str(showtable_tenors[2]) + 'Y'}</b></td>
                                                    <td class='style_table_header3' title='{tickers_list[3]}'><b>{str(showtable_tenors[3]) + 'Y'}</b></td>
                                                    <td class='style_table_header3' title='{tickers_list[4]}'><b>{str(showtable_tenors[4]) + 'Y'}</b></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(today_px[0][0])}'>Last close</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(today_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(today_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(today_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(today_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(today_px[4][1])}</td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(previous_px[0][0])}'>Previous close</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(previous_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(previous_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(previous_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(previous_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(previous_px[4][1])}</td>
                                                </tr>
                                                 <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOW_px[0][0])}'>Last week's close</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOW_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOW_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOW_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOW_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOW_px[4][1])}</td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOM_px[0][0])}'>Last month's close</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOM_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOM_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOM_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOM_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOM_px[4][1])}</td>
                                                </tr>
                                                 <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOQ_px[0][0])}'>Last quarter's close</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOQ_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOQ_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOQ_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOQ_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOQ_px[4][1])}</td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_EOY_px[0][0])}'>Last year's close</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOY_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOY_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOY_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOY_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_EOY_px[4][1])}</td>
                                                </tr>
                                                 <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_1m_px[0][0])}'>1-month</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_1m_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_1m_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_1m_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_1m_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_1m_px[4][1])}</td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_3m_px[0][0])}'>3-months</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_3m_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_3m_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_3m_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_3m_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_3m_px[4][1])}</td>
                                                </tr>
                                                 <tr class=''>
                                                    <td class='style_table_content'><div title='{ut.format_date(last_12m_px[0][0])}'>12-months</div></td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_12m_px[0][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_12m_px[1][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_12m_px[2][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_12m_px[3][1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(last_12m_px[4][1])}</td>
                                                </tr>
                                            </table>
                                            <br>
                                            <table class='style_table2'>
                                                <tr class=''>                 
                                                    <td class='style_table_header'>Statistics 12M</td>
                                                    <td class='style_table_header3'><b><div title='{ut.format_date(config_onepager.last_12m_dt)} -> {ut.format_date(config_onepager.today_dt)}'>{str(showtable_tenors[0]) + 'Y'}</div></b></td>
                                                    <td class='style_table_header3'><b><div title='{ut.format_date(config_onepager.last_12m_dt)} -> {ut.format_date(config_onepager.today_dt)}'>{str(showtable_tenors[1]) + 'Y'}</div></b></td>
                                                    <td class='style_table_header3'><b><div title='{ut.format_date(config_onepager.last_12m_dt)} -> {ut.format_date(config_onepager.today_dt)}'>{str(showtable_tenors[2]) + 'Y'}</div></b></td>
                                                    <td class='style_table_header3'><b><div title='{ut.format_date(config_onepager.last_12m_dt)} -> {ut.format_date(config_onepager.today_dt)}'>{str(showtable_tenors[3]) + 'Y'}</div></b></td>
                                                    <td class='style_table_header3'><b><div title='{ut.format_date(config_onepager.last_12m_dt)} -> {ut.format_date(config_onepager.today_dt)}'>{str(showtable_tenors[4]) + 'Y'}</div></b></td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'>Median</td>
                                                    <td class='style_table_content5'>{ut.format_quote(median_12M[0])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(median_12M[1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(median_12M[2])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(median_12M[3])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(median_12M[4])}</td>
                                                </tr>
                                                <tr class='style_table_row'>
                                                    <td class='style_table_content'>Average</td>
                                                    <td class='style_table_content5'>{ut.format_quote(average_12M[0])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(average_12M[1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(average_12M[2])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(average_12M[3])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(average_12M[4])}</td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'>1d vol @99%</td>
                                                    <td class='style_table_content5'>{ut.format_quote(vol_12m[0])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(vol_12m[1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(vol_12m[2])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(vol_12m[3])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(vol_12m[4])}</td>
                                                </tr>
                                                <tr  class='style_table_row'>
                                                    <td class='style_table_content'>Max</td>
                                                    <td class='style_table_content5'>{ut.format_quote(max_12M[0])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(max_12M[1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(max_12M[2])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(max_12M[3])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(max_12M[4])}</td>
                                                </tr>
                                                <tr class=''>
                                                    <td class='style_table_content'>Min</td>
                                                    <td class='style_table_content5'>{ut.format_quote(min_12M[0])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(min_12M[1])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(min_12M[2])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(min_12M[3])}</td>
                                                    <td class='style_table_content5'>{ut.format_quote(min_12M[4])}</td>
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
        
        return content_HTML
    

