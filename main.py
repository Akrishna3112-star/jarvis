import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
# from openai import OpenAI
# pip install pocketsphnix

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say (text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key= "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",
)
    completion  = client.chat.completions.create(
    model="gpt-4o",  
    messages=[
        {"role": "system", "content": "you ara avirtual assistant named jarvis skilled in genral tasks like alexa nad google cloud"},
        {"role": "user","content":command}
    ]
)

    return completion.choices[0].message.content


def processcommand(c):
    if "open google"in c.lower():
        webbrowser.open("https://google.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif"open gemini" in c.lower():
        webbrowser.open("https://gemini.google.com/app")
    

    elif c.startswith("play"):
        try:
            song = c.split(" ")[1].lower()
            print(f"User requested: {song}")
            link = musiclibrary.music[song]
            print(f"Opening: {link}")
            webbrowser.open(link)
        except IndexError:
            speak("Please say the song name after 'play'.")
        except KeyError:
            speak(f"Sorry, I couldn't find {song} in your library.")

    
    
    elif "exit" in c.lower() or "quit" in c.lower():
        speak("Goodbye!")
        exit()

    else:
        output = aiProcess(c)
        speak(output)
    



if __name__ == "__main__":
    speak("Initializing Jarvis...")
while True:

#Listen for the wake word "Jarvis"

#obtain audio from the microphone

    r = sr.Recognizer()

    print("recognizing...")

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source,timeout=5, phrase_time_limit=5)
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            speak("Ya how may i help you")
        #Listen for command

        with sr.Microphone() as source:

            print("Jarvis Active...")
            audio = r.listen(source)
            command = r.recognize_google(audio)

            processcommand(command)

    except Exception as e:
        print("  error;(0)".format(e))
        