from pyautogui import *
import pyautogui
import keyboard
import time
import win32api, win32con
import sys, threading

time.sleep(2)

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

#Auto Cookie Clicker Function
def click(x,y):
      #Mouse 
      win32api.SetCursorPos((x,y))
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
      #time.sleep(0.1)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

      #Auto-Clicker
      while keyboard.is_pressed('q') == False:
        #Buildings
        if pyautogui.pixel(1315,300) [0] == 255:
          click(1315,300) 
        elif pyautogui.pixel(1355,358) [0] == 255:
          click(1355,358)  
        #Upgrades  
        elif pyautogui.pixel(1289,208) [1] == 18:
          click(1289,208)
        #Cookie Location     
        else:
          click(278,401)

  
#Cookie Clicker(x,y)
click(278,401)
       