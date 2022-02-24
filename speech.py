import speech_recognition as sr 
import pyttsx3
import webbrowser


def takecommand():
    #listene the audio 

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1 # pause for sometime 
        audio=r.listen(source)

    try: 
        print('Recongnising...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
       
        url = "https://www.google.com.tr/search?q={}".format(query)
        webbrowser.open_new_tab(url)
        #webbrowser.open_new_tab(query)
        


    except Exception as e :
        print(e)

        print('sorry ! did nt get you ??')
        return "None"
    return query

if __name__=="__main__":
    takecommand()
   