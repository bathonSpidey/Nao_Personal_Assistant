# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:58:21 2019

@author: abir
"""

import speech_recognition as sr
import time
import almath
from naoqi import ALProxy
from random import randint


ip='10.111.14.131' #The ip of the bot
#using speech recogniser to get the command
def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = get_command();

    return command

#function to introduce itself   
def intro(command):
    tts=ALProxy('ALTextToSpeech','10.111.14.131',9559)
    tts.setParameter('speed', 60)
    motion=ALProxy('ALMotion','10.111.14.131',9559)
    motion.setStiffnesses('RArm',1.0)
    names=['RShoulderPitch','RElbowYaw','RShoulderRoll','RElbowRoll']
    angleLists=[[-64.0*almath.TO_RAD],[-4.0*almath.TO_RAD],[-30.0*almath.TO_RAD,-11.0*almath.TO_RAD],[48.0*almath.TO_RAD,32.0*almath.TO_RAD,48.0*almath.TO_RAD,32.0*almath.TO_RAD]]
    times=[[1.0],[1.5],[1.7,2],[2.2,2.4,2.6,2.8]]
    isAbsolute=True
    motion.post.angleInterpolation(names,angleLists,times,isAbsolute)
    tts.say('Hello! I am BETH! Here to help')
    print 'done...'
    

    
a=get_command()
if 'who are you' in a:
    intro(a)    

    

