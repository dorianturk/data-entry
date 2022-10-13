# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:43:15 2022

@author: Doria
"""

import cv2
import numpy as np
import pytesseract
import pyautogui
from time import sleep

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('image2.png')

print(img.shape) # Print image shape



pyautogui.press("win")
pyautogui.typewrite('isvu', interval=0.1)
pyautogui.press("return")
sleep(2)
pyautogui.typewrite('gtr456tgh', interval=0.1)
pyautogui.press("f10")
sleep(5)
pyautogui.press("f10")
sleep(2)
pyautogui.click(x=194, y=34, clicks=1, interval=1, button='left')
sleep(1)
pyautogui.click(x=260, y=331, clicks=1, interval=1, button='left')
sleep(0.5)
pyautogui.press("f7")
sleep(0.5)
pyautogui.click(x=1242, y=319, clicks=1, interval=1, button='left')
pyautogui.typewrite('2021', interval=0.1)
sleep(0.5)
pyautogui.press("f10")
sleep(5)










pyautogui.click(x=1000, y=1000, clicks=1, interval=1, button='left')
pyautogui.press('f7')



#[992:1009, 1800:1854]referada
myScreenshot = pyautogui.screenshot()
myScreenshot.save('image2.png')




"""
napravti duplu provjeru rasta stranice

"""