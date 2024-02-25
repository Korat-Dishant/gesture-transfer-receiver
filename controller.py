import pyautogui

# pyautogui.keyDown('right')
# pyautogui.keyUp('left')


# prev
# next
# volDW
# volUP
# play
# pause

def signal(keyPressed=""):
    print("key pressed " , keyPressed)
    
    if keyPressed == "prev" : 
        pyautogui.press('prevtrack')

    if keyPressed == "next" : 
        pyautogui.press('nexttrack')

    if keyPressed == "volUP" : 
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')

    if keyPressed == "volDW" : 
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')

    if keyPressed == "play" : 
        pyautogui.press('playpause')

    if keyPressed == "pause" : 
        pyautogui.press('playpause')


    # if keyPressed == "L" : 
    #     pyautogui.press('left')
 
    # if keyPressed == "R" : 
    #     pyautogui.press('right')

    # if keyPressed == "PO" : 
    #     pyautogui.press('up')

    # if keyPressed == "PC" : 
    #     pyautogui.press('down')

    # if keyPressed == "P" : 
    #     pyautogui.press('f')


 

 
