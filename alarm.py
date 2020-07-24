import os
import datetime
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 145)
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()


os. system('cls')
speak("What hour do you want the alarm to ring") 
timeH = int(input("What hour do you want the alarm to ring? "))
speak("What minute do you want the alarm to ring")
timeM = int(input("What minute do you want the alarm to ring? "))
speak("it is am or pm")
amPm = str(input("am or pm? "))

os. system('cls')
print("Waiting for alarm :-",timeH,":",timeM,amPm)
if (amPm == "pm"):
        timeH = timeH + 12
while True :
    if(timeH == datetime.datetime.now().hour and
        timeM == datetime.datetime.now().minute) :
    	# for i in range(5):
    	print("Time to wake up\n")
    	speak("time to wake up")
    	time.sleep(1)
    	for i in range(5):
    		print("press ctrl+c to stop")
	    	speak("time to wake up")
	    	break