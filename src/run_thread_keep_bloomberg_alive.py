import schedule
import time
import datetime as dt

from pkg_bloomberg.CLS_Terminal import BBG_terminal



def get_bbg_data():
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Sending signal bloomberg...")
    bbg = BBG_terminal()
    bbg.find_window()
    time.sleep(3)
    bbg.send_signal()
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Signal sent to bloomberg...")


schedule.every().day.at("22:14:30").do(get_bbg_data)
schedule.every().day.at("22:15:00").do(get_bbg_data)
schedule.every().day.at("22:16:00").do(get_bbg_data)




now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
print(f"{now}: Starting thread...")

while True:
    schedule.run_pending()
    time.sleep(5) # wait 5 seconds