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



class CLS_Onepager_report_curve_comparison():
    
    def __init__(self):
        #
        # ("Class report initiated.")
        pass
        
    def generate_html_curve_summary(self, cls_df_rates, curves_query, showtable_tenors=[2,3,4,5,7,8,9,10,15,20,30]):
                
        #print(f"{asset_show_1} | {asset_show_2}")
        print(f"Generating curve comparison report: {curves_query}")
        
        curve1 = curves_query[0]
        curve2 = curves_query[1]
        
        
        # tickers_list = [ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve1, showtable_tenors[0]),
        #                 ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve1, showtable_tenors[1]),
        #                 ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve1, showtable_tenors[2]),
        #                 ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve1, showtable_tenors[3]),
        #                 ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve1, showtable_tenors[4])
        #                 ]
        # #print(tickers_list)
        
        # today_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.today_dt),
        #              cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.today_dt),
        #              cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.today_dt),
        #              cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.today_dt),
        #              cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.today_dt)
        #              ]
        # #print(today_px)        

        # previous_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.previous_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.previous_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.previous_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.previous_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.previous_dt)
        #              ]
        # #print(previous_px)        

        # last_EOW_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOW_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOW_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOW_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOW_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOW_dt)
        #              ]
        # #print(last_EOW_px)        

        # last_EOM_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOM_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOM_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOM_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOM_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOM_dt)
        #         ]
        # #print(last_EOM_px)        

        # last_EOQ_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOQ_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOQ_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOQ_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOQ_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOQ_dt)
        #         ]
        # #print(last_EOQ_px)        
        
        # last_EOY_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_EOY_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_EOY_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_EOY_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_EOY_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_EOY_dt)
        #         ]
        # #print(last_EOY_px)        

        # last_1m_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_1m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_1m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_1m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_1m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_1m_dt)
        #         ]
        # #print(last_1m_px)        

        # last_3m_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_3m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_3m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_3m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_3m_dt),
        #                cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_3m_dt)
        #         ]
        # #print(last_3m_px)        

        # last_12m_px =  [cls_df_rates.get_mkt_price(tickers_list[0],config_onepager.last_12m_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[1],config_onepager.last_12m_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[2],config_onepager.last_12m_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[3],config_onepager.last_12m_dt),
        #                 cls_df_rates.get_mkt_price(tickers_list[4],config_onepager.last_12m_dt)
        #         ]
        # #print(last_12m_px)        
        
        
               
        # Chart
        ###########################################################################
        # For plot
        ###########################################################################
        curve_spec1 = config_onepager.ir_curves_dict[curve1][0]
        tenors_list1 = []
        tickers_list1 = []
        rates_list1 = []
        
        for tenor in curve_spec1:
            tenors_list1.append(tenor[0])
            tickers_list1.append(tenor[1])
            
            tenor_rate = cls_df_rates.get_mkt_price(tenor[1],config_onepager.today_dt)
            rates_list1.append(tenor_rate[1])
            
        date_plot = tenor_rate[0]

        plot_rates = {'Tenors': tenors_list1, 'Rates':  rates_list1}
        df_rates = pd.DataFrame(plot_rates)
        cubicspline_1 = splrep(df_rates['Tenors'], df_rates['Rates'])
        x_rates_interpolated_1 = np.linspace(df_rates['Tenors'].min(), df_rates['Tenors'].max(), 100)
        y_rates_interpolated_1 = splev(x_rates_interpolated_1,cubicspline_1)


        curve_spec2 = config_onepager.ir_curves_dict[curve2][0]
        tenors_list2 = []
        tickers_list2 = []
        rates_list2 = []
        
        for tenor in curve_spec2:
            tenors_list2.append(tenor[0])
            tickers_list2.append(tenor[1])
            
            tenor_rate = cls_df_rates.get_mkt_price(tenor[1],config_onepager.today_dt)
            rates_list2.append(tenor_rate[1])
            
        plot_rates2 = {'Tenors': tenors_list2, 'Rates':  rates_list2}
        df_rates = pd.DataFrame(plot_rates2)
        cubicspline_2 = splrep(df_rates['Tenors'], df_rates['Rates'])
        x_rates_interpolated_2 = np.linspace(df_rates['Tenors'].min(), df_rates['Tenors'].max(), 100)
        y_rates_interpolated_2 = splev(x_rates_interpolated_2,cubicspline_2)



        buffer = io.BytesIO()

        color_plot_curve1 = config_onepager.ir_curves_dict[curve1][1]
        color_plot_marker1 = config_onepager.ir_curves_dict[curve1][1]
        color_plot_curve2 = config_onepager.ir_curves_dict[curve2][1]
        color_plot_marker2 = config_onepager.ir_curves_dict[curve2][1]

        fig1, ax1 = plt.subplots(figsize=(6,3.85))
        #fig1, ax1 = plt.subplots(figsize=(6,4.4))
        
        ax1.plot(x_rates_interpolated_1, y_rates_interpolated_1, '-', color=color_plot_curve1)
        ax1.plot(x_rates_interpolated_2, y_rates_interpolated_2, '-', color=color_plot_curve2)
        plt.legend([curve1 + ': '+ ut.format_date(date_plot), curve2 + ': ' + ut.format_date(date_plot)], fontsize=9)
        
        ax1.plot(plot_rates['Tenors'], plot_rates['Rates'], '+', color=color_plot_marker1)
        ax1.plot(plot_rates2['Tenors'], plot_rates2['Rates'], '+', color=color_plot_marker2)


        
        ax1.grid(which='major', axis='both', linestyle='--')
       
        # ax1.set_xlabel("Yrs")
        # x_cord = max(plot_rates['Tenors']) + 0.5
        # ticklab = ax1.xaxis.get_ticklabels()[0]
        # ax1.xaxis.set_label_coords(x_cord, 0, transform=ticklab.get_transform())

        ax1.set_xlim(xmax=31)
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
        #img_space = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdj+P///38ACfsD/QVDRcoAAAAASUVORK5CYII='
        #img_space = "<img src=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAIAAABL1vtsAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAjSURBVDhPY/hPMRg1AgFGjUCAUSMQYNQIBBg1AgEoNuL/fwDRkqagQgCH/QAAAABJRU5ErkJggg== width=220px height=1px>"
        img_space = "<img src=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAIAAABL1vtsAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAjSURBVDhPY/hPMRg1AgFGjUCAUSMQYNQIBBg1AgEoNuL/fwDRkqagQgCH/QAAAABJRU5ErkJggg== width=22px height=1px>"
        
        
        ###########################################################################


        # Creating HTML content
        ###########################################################################               
        spacing_for_alignment = '&nbsp;' # not used anymore
        content_HTML = f"""
                                <table>
                                    <tr>
                                        <td class='style_title'> <div>{curve1} || {curve2}</div> </td>
                                    </tr>
                                </table>
                                <hr> <!--  -->
                                <table class='style_table'>
                                    <tr>
                                        <td class='style_content_left'>
                                            <table class='style_table2'>
                                                <tr>
                                                    <td class='style_table_header2'>Tenors</td>
                                                    <td class='style_table_header2'><b>{curve1}</b></td>
                                                    <td class='style_table_header2'><b>{curve2}</b></td>
                                                    <td class='style_table_header2'><b>Difference</b></td>
                                                <tr>
        """
        
        tr_style = 0
        for tenor in showtable_tenors:
            
            if tenor < 1 :
                tenor_label = str(round((tenor * 12))) + 'M'
            else:
                tenor_label = str(tenor) + 'Y'
            
            curve1_ticker = ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve1, tenor)
            curve2_ticker = ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve2, tenor)
            rate_curve1 = cls_df_rates.get_mkt_price(curve1_ticker,config_onepager.today_dt)[1]
            rate_curve2 = cls_df_rates.get_mkt_price(curve2_ticker,config_onepager.today_dt)[1]
            
            if isinstance(rate_curve1,str) or isinstance(rate_curve2,str):
                rate_diff = '-'
            else:
                rate_diff = rate_curve1 - rate_curve2                
            
            
            if tr_style == 0:
                content_HTML += f"""
                                    <tr class=''>
                                """
                tr_style = 1
            else:
                content_HTML +=  f"""
                                    <tr class='style_table_row'>
                                """
                tr_style = 0
            content_HTML += f"""
                                        <td class='style_table_content5' title='{curve1_ticker} || {curve2_ticker}'>{tenor_label}</td>
                                        <td class='style_table_content5'>{ut.format_quote(rate_curve1)}</td>
                                        <td class='style_table_content5'>{ut.format_quote(rate_curve2)}</td>
                                        <td class='style_table_content5'>{ut.format_change_html(rate_diff)}</td>
                                    </tr>
                                    
            """
        
        content_HTML += f"""
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
    

