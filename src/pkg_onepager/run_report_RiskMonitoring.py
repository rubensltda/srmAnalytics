import os, sys
sys.path.insert(1, os.path.abspath('./src'))
import pkg_onepager.config_module as config_onepager


import datetime as dt
import pkg_common.utils as ut
from pkg_bloomberg.CLS_Mkt_data import CLS_Mkt_data
from pkg_email.CLS_Msg_HTML import CLS_Msg_HTML
from pkg_onepager.CLS_Onepager_common import CLS_Onepager_common
from pkg_onepager.CLS_Onepager_report_summary_basis import CLS_Onepager_report_summary_basis
from pkg_onepager.CLS_Onepager_report_mtm_volatility import CLS_Onepager_report_mtm_volatility

def run_report_RiskMonitoring():

    print("Start processing Risk Monitoring report...")

    # Initiate Market Data
    ##################################################################
    mkt_data = CLS_Mkt_data()
    mkt_data.load_prices()
    #mkt_data.shift_and_calculate_basis_spreads()
    #mkt_data.export_data_csv()


    # Initiate message class
    ##################################################################
    #config_onepager.email_subject = '[SRM Analytics] Markets Monitor | Basis Risk | ' + ut.format_date(config_onepager.today_dt)
    msg_title = '[SRM Analytics] Markets Monitor | Risk Monitoring | ' + ut.format_date(config_onepager.today_dt)
    message = CLS_Msg_HTML()
    message.set_subject(msg_title)
    message.set_receiver(config_onepager.email_internal_srm_list)

    # Initiate report class
    ##################################################################
    report_common = CLS_Onepager_common()
    report_summary = CLS_Onepager_report_summary_basis()
    report_mtm = CLS_Onepager_report_mtm_volatility()

    message.add_content_html(report_common.generate_html_header(msg_title))

    # JAJO Basis summary
    message.add_content_html(f"<h3 style='background-color:powderblue;'>Basis Risk - JAJO reset</h3>")
    message.add_content_html(report_summary.generate_html_summary_basis(mkt_data) )

    # MTM Volatility
    message.add_content_html(f"<h3 style='background-color:powderblue;'>MTM Volatility</h3>")

    message.add_content_html(f"<font class='style_title'>Structural Hedging - Swaps</font><hr>")
    KRD_FV_SH = [14951, -650363 , -589989, -781541, -495277, -642452, -1480356, -718782, -964567, -930069, 704659, 748617, 720619, 657547, 603358, 544003, 503269, 443256, -387657, -593470, 679948, 4669802]
    message.add_content_html(report_mtm.generate_html_mtm_volatility(mkt_data,KRD_FV_SH) )
    
    message.add_content_html(f"<font class='style_title'>Balance Sheet - Fair Value Accounts</font><hr>")
    KRD_FV = [-192119,-677349,-531996,-761756, -790058, -138413, -848586, -922349, -1073037, -145584, 1199465, 1041222, 954095, 883523, 803439, 675947, 535045, 458041, -398102 , -580879, 680909, 4663367]
    message.add_content_html(report_mtm.generate_html_mtm_volatility(mkt_data,KRD_FV) )
    
    # ED estimation
    message.add_content_html(f"<h3 style='background-color:powderblue;'>ED Duration - Parametric estimation</h3>")
    message.add_content_html("TBD: Parametric estimation using BPV and Convexity")

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
    run_report_RiskMonitoring()