import schedule
import time
import datetime as dt

from pkg_bloomberg.run_bbg_query import run_bbg_query
from pkg_onepager.run_reports import run_reports






def get_bbg_data():
    today_dt = dt.date.today() 
    today_wd = today_dt.weekday()
    #today_wd = 4
    if (today_wd == 5 or today_wd == 6):
        print(f"Weekend, not run bloomberg.")
    else:
        now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        print(f"{now}: Calling job bloomberg...")
        run_bbg_query()


def generate_reports():
    today_dt = dt.date.today() 
    today_wd = today_dt.weekday()
    #today_wd = 4
    if (today_wd == 5 or today_wd == 6):
        print(f"Weekend, not run reports.")
    else:
        now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        print(f"{now}: Calling job reports...")
        run_reports()


schedule.every().day.at("10:23:00").do(get_bbg_data)
schedule.every().day.at("10:25:00").do(generate_reports)


now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
print(f"{now}: Starting thread...")

while True:
    schedule.run_pending()
    time.sleep(5) # wait 5 seconds