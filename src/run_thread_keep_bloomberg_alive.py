import schedule
import time
import datetime as dt

from pkg_bloomberg.CLS_Terminal import BBG_terminal


def get_bbg_data():
    try:
        now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        print(f"{now}: Sending signal bloomberg...")
        bbg = BBG_terminal()
        bbg.find_window()
        time.sleep(3)
        bbg.send_signal()
        now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
        print(f"{now}: Signal sent to bloomberg...")
    except:
        print("Could not send signal.")


schedule.every().day.at("00:30:00").do(get_bbg_data)
schedule.every().day.at("03:30:00").do(get_bbg_data)
schedule.every().day.at("06:30:00").do(get_bbg_data)
schedule.every().day.at("09:30:00").do(get_bbg_data)
schedule.every().day.at("12:30:00").do(get_bbg_data)
schedule.every().day.at("15:30:00").do(get_bbg_data)
schedule.every().day.at("18:29:00").do(get_bbg_data)
schedule.every().day.at("20:28:30").do(get_bbg_data)
schedule.every().day.at("22:32:30").do(get_bbg_data)
schedule.every().day.at("23:30:00").do(get_bbg_data)



now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
print(f"{now}: Starting thread...")

while True:
    schedule.run_pending()
    time.sleep(5) # wait 5 seconds