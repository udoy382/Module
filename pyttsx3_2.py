# pyttsx3 pypi / form web

import pyttsx3
from pyttsx3 import engine

'''
engine = pyttsx3.init()
engine.say('I will speak this text')
engine.runAndWait()
'''

""" RATE"""

engine = pyttsx3.init() # object creation

rate = engine.getProperty('rate') # getting details of current speaking rate
# print(rate) #printing current voice rate

# engine.setProperty('rate', 123) # setting up new voice rate

"""VOLUME"""

volume = engine.getProperty('volume') # getting to know current volume level (min=0 and max=1)
# print(volume) # printing current volume level

engine.setProperty('volume', 1.0) # setting up volume level  between 0 and 1

"""VOICE"""

voices = engine.getProperty('voices') # getting details of current voice

# engine.setProperty('voice', voices[0].id) # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id) # changing index, changes voices. o for male
# print(voices[1].id) # show voice detiels

# engine.say('Hello wrold!')
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

"""Saving Voice to a file"""

engine.save_to_file('Hello World', 'text.mp3')
engine.runAndWait()