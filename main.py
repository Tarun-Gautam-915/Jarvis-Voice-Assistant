import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "aa4cff7062a04bafb5154639a754f0d0"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Check if the request was successful
        if r.status_code == 200:
            data = r.json()  
            articles = data.get("articles", [])
            
            # Print the top headlines
            speak("Top News Headlines:\n")
            for article in articles:
                speak(article['title'])
            else:
                speak(f"Failed to fetch news: {r.status_code}")


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        # recognize speech using Google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2)

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))