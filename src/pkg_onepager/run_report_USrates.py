import datetime as dt

import config_module as config
import pkg_common.utils as ut
from pkg_bloomberg.CLS_Mkt_data import CLS_Mkt_data
from CLS_Msg_HTML import CLS_Msg_HTML
from CLS_Onepager_common import CLS_Onepager_common
from CLS_Onepager_report_asset_single import CLS_Onepager_report_asset
from CLS_Onepager_report_asset_group import CLS_Onepager_report_group
from CLS_Onepager_report_curve_single_tenors import CLS_Onepager_report_curve_tenors
from CLS_Onepager_report_curve_single_statistics import CLS_Onepager_report_curve_statistics
from CLS_Onepager_report_curve_comparison import CLS_Onepager_report_curve_comparison


def run_report_USrates():

    print("Start processing...")

    # Initiate Market Data
    ##################################################################
    mkt_data = CLS_Mkt_data()
    mkt_data.load_prices()
    #mkt_data.shift_and_calculate_basis_spreads()
    #mkt_data.export_data_csv()

    # Initiate message class
    ##################################################################
    config.email_subject = '[SRM Analytics] Markets Monitor | US Rates | ' + ut.format_date(config.today_dt)
    message = CLS_Msg_HTML()

    # Initiate report class
    ##################################################################
    report_common = CLS_Onepager_common()
    report_asset = CLS_Onepager_report_asset()
    report_group = CLS_Onepager_report_group()

    report_curve_tenors = CLS_Onepager_report_curve_tenors()
    report_curve_statistics = CLS_Onepager_report_curve_statistics()
    report_curves = CLS_Onepager_report_curve_comparison()
    message.add_content_html(report_common.generate_html_header())

    #message.add_content_html(report_curve.generate_html_curve_summary(mkt_data, "LIBOR YC",[2,3,4,5,7,8,9,10,15,20,30]))

    message.add_content_html(report_curve_tenors.generate_html_curve_summary(mkt_data, "SOFR YC",showtable_tenors=[0.25,0.5,1,2,3,4,5,6,7,8,9,10,20,30]))
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "SOFR Swaps" , showtable=[1,2]) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "SOFR TERM" , showtable=[1,2]) )
    message.add_content_html(report_curve_statistics.generate_html_curve_summary(mkt_data, "SOFR YC",showtable_tenors=[1,2,5,10,20]))

    message.add_content_html(report_curves.generate_html_curve_summary(mkt_data, ['LIBOR YC','SOFR YC'],showtable_tenors=[0.25,0.5,1,2,3,4,5,7,8,9,10,15,20,30]))

    message.add_content_html(report_curve_tenors.generate_html_curve_summary(mkt_data, "LIBOR YC",showtable_tenors=[0.25,0.5,1,2,3,4,5,6,7,8,9,10,20,30]))
    
    #message.add_content_html(report_curve_statistics.generate_html_curve_summary(mkt_data, "LIBOR YC",[2,5,10,20,30]))
    #message.add_content_html(report_group.generate_html_group_summary(mkt_data, "LIBOR Swaps" , [1,2]) )
    #message.add_content_html(report_group.generate_html_group_summary(mkt_data, "LIBOR" , showtable=[1,2]) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "Treasuries", showtable=[1,2] ) )

    message.add_content_html(report_common.generate_html_footer())

    message.save_html_file()

    if config.send_email_flag == True:
        message.send_email_gmail()
        #message.send_email_idb()

    print("End processing...")



########################################################################################################################################################################
########################################################################################################################################################################
if __name__ == "__main__":
    config.initialize()
    run_report_USrates()
    
