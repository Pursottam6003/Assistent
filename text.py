import pyttsx3 

engine=pyttsx3.init()   #object creation
#engine.say("hello pursottam sah i am your servent created by you")  #what need to say --> fast voice 

#rate=engine.getProperty('rate')
#print(rate)
rate=engine.setProperty('rate',70) # setting the property of rate function so that we can slow or fast 
print(rate)
#engine.say("hello is i am audible or not please response")  #slow voice 

# volume= engine.setProperty('volume')
# print(volume)

volume=engine.setProperty('volume',1.0)     # volume can be in between 0 and 1
#engine.say("now the voice is little dheere dheere!")



#voices 
voices =engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)  # for male voice 
engine.setProperty('voice',voices[1].id)
rate2=engine.setProperty('rate',150)
engine.say("Hello pursottam now my voice is changed hope its fine now, ask me anything")
engine.runAndWait()
engine.stop()