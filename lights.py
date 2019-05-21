#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:55:23 2019

@author: spidey
"""

from phue import Bridge
from gtts import gTTS
import speech_recognition as sr
from tempfile import TemporaryFile
from pygame import mixer
import pyautogui
import re
from random import randint
import webbrowser
from time import sleep

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sleep(2)
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def assistant(command):
    if 'set the mood' in command:
        lights('romantic')
    elif 'sad' in command:
        lights('sad')
    elif 'heart broken' in command:
        lights('break')
    elif 'happy' in command:
        lights('happy')
    elif 'let there be light' in command:
        lights('up')
    elif 'see you' in command:
        lights('down')
        
def lights(action):
    b = Bridge('10.111.14.17')
    light_names = b.get_light_objects('name')
    if action=='up':
       light_names['Hue color lamp 1'].on = True
       light_names['Hue color lamp 1'].hue = 40000
       light_names['Hue color lamp 1'].saturation = 10
    if action=='down':
        command1 =  {'transitiontime' : 100, 'on' : False}
#b.set_light(1, command1)
#time.sleep(1)
#command2={'transitiontime' : 100, 'on' : True,'hue' :40000, 'bri':50}
        b.set_light(1, command1)
        print('done')
    if action=='happy':
        url='https://www.youtube.com/watch?v=ApXoWvfEYVU'
        webbrowser.open(url)
        sleep(1)
        pyautogui.click(733, 237)
        i=0
        while i<4:
            hues=[45000,40000,35000,30000]
            command={'transitiontime' : 100, 'on' : True,'hue' :hues[i], 'bri':50}
            b.set_light(1,command)
            sleep(10)
            i+=1
    if action=='sad':
       url='https://www.youtube.com/watch?v=au2n7VVGv_c'
       webbrowser.open(url)
       sleep(1)
       pyautogui.click(733, 237)
       i=0
       while i<4:
           hues=[40000,44000,40000,44000]
           command={'transitiontime' : 100, 'on' : True,'hue' :hues[i], 'bri':50}
           b.set_light(1,command)
           sleep(10)
           i+=1
    if action=='romantic':
        url='https://www.youtube.com/watch?v=2Vv-BfVoq4g&t=20s'
        webbrowser.open(url)
        sleep(1)
        pyautogui.click(733, 237)
        i=0
        while i<4:
            hues=[1000,10000,55000,60000]
            command={'transitiontime' : 100, 'on' : True,'hue' :hues[i], 'bri':50}
            b.set_light(1,command)
            print('excuted',i)
            sleep(10)
            i+=1
    if action=='break':
        url='https://www.youtube.com/watch?v=J9Zjgb03FMQ'
        webbrowser.open(url)
        sleep(1)
        pyautogui.click(733, 237)
        i=0
        while i<4:
            hues=[40000,41000,42000,44000]
            command={'transitiontime' : 100, 'on' : True,'hue' :hues[i], 'bri':50}
            b.set_light(1,command)
            sleep(10)
            i+=1
while True:
    try:
        assistant(myCommand())
        sleep(5)
    except KeyboardInterrupt:
        print('All done')
        # If you actually want the program to exit
        raise  
       
        