# mr_amitdas / GUI Automation with PyAutoGUI

import pyautogui

pos = pyautogui.position() # show mouse curser pointer on the screen
# print(pos)

siz = pyautogui.size() # show my full laptop screen size
# print(siz)

onscrn = pyautogui.onScreen(200, 50) # if this giving screen size is present return True if screen size is to high return False
# print(onscrn)


#       PAUSE function used, if im pause program in feu seconds
# pyautogui.PAUSE = 5
# pyautogui.moveTo(100,200)
# pyautogui.PAUSE = 5
# pyautogui.moveTo(10,10)


#       FILESAFE avoid any error
# pyautogui.FAILSAFE = False
# pyautogui.PAUSE = 5
# pyautogui.moveTo(0,0)
# pyautogui.PAUSE = 5
# pyautogui.moveTo(10,10)


# pyautogui.displayMousePosition() # display live mouse pointer on the screen

# pyautogui.move(100,0) # move cursar 100px to the current positions

# pyautogui.moveTo(100,100) # move cursar to giving positions


# pyautogui.moveTo(100,100,2,pyautogui.easeInQuad) # start slow, end fast [ mous, cursar movement ]

# pyautogui.moveTo(200,200,3,pyautogui.easeOutQuad) # start fast, end slow

# pyautogui.moveTo(300,300,4,pyautogui.easeInOutQuad) # start and end fast, slow in the middle

# pyautogui.moveTo(400,400,5,pyautogui.easeInBounce) # Bounce at the first

# pyautogui.moveTo(500,500,5,pyautogui.easeInElastic) # rubber band at the first


# pyautogui.sleep(3)
# pyautogui.drag(50,50) # drag 20px to 20px 
# pyautogui.dragTo(100,100) # drag giving positions


# pyautogui.sleep(5)
# pyautogui.click() # click anyware where my mouse pointer parent


# pyautogui.sleep(5)
# pyautogui.doubleClick(x=1861, y=63) # dobule click giving positions


# pyautogui.sleep(5)
# pyautogui.tripleClick(x=1861, y=63) # triple click giving positions


# pyautogui.rightClick()
# pyautogui.leftClick()


#       smillar to the click function, if im use only mousDown so does not click or open anything so we must use mouseUp with it so open anything or click anyware
# pyautogui.sleep(5)
# pyautogui.mouseDown()
# pyautogui.mouseUp()


#       scroll anything, if im give nagitive value so scroll up to down and if im give positive value so scroll down to up
# pyautogui.sleep(3)
# pyautogui.scroll(-1000) # Down
# pyautogui.sleep(2)
# pyautogui.scroll(1000) # Up


#       this two functions only use for os x or linux, windows not supported
# pyautogui.hscroll()
# pyautogui.vscroll()


# write and click anyware, and interval is, write slowly
# pyautogui.sleep(5)
# pyautogui.click() # click anything
# pyautogui.write('https://www.facebook.com',interval=0.10) # write anyware and im use interval so write slowly 0.10 this is time
# pyautogui.press('enter')


#       hot key use for ctrl=a, ctrl+s and so on, this type of argiment
# pyautogui.sleep(3)
# pyautogui.click()
# pyautogui.hotkey('ctrl', 'a')


# pyautogui.alert(text='Alert',title='alert box',button='ok') # show alert box on popop

# pyautogui.confirm(text='Alert',title='alert box',buttons=['ok', 'cancel']) # show same alert box with ok or cancel

# pyautogui.prompt(text='input',title='input box', default='username') # prompt, this show input box

# pyautogui.password(text='input',title='input box',mask='*') # password, show password box


#---------------- login method
'''
ask = pyautogui.confirm(text='Would you like to login?', title='Alert', buttons=['Yes', 'No'])

if ask == 'Yes':
    username = pyautogui.prompt(title='Username', text='please enter your username', default='username')
    password = pyautogui.password(title='Password', text='please enter your password', mask='*')
elif ask== 'No':
    alert = pyautogui.confirm(title='Alert', text='are you sure?', buttons=['Yes', 'No'])
    if alert == 'Yes':
        print("user chose not to login")
        quit()
    elif alert == 'No':
        print("Please try again!!")
        quit()

print(f"Username: {username}")
print(f"Password: {password}")
'''

# screenshot

# pyautogui.screenshot("screenshot.png") # take one SS on full screen
# pyautogui.screenshot("screenshot.png", region=(0,0,300,400)) # take SS on giving positions screen

#       take multipul SS on seperate screen
# i = 0
# while i <=3:
#     i+=1
    # pyautogui.screenshot(f"{i}.png", region=(0,0,300,400))