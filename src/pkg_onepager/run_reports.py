# import os, sys
# sys.path.insert(1, os.path.abspath('./src'))
import pkg_onepager.config_module as config_onepager

#from cProfile import run
import datetime as dt
from pkg_bloomberg.CLS_Mkt_data import CLS_Mkt_data
from pkg_onepager.run_report_BasisRisk import run_report_BasisRisk
from pkg_onepager.run_report_Brazil import run_report_Brazil
from pkg_onepager.run_report_USrates import run_report_USrates
from pkg_onepager.run_report_miscellaneous import run_report_miscellaneous


def run_reports():
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Starting generating reports...")
    
    
    config_onepager.initialize()
    mkt_data = CLS_Mkt_data()
    mkt_data.load_prices()
    #mkt_data.calculate_spreads()
    #mkt_data.shift_and_calculate_basis_spreads()

    last_available_date = mkt_data.get_last_available_date()
    #print(last_available_date)
    today_wd = config_onepager.today_dt.weekday()
    #print(f"wheekday = {today_wd}"  )

    if last_available_date < config_onepager.today_dt:
        print(f"Market data needs to be updated to {config_onepager.today_dt} || Last_available_date: {last_available_date}")
    elif (today_wd == 5 or today_wd == 6):
        print(f"Weekend, not run reports.")
    # implement holiday check    
    else:
        if (today_wd == 0 or today_wd == 1 or today_wd == 2 or today_wd == 3):
            run_report_BasisRisk()
            run_report_USrates()
            run_report_Brazil()

        elif (today_wd == 4):
            run_report_BasisRisk()
            run_report_USrates()
            run_report_Brazil()
            run_report_miscellaneous()
        
        mkt_data.export_data_csv()
    
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Finished generating reports.")


########################################################################################################################################################################
########################################################################################################################################################################
if __name__ == "__main__":
    run_reports()
    

    

# else:
#     print("Not a business day.")



# Weekdays
#############
# 0 Monday
# 1 Tuesday
# 2 Wednesday
# 3 Thursday
# 4 Friday
# 5 Saturday
# 6 Sunday

