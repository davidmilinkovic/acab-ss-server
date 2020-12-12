import win32api, win32con, win32gui, winsound
from pynput.keyboard import Key, Listener, KeyCode, Controller as KController
from pynput.mouse import Button, Controller
import time
from win32con import *
import clipboard

xCursor = 660
yCursor = 950

radi = True

mouse = Controller()
keyboard = KController()


def isCursorInsert():
    return win32gui.GetCursorInfo()[1] == 65541


def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.ReleaseDC(i_desktop_window_id, i_desktop_window_dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def messageScraping():
    global radi
    win32api.SetCursorPos((xCursor, yCursor))
    brPoruka = 0
    while brPoruka != 15:
        while isCursorInsert() == False:
            time.sleep(0.00005)
            win32api.mouse_event(MOUSEEVENTF_WHEEL, xCursor, yCursor, 3, 0)
            time.sleep(0.00005)
            mouse.move(-40, 0)
            time.sleep(0.00005)
            mouse.move(40, 0)

        # winsound.Beep(1000, 100)

        for i in range(3):
            mouse.press(Button.left)
            mouse.release(Button.left)

        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        # time.sleep(0.01)
        text = clipboard.paste()
        print(text)

        while isCursorInsert():
            time.sleep(0.00005)
            win32api.mouse_event(MOUSEEVENTF_WHEEL, xCursor, yCursor, 3, 0)
            time.sleep(0.00005)
            mouse.move(-20, 0)
            time.sleep(0.00005)
            mouse.move(20, 0)

        brPoruka += 1
    winsound.Beep(1000, 500)

def messageScraping2():
    global radi
    win32api.SetCursorPos((xCursor, yCursor))
    brPoruka = 0
    while brPoruka != 15:
        while isCursorInsert() == False:
            time.sleep(0.00005)
            win32api.mouse_event(MOUSEEVENTF_WHEEL, xCursor, yCursor, 1, 0)
            time.sleep(0.00005)
            mouse.move(-20, 0)
            time.sleep(0.00005)
            mouse.move(20, 0)

        winsound.Beep(1000, 100)

        for i in range(3):
            mouse.press(Button.left)
            mouse.release(Button.left)

        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        time.sleep(0.1)
        text = clipboard.paste()
        print(text)

        while isCursorInsert():
            time.sleep(0.00005)
            win32api.mouse_event(MOUSEEVENTF_WHEEL, xCursor, yCursor, 1, 0)
            time.sleep(0.00005)
            mouse.move(-20, 0)
            time.sleep(0.00005)
            mouse.move(20, 0)

        brPoruka += 1
    winsound.Beep(1000, 500)

def on_release(key):
    global radi
    if key == KeyCode.from_char('s'):
        print("Pocinjemo")
        winsound.Beep(261, 300)
        winsound.Beep(326, 300)
        winsound.Beep(392, 300)
        winsound.Beep(326, 300)
        winsound.Beep(261, 600)
        radi = True
        messageScraping()
    if key == KeyCode.from_char('a'):
        print("Pocinjemo")
        winsound.Beep(261, 300)
        winsound.Beep(326, 300)
        winsound.Beep(392, 300)
        winsound.Beep(326, 300)
        winsound.Beep(261, 600)
        radi = True
        messageScraping2()
    if key == KeyCode.from_char('c'):
        radi = False
    if key == KeyCode.from_char('i'):
        print(isCursorInsert())
    if key == KeyCode.from_char('g'):
        print(get_pixel_colour(xCursor, yCursor))
    if key == Key.esc:
        return False


with Listener(on_release=on_release) as listener:
    listener.join()