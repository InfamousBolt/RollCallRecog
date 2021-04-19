# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:27:41 2020

@author: 91891
"""


import speech_recognition as sr
import playsound



r = sr.Recognizer()  
  
while(1):     
    try: 
          
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2) 
            audio2 = r.listen(source2) 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower()
            if "keshav" in MyText:
                print("Name called")
                playsound.playsound("C:/Users/91891/Downloads/distort1.wav")  
                print("Responded")
            if "88" in MyText:
                print("Roll called")
                playsound.playsound("C:/Users/91891/Downloads/distort2.wav")  
                print("Responded")
                
                
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("Your name probably isn't called yet") 