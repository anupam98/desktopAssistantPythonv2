import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia


#taking voice from the system
engine= pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
print(voices[0].id)
print(type(voices))
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

#speak function
def speak(text):
    '''This function takes text and return voice


    Args:
        text (_type_)= string
    
    '''
    engine.say(text)
    engine.runAndWait()

# speak("Hello I am a programmer how are you")



mic = sr.Microphone()
# print("Available microphones:")
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(f"{index}: {name}")



#speech recognition function
def takeCommand():
    """This function will recognize voice and return text

    """

    r=sr.Recognizer()
    with sr.Microphone(device_index=15) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,phrase_time_limit=5)
        print("we are here")
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query

print("Before welcome")

def wish_me():
    hour=(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir. How are you doing")
    elif 12 <= hour < 18: 
        text = "Good Afternoon sir. I am Jarvis. How can I Serve you?" 
    else: 
        text = "Good Evening sir. I am Jarvis. How can I Serve you?" 

    speak(" I am Jarvis, tell me sir how can i help you")


if __name__ == "__main__":
    

    wish_me()
    
    while True:
        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia")
            results= query.replace("wikipedia","")
            wikipedia.summary(results, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif "youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif "github" in query:
            speak("Opening github")
            webbrowser.open("github.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")


        elif "goodbye" in query:
            speak("Ok sir. I am always here for you. bye bye")
            exit()