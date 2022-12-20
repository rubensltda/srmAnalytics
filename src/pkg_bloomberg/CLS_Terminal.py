import time
import random
from pynput.keyboard import Key, Controller
import win32gui
import win32com.client
import datetime as dt
#from notebooks.bloomberg_keep_alive import get_app_list

class BBG_terminal():
    
    def __init__(self):
        self.list_commands = ['TOP BR', 'TOP BR', 'ECO BR', 'ECO US', 'BTMM BZ']
        self.bbg_titles = ['New Tab', 'TOP Top News', 'SWPM Swap Manager', 'BTMM TREASURY & MONEY MARKETS', 'ECO Economic Calendars', 'CRVF Curve Finder', 'WEI World Equity Indices']
        self.opened_windows = []
        self.bbg_window_id = 0

    def window_enum_handler(self, hwnd, resultList):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
            resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

    def get_app_list(self, handles=[]):
        mlst=[]
        win32gui.EnumWindows(self.window_enum_handler, handles)
        for handle in handles:
            mlst.append(handle)
                
        #print(mlst)
        self.opened_windows = mlst


    def find_window(self):
        self.get_app_list()
        
        found_window = False
        for bk in self.bbg_titles:
            for window in self.opened_windows:
                window_title = window[1]
                
                if bk in window_title:
                    #print(f"{bk}---{window[0]}---{window[1]}")
                    found_window = True
                    self.bbg_window_id = window[0]

        if found_window == True:
            # the next 2 lines are only necessary in BBg laptop
            #####################################################
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            #####################################################
            win32gui.SetForegroundWindow(self.bbg_window_id)
        
        
    def send_signal(self):        
        
        if self.bbg_window_id != 0:
            
            keyboard = Controller()
            
            num = random.randint(0, len(self.list_commands)-1)
            command = self.list_commands[num]
            #print(f'Sending {command}')

            # Open a new tab in bloomberg
            #####################################################
            time.sleep(3)
            keyboard.press(Key.ctrl_l)
            time.sleep(0.05)
            keyboard.press("t")
            time.sleep(0.05)
            keyboard.release("t")
            time.sleep(0.05)
            keyboard.release(Key.ctrl_l)

            # Send command to bloomberg
            #####################################################
            # time.sleep(10)
            # keyboard.type(command)
            # time.sleep(3)
            # keyboard.press(Key.enter)
            # keyboard.release(Key.enter)
            # Alternative to send character by character
            #####################################################
            command_chars = [*command]
            #print(command_list)
            for c in command_chars:
                time.sleep(random.randint(1,3))
                keyboard.type(c)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            
            # Close tab
            #####################################################
            time.sleep(10)
            keyboard.press(Key.ctrl_l)
            time.sleep(0.05)
            keyboard.press("w")
            time.sleep(0.05)
            keyboard.release("w")
            time.sleep(0.05)
            keyboard.release(Key.ctrl_l)

            now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            #print(f"{now}: Signal sent to bloomberg...")
        
        else:
            now = dt.datetime.now().strftime("%Y-%m-%d %H.%M.%S")
            print(f"{now}: Bloomberg window not found...")


########################################################################################################################################################################
########################################################################################################################################################################
if __name__ == "__main__":
    bbg = BBG_terminal()
    bbg.find_window()
    time.sleep(3)
    bbg.send_signal()

