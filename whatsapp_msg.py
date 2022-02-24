from logging import exception
import speech_recognition as sr
import pyttsx3
import pywhatkit

speaker=pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)

def send_message(message):
    pywhatkit.sendwhatmsg(message,"Hello bro how are you",17,17)

def writemessage_whatapp():
    num=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        num.pause_threshold=1
        audio=num.listen(source)
    
    try: 
        print('getting results')
        contact=num.recognize_google(audio,language='en-in')
        contact=contact.lower()
        print(f"searching {contact}")
        mydict = {'ashi':8979218038, 'akash':+919521877470,'ankit':+916287083304,'bomge':+918258976628,'chandrashekhar':+918448052150,'chinmayee':+917337315154,'dev':+919407454771,'dolly gautam':+919521429017,'dankya baam':+918414911434,'gaurav':+916201312718}

        
        for name in mydict.items():
            if contact in name :
                number=mydict[contact]
                print(f"Messaging to {number}")
                speaker.say(f"sending message to {contact}")
                send_message(number)
                
    except exception as e :
        print(e)       


def send_msg():
    pywhatkit.sendwhatmsg("+919521877470","hello bro",17,25)
    return 0
if __name__=="__main__":
    #writemessage_whatapp()
    send_msg()