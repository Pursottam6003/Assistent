#import the file 

import pyttsx3 

engine=pyttsx3.init()
voices=engine.getProperty('voices')
voices=engine.setProperty('voice',voices[1].id)
engine.save_to_file("Hello pursottam , you can save the file into the audio format and listen when you get bored ! Thank You ",'audio.mp3')
engine.runAndWait()
engine.stop()
