import pyautogui
import win32api
import win32gui
import win32con
import keyboard
import time
from PIL import Image
# const
startX = 0
startY = 279
width = 374
height = 93
scrollHeight=150
rightX=500
rightY=300
leftX=80
leftY=300
leftX2=80
leftY2=1020
testX=340
testY=40
purple=(134, 115, 252)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def scroll1():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, leftX, leftY, -scrollHeight, 0)

def scroll(sH):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, leftX, leftY, sH, 0)

def nemaPoruka(im):
    pix=im.load()
    print(pix[testX,testY])
    return pix[testX,testY]!=purple

def spustiDole():
    scroll(-100000000)
    click(leftX2,leftY2)

def vratiGore():
    scroll(100000000)
    #click(leftX,leftY)


print(win32api.GetComputerName())
time.sleep(2) 
im = pyautogui.screenshot('screenshot.png',region=(startX,startY,width,height))
'''
#im = pyautogui.screenshot('screenshot.png',region=(startX,startY,width,height))
im=Image.open('screenshot.png')
pix=im.load()
print(im.size) 
print(pix[testX,testY])
'''
while True:
    #click(leftX,leftY)
    vratiGore()
    if keyboard.is_pressed('esc'):
        print("KRAJ2")
        break
    while True:
        time.sleep(2)
        if keyboard.is_pressed('esc'):
            print("KRAJ")
            break
        print("USO")
        #click(leftX,leftY)
        im=pyautogui.screenshot('screenshot.png',region=(startX,startY,width,height))
        if nemaPoruka(im):
            spustiDole()
            break
        time.sleep(2)
        click(leftX,leftY)
        click(rightX,rightY)
        time.sleep(2)
        #OVDE SE POZIVAJU PAJA I DAVID
        click(leftX,leftY)
        scroll1()
    time.sleep(10)
    
#myScreenshot = pyautogui.screenshot('screenshot.png',region=(startX,startY,width,height))
# myScreenshot.save(r'screenshot.png')
