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
from pkg_onepager.CLS_Onepager_report_summary_basis import CLS_Onepager_report_summary_basis

def run_report_BasisRisk():

    print("Start processing Basis Risk report...")

    # Initiate Market Data
    ##################################################################
    mkt_data = CLS_Mkt_data()
    mkt_data.load_prices()
    mkt_data.shift_and_calculate_basis_spreads()
    #mkt_data.export_data_csv()


    # Initiate message class
    ##################################################################
    #config_onepager.email_subject = '[SRM Analytics] Markets Monitor | Basis Risk | ' + ut.format_date(config_onepager.today_dt)
    msg_title = '[SRM Analytics] Markets Monitor | Basis Risk | ' + ut.format_date(config_onepager.today_dt)
    message = CLS_Msg_HTML()
    message.set_subject(msg_title)
    message.set_receiver(config_onepager.email_internal_srm_list)

    # Initiate report class
    ##################################################################
    report_common = CLS_Onepager_common()
    report_asset = CLS_Onepager_report_asset()
    report_group = CLS_Onepager_report_group()
    report_summary = CLS_Onepager_report_summary_basis()

    message.add_content_html(report_common.generate_html_header(msg_title))

    # message.add_content_html(report_summary.generate_html_summary_basis(mkt_data) )
    
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "Risk-free rates" , showtable=[0,1]) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "SOFR Average" , showtable=[0,1]) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "SOFR TERM" , showtable=[1,2]) )
    

    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "LIBOR" , showtable= [1,2]) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "Libor 3M (shifted) vs SOFR 90d comp." ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Spread: Libor 3M (shifted) - SOFR 90d comp.") )

    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "Libor 6M (shifted) vs SOFR 180d comp." ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Spread: Libor 6M (shifted) - SOFR 180d comp.") )

    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "SOFR Term 3M (shifted) vs SOFR 90d comp. (SOFR Term as a predictor)" ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Spread: SOFR Term 3M (shifted) - Sofr 90d comp.") )
    
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "SOFR Term 6M (shifted) vs SOFR 180d comp. (SOFR Term as a predictor)" ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Spread: SOFR Term 6M (shifted) - Sofr 180d comp." ) )

    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "Libor 3M vs SOFR Term 3M (Credit component)" ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Spread: Libor 3M - Sofr Term 3M" ) )

    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Market Basis Swap - Libor 3M vs SOFR Basis") )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "Market Basis Swap pricing" ) )

    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "BSBY",showtable= [2,3] ) )


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
    run_report_BasisRisk()