import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   
engine.setProperty('rate', 170)  
engine.setProperty('volume', 1.0)  


def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that. Please say again.")
        return "None"
    return query.lower()

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you?")

    while True:
        query = take_command()

        
        if "hello" in query:
            speak("Hello! How are you?")

        
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        
        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        
        elif "search" in query:
            speak("What should I search for?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the results for {search_query}")

        
        elif "exit" in query or "stop" in query or "quit" in query:
            speak("Goodbye! Have a nice day.")
            break

