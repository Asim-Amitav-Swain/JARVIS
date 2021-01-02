import pyttsx3
import pdb
import speech_recognition as sr
import wikipedia
import datetime

pdb.set_trace()
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening !")
    
    speak("hy mom, whats up")
 
def takeCommand():
    #it take microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:  {query}\n" )
    
    except Exception as e:
        # print(e)
        print("Say That again please...")
        return "None"
    return query

engine.connect('started-word', takeCommand)



if __name__ == "__main__":
   wishMe()
   while True:
        query = takeCommand().lower()
   #Logic for Executing tasks based on query
   if 'wikipedia' in query:
       speak('Searching wikipedia...')
       query = query.replace("wikipedia", "")
       results = wikipedia.summary(query, sentences=2)
       speak("According to wikipedia")
       print(results)
       speak(results)