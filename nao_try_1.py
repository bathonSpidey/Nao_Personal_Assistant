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
    '''motion.setStiffnesses('RArm',1.0)
    names=['RShoulderPitch','RElbowYaw','RShoulderRoll','RElbowRoll']
    angleLists=[[-64.0*almath.TO_RAD],[-4.0*almath.TO_RAD],[-30.0*almath.TO_RAD,-11.0*almath.TO_RAD],[48.0*almath.TO_RAD,32.0*almath.TO_RAD,48.0*almath.TO_RAD,32.0*almath.TO_RAD]]
    times=[[1.0],[1.5],[1.7,2],[2.2,2.4,2.6,2.8]]
    isAbsolute=True
    motion.post.angleInterpolation(names,angleLists,times,isAbsolute)'''
    response=['Hello,I am BETH! Basic Embodiment of a Talking Humanoid. Nice to meet you!','I am vengence, I am the night... I am BATMAN. hehe!', 'Spiderman, spiderman, your friendly neighborhood spiderman']
    b=randint(0, 2)
    #tts.say(response[b])   
    if b==0:
        motion.setStiffnesses('RArm',1.0)
        names=['RShoulderPitch','RElbowYaw','RShoulderRoll','RElbowRoll']
        angleLists=[[-64.0*almath.TO_RAD],[-4.0*almath.TO_RAD],[-30.0*almath.TO_RAD,-11.0*almath.TO_RAD],[48.0*almath.TO_RAD,32.0*almath.TO_RAD,48.0*almath.TO_RAD,32.0*almath.TO_RAD]]
        times=[[1.0],[1.5],[1.7,2],[2.2,2.4,2.6,2.8]]
        isAbsolute=True
        motion.post.angleInterpolation(names,angleLists,times,isAbsolute)
        tts.say(response[b])
    if b==1:
        motion.setStiffnesses('RArm',1.0)
        motion.setStiffnesses('LArm',1.0)
        namesR=['RShoulderPitch','RElbowYaw','RShoulderRoll','RElbowRoll','RWristYaw']
        angleListsR=[[89.7*almath.TO_RAD],[25.0*almath.TO_RAD],[-30.9*almath.TO_RAD],[88.5*almath.TO_RAD],[9.5*almath.TO_RAD]]
        timesR=[[1.0],[1.3],[1.5],[1.7],[2]]
        namesL=['LShoulderRoll','LElbowRoll','LShoulderPitch','LElbowYaw','LWristYaw']
        angleListsL=[[22.1*almath.TO_RAD],[81.4*almath.TO_RAD],[58.8*almath.TO_RAD],[15.5*almath.TO_RAD],[-36.8*almath.TO_RAD]]
        timesL=[[1.0],[1.3],[1.5],[1.7],[2]]
        isAbsolute=True
        motion.post.angleInterpolation(namesR,angleListsR,timesR,isAbsolute)
        motion.post.angleInterpolation(namesL,angleListsL,timesL,isAbsolute)
        tts.say(response[b])
    if b==2:
        motion.setStiffnesses('RArm',1.0)
        names=['RShoulderPitch','RElbowYaw','RShoulderRoll','RElbowRoll']
        angleLists=[[-64.0*almath.TO_RAD],[-4.0*almath.TO_RAD],[-30.0*almath.TO_RAD,-11.0*almath.TO_RAD],[48.0*almath.TO_RAD,32.0*almath.TO_RAD,48.0*almath.TO_RAD,32.0*almath.TO_RAD]]
        times=[[1.0],[1.5],[1.7,2],[2.2,2.4,2.6,2.8]]
        isAbsolute=True
        tts.say(response[b])
        
    #print 'done...'
    

    
a=get_command()
if 'who are you' in a:
    intro(a)    

    

