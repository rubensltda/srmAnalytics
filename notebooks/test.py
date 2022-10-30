import win32gui
import win32com
import time
from pynput.keyboard import Key, Controller
import win32gui
import random
import schedule
import datetime as dt

def send_command():
    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Sending command...")
    keyboard = Controller()

    # the next 2 lines are only necessary in BBg laptop
    #####################################################
    #shell = win32com.client.Dispatch("WScript.Shell")
    #shell.SendKeys('%')
    #####################################################
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    keyboard.type('')
    time.sleep(3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    win32gui.SetForegroundWindow('722506')
    
    time.sleep(3)
    keyboard.type('locked')
    time.sleep(3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
    print(f"{now}: Command sent...")


schedule.every().day.at("10:46:00").do(send_command)
schedule.every().day.at("10:46:20").do(send_command)
schedule.every().day.at("10:46:40").do(send_command)



now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
print(f"{now}: Starting thread...")

while True:
    schedule.run_pending()
    time.sleep(5) # wait 5 seconds