from pyautogui import *
import PIL
import pyautogui
import time
import keyboard
import win32api, win32con
import random

tile_colour = (17, 17, 17)
tile_x = (790, 900, 1020, 1150)
tile_y = 760

rgb_check = 0
time.sleep(2)
# tile 1: 660
# tile 2: 760
# tile 3: 860
# tile 4: 960

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1) # if we let go of the mouse immediately after the click would have no effect
    
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


def click_when_colour(x, y):
    
    try:
        try:
            pixel = pyautogui.pixel(x, y)
        except:
            pixel = pyautogui.pixel(x, y)
    except:
        try:
            pixel = pyautogui.pixel(x, y)
        except:
            pixel = pyautogui.pixel(x, y)

    if pixel[rgb_check] >= tile_colour[rgb_check] and pixel[rgb_check] <= tile_colour[rgb_check] + 10:
        click(x, y)

    
while keyboard.is_pressed('q') == False:
    click_when_colour(tile_x[0], tile_y)
    click_when_colour(tile_x[1], tile_y)
    click_when_colour(tile_x[2], tile_y)
    click_when_colour(tile_x[3], tile_y)
    
