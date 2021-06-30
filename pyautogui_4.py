# from web / PyAutoGUI’s documentation!

import pyautogui

#       Get the size of the primary monitor.
# screenWidth, screenHeigh = pyautogui.size()
# print(screenWidth,'\t',screenHeigh)


#       Get the XY position of the mouse.
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX,'\t',currentMouseY)


# pyautogui.moveTo(100,150) # Move the mouse to XY coordinates

# pyautogui.click() # Move the mouse to XY coordinates

# pyautogui.click(100,200) # Move the mouse to XY coordinates and click it.

# pyautogui.move(0,10) # Move mouse 10 pixels down from its current position.

# pyautogui.doubleClick() # Double click the mouse.

# pyautogui.moveTo(500,500,duration=2,tween=pyautogui.easeInOutQuart) # Use tweening/easing function to move mouse over 2 seconds.

# pyautogui.write('Hello world',interval=0.25) # type with quarter-second pause in between each key

# pyautogui.sleep(3)
# pyautogui.press('enter') # Press the enter key. All key names are in pyautogui.KEY_NAMES

# pyautogui.keyDown('shift') # Press the Esc key. All key names are in pyautogui.KEY_NAMES

# pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.

# pyautogui.keyUp('shift') # Let go of the Shift key.

# pyautogui.sleep(5)
# pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

# pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

#------------------------
# This example drags the mouse in a square
# spiral shape in MS Paint (or any graphics drawing program):

'''
pyautogui.sleep(5)
distance = 200
while distance > 0:
    pyautogui.drag(distance,0,duration=0.5) # move right
    distance -=5
    pyautogui.drag(0,distance,duration=0.5) # move down
    pyautogui.drag(-distance,0,duration=0.5) # move left
    distance -=5
    pyautogui.drag(0,-distance,duration=0.5)
'''