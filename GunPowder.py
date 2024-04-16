import pyautogui
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

print('Init Bot-Start')

def openJ():
    print('Opening Inventory')
    pyautogui.press('j')
    time.sleep(1)

def clickOnScreen(x, y):
    print('Click on screen')
    pyautogui.click(x=x, y=y)


def check_if_ark_is_running():
    try:
        ark_window = pyautogui.getWindowsWithTitle('ARK')[0]
        ark_window.activate()
        return True
    except IndexError:
        return False
    
def pressKey(key, amount):
    for i in range(amount):
        pyautogui.press(key) 
        time.sleep(0.1)

def startCrafting():
    print('Start Crafting...')
    time.sleep(0.5)
    openJ()
    time.sleep(0.5)
    clickOnScreen(1050, 450)
    time.sleep(0.2)
    pressKey('a', 10)
    pyautogui.press('esc')

def walkUp(duration):
    print("Walking Up...")
    keyboard.press('w')
    time.sleep(duration)
    keyboard.release('w')

def walkLeft():
    print("Walking left...")
    keyboard.press('a')
    time.sleep(1.2)
    keyboard.release('a')

def walkBack():
    print("Walking backwards...")
    keyboard.press('s')
    time.sleep(0.4)
    keyboard.release('s')

def walkRight():
    print("Walk left...")
    keyboard.press('d')
    time.sleep(1.2)
    keyboard.release('d')

def startShitRn():
    for _ in range(11):
        startCrafting()
        time.sleep(0.29)
        walkUp(0.29)
        time.sleep(0.29)
    time.sleep(1)
    walkLeft()
    for _ in range(11):
        startCrafting()
        time.sleep(0.4)
        walkBack()
        time.sleep(0.4)
    time.sleep(1)
    walkRight()
    time.sleep(10)
    startShitRn()

if check_if_ark_is_running:
    print('ARK is running')
    pyautogui.getWindowsWithTitle('ARK')[0].activate()
    time.sleep(1)
    startShitRn()
else:
    print('ARK is not running')