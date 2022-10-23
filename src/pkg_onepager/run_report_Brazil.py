import os, sys
sys.path.insert(1, os.path.abspath('./src'))
import pkg_onepager.config_module as config_onepager

import datetime as dt
import pkg_common.utils as ut
from pkg_bloomberg.CLS_Mkt_data import CLS_Mkt_data
from pkg_email.CLS_Msg_HTML import CLS_Msg_HTML
from pkg_onepager.CLS_Onepager_common import CLS_Onepager_common
from pkg_onepager.CLS_Onepager_report_asset_single import CLS_Onepager_report_asset
from pkg_onepager.CLS_Onepager_report_asset_group import CLS_Onepager_report_group
from pkg_onepager.CLS_Onepager_report_curve_single_tenors import CLS_Onepager_report_curve_tenors
from pkg_onepager.CLS_Onepager_report_curve_single_statistics import CLS_Onepager_report_curve_statistics
from pkg_onepager.CLS_Onepager_report_curve_comparison import CLS_Onepager_report_curve_comparison


def run_report_Brazil():

    print("Start processing...")
    
    # Initiate Market Data
    ##################################################################
    mkt_data = CLS_Mkt_data()
    mkt_data.load_prices()
    #mkt_data.shift_and_calculate_basis_spreads()
    #mkt_data.export_data_csv()

    #mkt_data.export_data_csv()
    #print(cls_mkt_data.pd_rates_data)

    # Initiate message class
    ##################################################################
    #config_onepager.email_subject = '[SRM Analytics] Markets Monitor | Brazil | ' + ut.format_date(config_onepager.today_dt)
    msg_title = '[SRM Analytics] Markets Monitor | Brazil | ' + ut.format_date(config_onepager.today_dt)
    message = CLS_Msg_HTML()
    message.set_subject(msg_title)
    #message.set_receiver(config_onepager.email_distribution_list)
    message.set_receiver("rubensh@iadb.org")
    #message.set_receiver(["markets.reporting@gmail.com"])

    
    # Initiate report class
    ##################################################################
    report_common = CLS_Onepager_common()
    report_asset = CLS_Onepager_report_asset()
    report_group = CLS_Onepager_report_group()

    report_curve_tenors = CLS_Onepager_report_curve_tenors()
    report_curve_statistics = CLS_Onepager_report_curve_statistics()
    report_curves = CLS_Onepager_report_curve_comparison()

    message.add_content_html(report_common.generate_html_header(msg_title))

    br_flag = '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'
    message.add_content_html(f"<img src=data:image/png;base64,{br_flag} width='128px' height='90px'><br><br>")

    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Brazilian Real") )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Ibovespa") )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "BRL PRE" , showtable=[0,1]) )
    message.add_content_html(report_curve_statistics.generate_html_curve_summary(mkt_data, "BRL PRE",[2,3,5,9,10]))
    message.add_content_html(report_curve_tenors.generate_html_curve_summary(mkt_data, "BRL PRE",[1,2,3,4,5,6,7,8,9,10]))
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Brazil 5Y CDS",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Ibovespa",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "IBOV Forward P/E",long_period=True) )

    message.add_content_html(report_common.generate_html_footer())
    message.save_html_file()

    if config_onepager.send_email_flag == True:
        if config_onepager.send_email_idb == True:
            message.send_email_idb()
        else:
            message.send_email_gmail()
    
    print("End processing...")
    

########################################################################################################################################################################
########################################################################################################################################################################
if __name__ == "__main__":
    config_onepager.initialize()
    run_report_Brazil()