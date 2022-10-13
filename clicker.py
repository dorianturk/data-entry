# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:36:28 2022

@author: Doria
"""
import cv2
import numpy as np
import pytesseract
import pyautogui
from time import sleep

omjer_stranica = 0
omjer_stranica1 = 0

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
myScreenshot = pyautogui.screenshot()
myScreenshot.save('image2.png')
img = cv2.imread('image2.png')

cropped_image = img[975:995, 1802:1856]
cropped_image = cv2.resize(cropped_image, (375, 113))

cropped_image1 = img[392:410, 1702:1760]
cropped_image1 = cv2.resize(cropped_image1, (620, 200))

cv2.imwrite("image3.png", cropped_image)
img2 = cv2.imread('image3.png')
cv2.imwrite("image4.png", cropped_image1)
img3 = cv2.imread('image4.png')


text = pytesseract.image_to_string(img2)
text1 = pytesseract.image_to_string(img3)


print(text)
print(text1)


#omjer_stranica = eval(text)
print(omjer_stranica)
#omjer_stranica1 = eval(text1)
print(omjer_stranica1)

try:
    text1 = pytesseract.image_to_string(img3)
    print(text1)
    omjer_stranica1 = eval(text1)
    print(omjer_stranica1)
    
    if omjer_stranica1 > 2 or type(omjer_stranica1) == 'str':
        omjer_stranica1 = 0.3
        print("krivo ocitana stranica", text1)
              
except NameError:
    print("ne mogu ocitati broj, NameError1")
    if text == "ees\n":
        omjer_stranica == 0.991
    if text == "Ti7\n":
        omjer_stranica == 0.991
except SyntaxError:
    print("ne mogu ocitati broj, SyntaxError")
    cropped_image6 = img[975:995, 1827:1856]
    cropped_image6 = cv2.resize(cropped_image6, (235, 120))
    
    cv2.imwrite("image6.png", cropped_image6)
    img6 = cv2.imread('image6.png')
    
    text4 = pytesseract.image_to_string(img6)

    if text4 == "1/4\n":
        print("stranica je 1/1")
        sleep(0.5)
        pyautogui.press("return")
        pyautogui.press("backspace")
        pyautogui.typewrite('A', interval=0.3)
        sleep(1)
        pyautogui.press("f10")
        sleep(3)
        text = "prazno"
        pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
        sleep(1)
        pyautogui.moveTo(1551, 551)
        pyautogui.scroll(1000000)
        pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
        
        sleep(0.5)
        pyautogui.press("f9")
        sleep(0.5)
    

pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
sleep(0.5)
pyautogui.press("f9")
sleep(0.5)

while omjer_stranica1 <= 1 and omjer_stranica <=1:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('image2.png')
    img = cv2.imread('image2.png')
    cropped_image1 = img[392:410, 1702:1760]
    cropped_image1 = cv2.resize(cropped_image1, (620, 200))
    cv2.imwrite("image4.png", cropped_image1)
    img3 = cv2.imread('image4.png')
    
    cropped_image2 = img[754:768, 1145:1187]
    cropped_image2 = cv2.resize(cropped_image2, (420, 140))

    cv2.imwrite("image4.png", cropped_image2)
    img4 = cv2.imread('image4.png')

    text2 = pytesseract.image_to_string(img4)
    
    try:
        text1 = pytesseract.image_to_string(img3)
        print(text1)
        omjer_stranica1 = eval(text1)
        print(omjer_stranica1)
        
        if omjer_stranica1 > 2 or type(omjer_stranica1) == 'str':
            omjer_stranica1 = 0.3
            print("krivo ocitana stranica", text1)
                  
    except NameError:
        print("ne mogu ocitati broj, NameError2")
        if type(text1) == 'str':
            omjer_stranica1 = 0.3
            print("procitao sam random string pa korigiram br str u br")
            
    except SyntaxError:
        print("ne mogu ocitati broj, SyntaxError2")   
    
    
    
    while omjer_stranica < 1 or omjer_stranica > 1.5:
        
            
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('image2.png')
        img = cv2.imread('image2.png')

        cropped_image = img[975:995, 1802:1856]
        cropped_image = cv2.resize(cropped_image, (375, 113))

        cropped_image3 = img[754:768, 1145:1177]
        cropped_image3 = cv2.resize(cropped_image3, (420, 140))
        
        cv2.imwrite("image5.png", cropped_image3)
        img5 = cv2.imread('image5.png')
                
        cv2.imwrite("image3.png", cropped_image)
        img2 = cv2.imread('image3.png')
        
        text3 = pytesseract.image_to_string(img5)
#1/1
        cropped_image6 = img[975:995, 1828:1856]
        cropped_image6 = cv2.resize(cropped_image6, (220, 120))
        
        cv2.imwrite("image6.png", cropped_image6)
        img6 = cv2.imread('image6.png')
        


        try:
            text = pytesseract.image_to_string(img2)      
            text4 = pytesseract.image_to_string(img6)
            
            if text == "ees\n":
                omjer_stranica == 0.991
            if text == "Ti7\n":
                omjer_stranica == 0.991
            
            if text4 == "a/1\n":
                print("stranica je 1/1")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
            
            if omjer_stranica > 2:
                omjer_stranica = 0.3
                print("krivo ocitana stranica", text)
            
            print(text)
            omjer_stranica = eval(text)
            
            print(omjer_stranica)           
        except NameError:
            print("ne mogu ocitati broj, NameError3")
            if text == "ees\n":
                print("ocitao sam random sto nevalja")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            if text == "Ti7\n":
                print("ocitao sam random sto nevalja")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            if text == "f2/72\n":
                print("ocitao sam random sto nevalja")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            if text == "Tl7\n":
                print("ocitao sam random sto nevalja")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            if omjer_stranica == 2/3:
                print("stranica je 3/3")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            print(omjer_stranica)
        except SyntaxError:
            print("ne mogu ocitati broj, SyntaxError3")
            if omjer_stranica == 0.9696969696969697:
                print("stranica je 33/33")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            if omjer_stranica == 0.984375:
                print("stranica je 64/64")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text == "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(100000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
               
            if omjer_stranica == 37/38:
                print("stranica je 38/38")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text == "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(100000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                
            
            if omjer_stranica == 57/58:
                print("stranica je 58/58")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
            
            if omjer_stranica == 47/48:
                print("stranica je 48/48")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5) 
                
            if omjer_stranica == 33/34:
                print("stranica je 34/34")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
            
            if omjer_stranica == 89/90:
                print("stranica je 90/90")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
           
            if omjer_stranica == 53/54:
                print("stranica je 54/54")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
            #1/1 str    
            cropped_image6 = img[975:995, 1827:1856]
            cropped_image6 = cv2.resize(cropped_image6, (235, 120))
            cv2.imwrite("image6.png", cropped_image6)
            img6 = cv2.imread('image6.png')
            
            text4 = pytesseract.image_to_string(img6)
                   
            if text4 == "1/4\n":
                print("stranica je 1/1")
                sleep(0.5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.typewrite('A', interval=0.3)
                sleep(1)
                pyautogui.press("f10")
                sleep(3)
                text4 = "prazno"
                pyautogui.click(x=1900, y=398, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
            #ubaci novi screen
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('image2.png')
            img = cv2.imread('image2.png')
            
            cropped_image7 = img[754:772, 1145:1177]
            cropped_image7 = cv2.resize(cropped_image7, (360, 180))
            cv2.imwrite("image7.png", cropped_image7)
            img7 = cv2.imread('image7.png')
            text5 = pytesseract.image_to_string(img7)
            
            if text5 == 'redu\n':
                print("nema unosa", text5)
                pyautogui.press("return")
                pyautogui.press("backspace")
                pyautogui.press("f10")
                sleep(3)
                pyautogui.click(x=1900, y=400, clicks=1, interval=1, button='left')
                sleep(1)
                pyautogui.moveTo(1551, 551)
                pyautogui.scroll(1000000)
                pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
                sleep(0.5)
                pyautogui.press("f9")
                sleep(0.5)
                text5 == "prazno"
           
        if omjer_stranica > 2:
            omjer_stranica = 0.1
            print("korigirao sam omjer stranica")
            
        
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('image2.png')
        img = cv2.imread('image2.png')
        
        if text3 == "redu\n":
            print(text3)
            pyautogui.press("return")
            pyautogui.press("backspace")
            pyautogui.press("f10")
            sleep(3)
            pyautogui.click(x=1900, y=400, clicks=1, interval=1, button='left')
            sleep(1)
            pyautogui.moveTo(1551, 551)
            pyautogui.scroll(1000000)
            pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
            sleep(0.5)
            pyautogui.press("f9")
            sleep(0.5)
            text3 == "prazno"
      
      
        if text == "ees\n":
            omjer_stranica == 0.991
        if text == "Ti7\n":
            omjer_stranica == 0.991 
      
        pyautogui.typewrite('A', interval=0.1)
        pyautogui.press("return")
        sleep(0.5)
                       
        
    if omjer_stranica == 1 or omjer_stranica == float(1):
        omjer_stranica = 0
            
    pyautogui.press("f10")
    
    if text2 == "lredy )\n" or text2 == "U red\n" or text == "Ti7A\n"  or text2 == "lredu |\n":
        print(text2)
        sleep(0.5)
        pyautogui.press("return")
        pyautogui.press("backspace")
        pyautogui.typewrite('A', interval=0.3)
        sleep(1)
        pyautogui.press("f10")
        sleep(3)
        text2 = "prazno"
        
    sleep(3)
    pyautogui.click(x=1162, y=772, clicks=1, interval=1, button='left')
    sleep(2)
    pyautogui.click(x=1900, y=400, clicks=1, interval=1, button='left')
    sleep(1)
    pyautogui.moveTo(1551, 551)
    pyautogui.scroll(1000000)
    pyautogui.click(x=503, y=473, clicks=1, interval=1, button='left')
    
    sleep(0.5)
    pyautogui.press("f9")
    sleep(0.5)
        
if omjer_stranica1 == 1:
    print("Unos je gotov!")
    omjer_stranica = 0
        
