import pyautogui
import win32api
import win32gui
import win32con
import keyboard
import time
import winsound
from groupNameExtraction import vratiImeGrupe
from scroller import messageScraping2
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
from PIL import Image
# const
startX = int(config['Miksa']['startX'])
startY = int(config['Miksa']['startY'])
width = int(config['Miksa']['width'])
height = int(config['Miksa']['height'])
scrollHeight = int(config['Miksa']['scrollHeight'])
leftX = int(config['Miksa']['leftX'])
leftY = int(config['Miksa']['leftY'])
leftX2 = int(config['Miksa']['leftX2'])
leftY2 = int(config['Miksa']['leftY2']) 
testX = int(config['Miksa']['testX'])
testY = int(config['Miksa']['testY'])
purple = (134, 115, 252)
gray=(117, 124, 132)
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
    #print(pix[testX,testY])
    return pix[testX,testY]!=purple and pix[testX,testY]!=gray

def spustiDole():
    scroll(-100000000)
    click(leftX2,leftY2)

def vratiGore():
    scroll(100000000)
    #click(leftX,leftY)


print(win32api.GetComputerName())
time.sleep(2) 
im = pyautogui.screenshot('screenshot.png',region=(startX,startY,width,height))

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
        # print("USO")
        #click(leftX,leftY)
        im=pyautogui.screenshot('screenshot.png',region=(startX,startY,width,height))
        if nemaPoruka(im):
            spustiDole()
            break
        time.sleep(2)
        click(leftX,leftY)
        # click(rightX,rightY)
        time.sleep(2)
        imeGrupe = vratiImeGrupe(im)
        print(imeGrupe)
        messageScraping2(imeGrupe)
        winsound.Beep(1000, 1000)
        click(leftX,leftY)
        scroll1()
    time.sleep(10)
    
