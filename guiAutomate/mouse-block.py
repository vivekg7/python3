# script to block mouse b/w 100,100
import pyautogui

pyautogui.FAILSAFE = False

while True:
    x, y = pyautogui.position()
    if x > 10 :
        x = 1
    if y > 10 :
        y = 1
    pyautogui.moveTo(x, y)
