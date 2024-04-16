import pyautogui
import time
from pynput.keyboard import Key, Controller

print('Init Bot-Start')
keyboard = Controller()

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
    clickOnScreen(1000, 625)
    time.sleep(0.2)
    pressKey('a', 10)
    pyautogui.press('esc')

def walkRight():
    print("Walk right...")
    keyboard.press('d')
    time.sleep(0.37)
    keyboard.release('d')
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.release('w')

def walkLeft():
    print("Walking left...")
    keyboard.press('a')
    time.sleep(3)
    keyboard.release('a')
    

def RunThatShit():
    for _ in range(9):
        startCrafting()
        time.sleep(0.37)
        walkRight()
        time.sleep(0.37)
    time.sleep(1)
    walkLeft()
    time.sleep(60)
    RunThatShit()


if check_if_ark_is_running:
    print('ARK is running')
    pyautogui.getWindowsWithTitle('ARK')[0].activate()
    RunThatShit()
else:
    print('ARK is not running')