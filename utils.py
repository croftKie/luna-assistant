import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print("running")
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()  
    with sr.Microphone() as source:   
        print("Now listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Deciphering")   
        query = r.recognize_google(audio, language ='en-gb')
        print("You Said: " + query)
    except Exception as e:
        print(e)
        print("Did not hear anything") 
        return "None"
    return query