import pyautogui

pyautogui.keyDown('right')
pyautogui.keyUp('left')

def signal(keyPressed=""):
    print("key pressed " , keyPressed)
    if keyPressed == "left" : 
        pyautogui.keyDown('right')
        pyautogui.keyUp('left')
 
    if keyPressed == "right" : 
        pyautogui.keyDown('left')
        pyautogui.keyUp('right')

    if keyPressed == "s" : 
        pyautogui.keyUp('right')
        pyautogui.keyUp('left')
 

 
