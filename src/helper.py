import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import google.generativeai as genai
from gtts import gTTS
import os

GOOGLE_API_KEY= "AIzaSyAThfIZ_swfZhObXP_OeFpAnez08o2d_sE"
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

def voice_input():
    # Create a recognizer instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)  # Using Google Speech Recognition
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def text_to_speech(text):
    tts=gTTS(text=text)
    tts.save("speech.mp3")


def llm_model_object(user_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content(user_text)
    result=response.text
    
    return result
    