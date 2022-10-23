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



class CLS_Onepager_report_curve_tenors():
    
    def __init__(self):
        #
        # ("Class report initiated.")
        pass
        
    def generate_html_curve_summary(self, cls_df_rates, curve_query, showtable_tenors=[2,3,4,5,7,8,9,10,15,20,30]):
                
        #print(f"{asset_show_1} | {asset_show_2}")
        print(f"Generating single curve report: {curve_query}")
        
        date0 = config_onepager.today_dt
        date1 = config_onepager.previous_dt
        date2 = config_onepager.last_EOQ_dt
        
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
            
            tenor_rate_previous_day = cls_df_rates.get_mkt_price(tenor[1],date1)
            previous_day_rates_list.append(tenor_rate_previous_day[1])
            
            tenor_rate_previous_quarter = cls_df_rates.get_mkt_price(tenor[1],date2)
            previous_quarter_rates_list.append(tenor_rate_previous_quarter[1])
        
        date0 = tenor_rate[0]
        date1 = tenor_rate_previous_day[0]
        date2 = tenor_rate_previous_quarter[0]

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
        #plt.savefig(f'chart_cuve.png', bbox_inches = 'tight', pad_inches = 0.01)
        
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
                                        <td class='style_title' title='{curve_query}'> <div>{curve_query}</div> </td>
                                    </tr>
                                </table>
                                <hr> <!--  -->
                                <table class='style_table'>
                                    <tr>
                                        <td class='style_content_left'>
                                            <table class='style_table2'>
                                                <tr>
                                                    <td class='style_table_header2'>Tenors</td>
                                                    <td class='style_table_header2'><b>{ut.format_date_short(date0)}</b></td>
                                                    <td class='style_table_header2' colspan='3'><b>{ut.format_date_short(date1)}</b></td>
                                                    <td class='style_table_header2' colspan='3'><b>{ut.format_date_short(date2)}</b></td>
                                                <tr>
        """
        
        tr_style = 0
        for tenor in showtable_tenors:
            
            if tenor < 1 :
                tenor_label = str(round((tenor * 12))) + 'M'
            else:
                tenor_label = str(tenor) + 'Y'
            
            curve_ticker = ut_curves.find_ticker_curve_by_tenor(config_onepager.ir_curves_dict, curve_query, tenor)
            rate_today = cls_df_rates.get_mkt_price(curve_ticker,date0)[1]
            rate_date1 = cls_df_rates.get_mkt_price(curve_ticker,date1)[1]
            rate_date2 = cls_df_rates.get_mkt_price(curve_ticker,date2)[1]

            change_rate_date1 = ut.calculate_change(rate_today , rate_date1)
            change_rate_date2 = ut.calculate_change(rate_today , rate_date2)
            
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
                                        <td class='style_table_content5' title='{curve_ticker}'>{tenor_label}</td>
                                        <td class='style_table_content5'>{ut.format_quote(rate_today)}</td>
                                        <td class='style_table_content2'>{ut.format_quote(rate_date1)}</td>
                                        <td class='style_table_content3'>{ut.format_change_html_small(change_rate_date1)}</td>
                                        <td class='style_table_content4'></td>
                                        <td class='style_table_content2'>{ut.format_quote(rate_date2)}</td>
                                        <td class='style_table_content3'>{ut.format_change_html_small(change_rate_date2)}</td>
                                        <td class='style_table_content4'></td>
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
    

