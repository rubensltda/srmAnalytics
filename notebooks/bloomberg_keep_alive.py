import win32gui
import win32con
import time
from pynput.keyboard import Key, Controller
import win32gui
import random

def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst

appwindows = get_app_list()

bbg_keywords = ['New Tab', 'TOP Top News', 'SWPM Swap Manager', 'BTMM TREASURY & MONEY MARKETS', 'ECO Economic Calendars', 'CRVF Curve Finder', 'WEI World Equity Indices']

#print(appwindows)

found_window = False
for bk in bbg_keywords:
    for window in appwindows:
        window_title = window[1]
        
        if bk in window_title:
            print(f"{bk}---{window[0]}---{window[1]}")
            found_window = True
            window_id = window[0]

print(window_id)




win32gui.SetForegroundWindow(window_id)



################################################################################
list_commands = ['TOP BR', 'TOP BR', 'ECO BR', 'ECO US', 'BTMM BZ']

keyboard = Controller()
num = random.randint(0, len(list_commands)-1)
command = list_commands[num]
#print(f'Sending {command}')

#keyboard.type("T")
time.sleep(2)


keyboard.press(Key.ctrl_l)
time.sleep(0.05)
keyboard.press("t")
time.sleep(0.05)
keyboard.release("t")
time.sleep(0.05)
keyboard.release(Key.ctrl_l)


# Send command
#####################################################
time.sleep(3)
keyboard.type(command)
time.sleep(3)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
# Alternative to send character by character
#####################################################
# command_chars = [*command]
# print(command_list)
# for c in command_chars:
#     time.sleep(random.randint(1,3))
#     keyboard.type(c)
        
time.sleep(3)

keyboard.press(Key.ctrl_l)
time.sleep(0.05)
keyboard.press("w")
time.sleep(0.05)
keyboard.release("w")
time.sleep(0.05)
keyboard.release(Key.ctrl_l)
