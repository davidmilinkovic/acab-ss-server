import win32api, win32con, win32gui, winsound 
from pynput.keyboard import Key, Listener, KeyCode, Controller as KController
from pynput.mouse import Button, Controller
import time
from win32con import *
import clipboard
import configparser
config = configparser.ConfigParser()
config.read("config.ini")

doleDesnoX = int(config['David']['doleDesnoX'])
doleDesnoY = int(config['David']['doleDesnoY'])
goreDesnoX = int(config['David']['goreDesnoX'])
goreDesnoY = int(config['David']['goreDesnoY'])

radi = True

mouse = Controller()
keyboard = KController()

def isCursorInsert():
    return win32gui.GetCursorInfo()[1] == 65541

poslednjaPoruka = {
    "Žaretovrođendan": "[ Saturday, December 12, 2020 6:05 PM ] Miksa Trajković: e",
    "POLOMLULU": "[ Saturday, December 12, 2020 6:05 PM ] Miksa Trajković: e",
    "MiksaTrajković": "[ Saturday, December 12, 2020 5:28 PM ] Miksa Trajković: /Stickers",
}
    
def messageScraping2(grupa):
    global radi
    delay = float(config['David']['delay'])
    prosaoPrviKrug = False
    poslednjaPorukaSada = ""
    while True:
        win32api.SetCursorPos((doleDesnoX, doleDesnoY))
        time.sleep(delay)
        mouse.press(Button.left)
        time.sleep(delay)
        y = doleDesnoY
        while y > goreDesnoY:
            mouse.move(0, -5)
            time.sleep(0.001)
            y -= 5
        win32api.SetCursorPos((goreDesnoX, goreDesnoY))
        time.sleep(delay)
        mouse.release(Button.left)
        time.sleep(delay)
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        time.sleep(delay)
        text = clipboard.paste()
        poruke = text.split('\r\n')
        if prosaoPrviKrug == False:
            poslednjaPorukaSada = poruke[len(poruke)-1]
            print("Poslednja poruka do sada: " + poslednjaPoruka[grupa])
            print("Poslednja poruka sada: " + poslednjaPorukaSada)
            prosaoPrviKrug = True
        zaustavi = False
        for poruka in reversed(poruke):
            if poslednjaPoruka[grupa] == poruka:
                zaustavi = True
                break
            print("Nova: " + poruka)
        if zaustavi:
            break
        win32api.SetCursorPos((doleDesnoX, doleDesnoY))
        time.sleep(delay)
        win32api.mouse_event(MOUSEEVENTF_WHEEL, doleDesnoX, doleDesnoY, (doleDesnoY-goreDesnoY)*2, 0)
        time.sleep(delay)
        mouse.press(Button.left)
        time.sleep(delay)
        mouse.release(Button.left)
    poslednjaPoruka[grupa] = poslednjaPorukaSada    
 