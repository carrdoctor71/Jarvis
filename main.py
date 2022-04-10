# 
import speech_recognition as user_talking # library to recognize user speach
import pyttsx3 # library for speach back to user
import pywhatkit # library to search and play youtube videos
import wikipedia # library for doing research
import datetime # library to pull the current time

hear = user_talking.Recognizer() # voice recognition engine
engine = pyttsx3.init() # speech engine

def speak(text): # funtion for all repeated funtions of speaking commands for jarvis
    engine.say(text)
    engine.runAndWait()

run=True # controls run loop and shuts down jarvis when you say goodnight to it
while run:
    try:    
        with user_talking.Microphone() as source: # calls microphone from computer to hear user speach
            print('Jarvis waiting to be addressed...') # message on debug screen to show its wating
            voice = hear.listen(source)
            # accesses google speach recognition to convert user language to string
            user_speaking = hear.recognize_google(voice)
            user_speaking = user_speaking.lower() # making all incoming speak lower case to derisk interpretation issues
            print(user_speaking) # confirmation of what was herd for debug
            # since users say the same thing in various ways I have searched for just key words
            # within the user speacking to trigger a response to decrease needed sentence accurancy 
            # to run funtions and order of words also will not matter with this format
            if "jarvis" and "good morning" in user_speaking:
                speak("Good morning Sir")
                print("Good morning Sir")
            elif "jarvis" and "what" and "time" in user_speaking:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak("Sir the current time is " + time)
                print(time) # debug screen feedback
            elif "jarvis" and "research" in user_speaking:
                topic = user_speaking.replace("jarvis research","")
                research = wikipedia.summary(topic,sentences=3) # keeps research results short
                speak("Of course sir, here is what I found on " + topic + "  " + research)
                print("Jarvis researching") # debug screen feedback
            elif "jarvis" and "play" in user_speaking:
                song = user_speaking.replace("jarvis play","")
                speak("Of course Sir, I will play " + song)
                pywhatkit.playonyt(song)
                print("playing: " + song) # debug screen feedback
            elif "jarvis" and "heat" and "down" in user_speaking:
                speak("Getting a bit warm Sir? I have turned the heat down")
            elif "jarvis" and "heat" and "up" in user_speaking:
                speak("Feeling a bit chilled Sir? I have turned the heat up")
            elif "jarvis" and "goodnight" in user_speaking:
                speak("Goodnight Sir")
                run = False # shuts down program by voice command
                print("Jarvis Powered Down") # debug screen feedback
            else: # feedback to user that jarvis couldn't interpreate there request
                speak("What was that Sir?")
    except:
        pass