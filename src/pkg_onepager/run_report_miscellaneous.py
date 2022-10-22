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


def run_report_miscellaneous():

    print("Start processing...")

    # Initiate Market Data
    ##################################################################
    mkt_data = CLS_Mkt_data()
    mkt_data.load_prices()
    mkt_data.calculate_spreads()
    #mkt_data.shift_and_calculate_basis_spreads()
    #mkt_data.export_data_csv()

    # Initiate message class
    ##################################################################
    config.email_subject = '[SRM Analytics] Markets Monitor | Miscellaneous | ' + ut.format_date(config.today_dt)
    message = CLS_Msg_HTML()

    # Initiate report class
    ##################################################################
    report_common = CLS_Onepager_common()
    report_asset = CLS_Onepager_report_asset()
    report_group = CLS_Onepager_report_group()

    report_curve = CLS_Onepager_report_curve_tenors()
    report_curve_statistics = CLS_Onepager_report_curve_statistics()
    report_curves = CLS_Onepager_report_curve_comparison()

    message.add_content_html(report_common.generate_html_header())

    message.add_content_html(f"<h3 style='background-color:powderblue;'>Chart of the week</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "JPY/USD",long_period=True) )
    #message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "GBP/USD",long_period=True) )
    #message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Bloomberg UK Gilt 15+ TR value unhedged GBP",long_period=True) )

    message.add_content_html(f"<h3 style='background-color:powderblue;'>On inflation...</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "CPI YOY",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "CORE CPI YOY",long_period=True) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "US Personal Consumption Expenditures MOM" , showtable=[0,1],long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "UN Food and Agriculture World Food Price Index",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "OIL CME Futures",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Fed Funds",long_period=True) )

    message.add_content_html(f"<h3 style='background-color:powderblue;'>On recession...</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Spread: Treasury 10Y - Treasury 2Y",long_period=True ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "USD Real GDP QoQ",long_period=True ) )
    #message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "USD Real GDP YoY",long_period=True ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "US Unemployment Rate",long_period=True ) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "US Participation Rate",long_period=True ) )



    message.add_content_html(f"<h3 style='background-color:powderblue;'>On market sentiment...</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "VIX",long_period=True) )

    message.add_content_html(f"<h3 style='background-color:powderblue;'>On stock markets...</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "S&P500",long_period=True) )
    message.add_content_html(report_group.generate_html_group_summary(mkt_data, "S&P500 P/E" , showtable=[0,1],long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "NASDAQ",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "NASDAQ Forward P/E",long_period=True) )

    message.add_content_html(f"<h3 style='background-color:powderblue;'>On FX markets...</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "Dollar Index",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "EUR/USD",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "JPY/USD",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "GBP/USD",long_period=True) )

    message.add_content_html(f"<h3 style='background-color:powderblue;'>On Credit...</h3>")
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "CDX North America High Yield Index",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "CDX North America Investment Grade Index",long_period=True) )
    message.add_content_html(report_asset.generate_html_asset_summary(mkt_data, "CDX Markit Emerging Markets Index",long_period=True) )

    message.add_content_html(report_common.generate_html_footer())

    message.save_html_file()

    if config.send_email_flag == True:
        #message.send_email_gmail()
        message.send_email_idb()

    print("End processing...")
    

########################################################################################################################################################################
########################################################################################################################################################################
if __name__ == "__main__":
    config.initialize()
    run_report_miscellaneous()