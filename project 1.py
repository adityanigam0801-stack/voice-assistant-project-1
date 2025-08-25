import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# -------- आवाज से बोलवाने के लिए Engine सेट करना --------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # [0] = Male, [1] = Female (try kar sakte ho)
engine.setProperty('rate', 170)  # बोलने की स्पीड
engine.setProperty('volume', 1.0)  # वॉल्यूम 0.0 से 1.0 तक

# टेक्स्ट को बोलने वाला फ़ंक्शन
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# -------- आवाज को सुनने वाला फ़ंक्शन --------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")  # हिंदी चाहिए तो "hi-IN" कर सकते हो
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that. Please say again.")
        return "None"
    return query.lower()

# --------- Main Program ---------
if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you?")

    while True:
        query = take_command()

        # 1) Hello का जवाब
        if "hello" in query:
            speak("Hello! How are you?")

        # 2) टाइम बताना
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        # 3) डेट बताना
        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        # 4) Google search
        elif "search" in query:
            speak("What should I search for?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the results for {search_query}")

        # 5) Exit command
        elif "exit" in query or "stop" in query or "quit" in query:
            speak("Goodbye! Have a nice day.")
            break
