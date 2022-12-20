import pyautogui
import time

print('Keeping alive...')
while True:
    pyautogui.press('volumedown')
    time.sleep(200)
    pyautogui.press('volumeup')
    time.sleep(200)