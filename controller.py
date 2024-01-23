import pyautogui

pyautogui.keyDown('right')
pyautogui.keyUp('left')

def signal(keyPressed=""):
    print("key pressed " , keyPressed)
    if keyPressed == "left" : 
        pyautogui.press('left')
 
    if keyPressed == "right" : 
        pyautogui.press('right')

 

 
