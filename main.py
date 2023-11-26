import pyttsx3
import speech_recognition as sr
import os
import vertexai
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION") 

vertexai.init(project=PROJECT_ID, location=LOCATION)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def create_session():
    chat_model = vertexai.language_models.ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    return chat

def response(chat, message):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    result = chat.send_message(message, **parameters)
    return result.text

def run_chat(query):
    chat_model = create_session()
    print(query)
    
    while True:      
        content = response(chat_model, query)
        print(f"AI: {content}")
        return content

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Good day Lendly! How are you today?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en')
        print("Lendly Said: {} \n".format(query))
    except Exception as e:
        speak("Say that again boss! ")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query=takeCommand().lower()
        ans=run_chat(query)
        print(ans)
        speak(ans)
        if 'jarvis dismiss' in query:
            speak("goodbye boss")      
            break



