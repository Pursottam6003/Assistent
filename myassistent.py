 
from logging import exception
import webbrowser
from xmlrpc.client import DateTime
import pyttsx3 #for text to speech 
import speech_recognition as sr   # for speech to text 
import pyaudio  # audio
import os # importing os 
import time 
from time import gmtime,strftime
from datetime import date
import datetime
import csv 

engine=pyttsx3.init()
voices =engine.getProperty('voices')
rate=engine.setProperty('rate',150)
engine.setProperty('volume',0.9)

def intro():
    #speaking task 
    # tell user about assistent 
    # print what they can do for you 
    # little background sound for 5 secs 
    # space left for audio part 
    print('Starting the assistent...\n')
    #will add some virtual effects in future 
    print('Hello Sir...')
    greet()
    engine.setProperty('voice',voices[1].id)
    engine.say('Hello Mr CEO ! Sir I am ProBot-001 , your virtual personal assistent \n')
    engine.say('Here I am happy to help you please tell me how i can help you ?\n')
    engine.say('Please look on the screen  some commands and tips i can perform happily')
    print('1.Asking TIme \t 2. Greeting \t 3. Daily Task \t 4.Chanting Bhajans\t 5. Reading News\t 6.Opening Social Media')
    print('7.Playing Games \t 8. Emails to anyone\t 9. Opening Google Meet  \t 10.Sending Messages  11. And lot more ! \t ')
    
    engine.runAndWait()


def close_me():
    engine.say('closing sir one momment please ...')
    engine.stop()

def playmusic():
    #plays the music or seach in web about the specified name 
    myvoice = sr.Recognizer()
    with sr.Microphone() as source :
        print('Listening')
        myvoice.pause_threshold=0.9
        audio=myvoice.listen(source)
    #trying to reconginse the voice 

    try:
        print('getting results...')
        engine.say('searching on the web')
        query= myvoice.recognize_google(audio,'language=en-in')
        print(f"user said : {query}")
    except exception as e :
        engine.say('sorry! did not get you ?')
        print('Please repeat')
        return "None"
    
    return query


def find_all(name,path):
    result=[]# creating an empty list 
    try: #may be get some exception in getting the specified file so covering into try catch block 

        for root,dirs,files in os.walk(path):
            if name in files:
                result.append(os.path.join(root,name))
        
        return result 
    
    except exception as e:
        print(e)
        engine.say(f"cannot able to seach the {name} in the specified directory !")
        engine.say('throws exception:'+e)


def tell():
    
    speaker=pyttsx3.init()
    speaker.say('what would like to search')
    speaker.runAndWait()
    speaker.stop()



def open_something():
    tell()
    print("What whould you like to open !")

    speak=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        speak.pause_threshold=1 # pause for sometime 
        audio=speak.listen(source)

    try: 
        print('Recongnising...')
        query = speak.recognize_google(audio,language='en-in')
        query=query.lower()
        print(f"user said: {query}\n")
        if 'work' in query :
            work()
            return "None"
        else :

            url = "https://www.google.com.tr/search?q={}".format(query)
            webbrowser.open_new_tab(url)
            return "none"
        
    
        
    except Exception as e :
        print(e)
        engine=pyttsx3.init()
        engine.say('sorry sir could you please repeat once again')
        print('sorry ! did nt get you ??')
        return "None"
    return query

def read():
    #read something for you like new article. 
    pass 


def work():
    #now we are creating the application that used in our daily work 
    tell()
    mywork=sr.Recognizer()
    with sr.Microphone() as source :
        print('listening')
        mywork.pause_threshold=1
        audio=mywork.listen(source)
    
    try:
        print('getting results...')
       
        task=mywork.recognize_google(audio,language='en-in')
        print(type(task))
        task=task.lower()
        print(f"user said : {task}")

        if 'youtube' in task :
          
            webbrowser.open_new_tab('https://www.youtube.com/')
            return "none"
        
        elif 'linkdin' in task:
            webbrowser.open_new_tab('https://www.linkedin.com/')
            return "none"
        
        elif 'moodle ' in task:
            webbrowser.open_new_tab('http://nitap.co.in/moodle/')
            return "none"

        elif 'facebook' in task :
           
            webbrowser.open_new_tab('https://www.facebook.com/')
            return "none"
        
        elif 'google meet' in task:
            #may ask the code also 
           
            webbrowser.open_new_tab('https://meet.google.com/landing?authuser=1')
            return "none" 
        
        elif 'whatsapp' in task:
           
            webbrowser.open_new_tab('https://web.whatsapp.com/')
            return "none"
        
        elif 'webex' in task:
            webbrowser.open_new_tab('https://nitap.webex.com/wbxmjs/joinservice/sites/nitap/meeting/download/3e0f81c74f544a6d9ebc1b2a60d47e68?siteurl=nitap&MTID=mfaad87feb04e2f95b3f227d5ed7dbc58')
            return "none"
        elif 'zoom' in task:
          
            webbrowser.open_new_tab('https://zoom.us/join')
            return "none"
        
        elif 'jitsi' in task:
          
            webbrowser.open_new_tab('https://meet.jit.si/')
            return "none"

        else :
            link ="https://www.google.com.tr/search?q={}".format(task)
            webbrowser.open_new_tab(link)
            return "none"
        
    except exception as e :
        engine.say('sorry! did not get you ?')
        print('Please repeat')
        return "None"

def greet():
    print("Todays Date")
    
    date= str(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    print(date)
    
    mytime = datetime.datetime.now().hour
     
    if mytime <1:
        print('Good Hardworking Sir ! But its time to relax and sleep')
        engine.say('Ohh ! Sir please sleep tommrow you have meeting')
        engine.say('Good Night Sir have sweet dreams !')
    
    elif mytime >6 and mytime <12 :
        engine.say('Good Moring Sir')
        engine.say('Here is your morning quotes from my side !')
        print('One small positive thought can change your whole day')
        engine.say('One small positive thought can change your whole day')

    elif mytime >12 and mytime <=15:
        engine.say('Good Afternoon Sir')
    elif mytime >15 and mytime <20 :
        engine.say('Good Evening Sir')
    else :
        engine.say('Keep Growing Sir! keep Going !')

def sendmail():
    pass 

def writemessage_whatapp():
    num=sr.Recognizer()
    with sr.Recognizer() as source:
        print('listening')
        num.pause_threshold=1
        audio=num.listen(source)
    
    try: 
        print('getting results')
        contact=num.recognize_google(audio,language='en-in')
        contact=contact.lower()
        print(f"searching {contact}")
        mydict ={'ashi':8979218038, 'akash':9521877470,'ankit':6287083304,'bomge':8258976628,'chandrashekhar':8448052150,'chinmayee':7337315154,'dev':9407454771,'dolly gautam':9521429017,'dankya baam':8414911434,'gaurav':6201312718}

        
        for name in mydict.items():
            if contact in name :
                number=mydict['contact']
            
        
                
    

def save_audio():
    pass
if __name__== "__main__":
    
    # find=find_all('fav_str.cpp',"C:\\Users\\user\\Desktop\\codechef\\Codedrive")
    # print(find)
    #intro()
    open_something()
  