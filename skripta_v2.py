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

omjer_stranica = 0
omjer_stranica1 = 0

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


pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
myScreenshot = pyautogui.screenshot()
myScreenshot.save('image2.png')
img = cv2.imread('image2.png')

cropped_image = img[975:1000, 1800:1856]
cropped_image = cv2.resize(cropped_image, (375, 113))

cropped_image1 = img[384:408, 1702:1760]
cropped_image1 = cv2.resize(cropped_image1, (620, 200))

cv2.imwrite("image3.png", cropped_image)
img2 = cv2.imread('image3.png')
cv2.imwrite("image4.png", cropped_image1)
img3 = cv2.imread('image4.png')


text = pytesseract.image_to_string(img2)
text1 = pytesseract.image_to_string(img3)

pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
sleep(0.5)
pyautogui.press("f9")
sleep(0.5)

while omjer_stranica1 <= 1 and omjer_stranica <=1:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('image2.png')
    img = cv2.imread('image2.png')
    cropped_image1 = img[384:408, 1702:1760]
    cropped_image1 = cv2.resize(cropped_image1, (620, 200))
    cv2.imwrite("image4.png", cropped_image1)
    img3 = cv2.imread('image4.png')
    
    try:
        text1 = pytesseract.image_to_string(img3)
        print(text1)
        omjer_stranica1 = eval(text1)
        print(omjer_stranica1)
    except NameError:
        print("ne mogu ocitati broj, NameError")
    except SyntaxError:
        print("ne mogu ocitati broj, SyntaxError")   
    
    while omjer_stranica < 0.99:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('image2.png')
        img = cv2.imread('image2.png')

        
        cropped_image = img[975:1000, 1800:1856]
        cropped_image = cv2.resize(cropped_image, (375, 113))
              
        cv2.imwrite("image3.png", cropped_image)
        img2 = cv2.imread('image3.png')
                
        try:
            text = pytesseract.image_to_string(img2)      
            print(text)
            omjer_stranica = eval(text)
            print(omjer_stranica)           
        except NameError:
            print("ne mogu ocitati broj, NameError")
        except SyntaxError:
            print("ne mogu ocitati broj, SyntaxError")   
            
        pyautogui.typewrite('A', interval=0.1)
        sleep(0.1)
        pyautogui.press("return")
        sleep(0.05)
        
    if omjer_stranica > 0.99:
        omjer_stranica = 0
            
    pyautogui.press("f10")
    sleep(0.5)
    pyautogui.click(x=1162, y=772, clicks=1, interval=1, button='left')
    sleep(2)
    pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
    sleep(0.5)
    pyautogui.moveTo(1551, 551)
    sleep(0.5)
    pyautogui.scroll(1000000)
    sleep(0.5)
    pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
    sleep(0.5)
    pyautogui.press("f9")
    sleep(0.5)
        
    if omjer_stranica1 == 1.0:
        print("Unos je gotov!")
        omjer_stranica1 = 2
        if omjer_stranica1 == 2:
            print("Skripta je završila!")
        

