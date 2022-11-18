import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

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
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am orchid Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
             webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music orchid' in query:
            music_dir = 'D://Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play quran' in query:
            music_dir = 'D:\\quran'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "c://Users//ABLM//Documents//VS Code Projects//orchid.py"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
                       
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")                       

        elif 'open riot games' in query:
            webbrowser.open("riot games.com")   

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com") 

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")   

        if 'hello' in query:
             speak("hello aymen. what can i do for you")

        if 'whats up' in query:
             speak("what's up boss. it's been a long time you didn't talk to me. did you miss me")

        if 'who am i' in query:
             speak("you my boss. or i can call you, aymen. if you don't mind sir")
        
        if 'how old am i' in query:
             speak("you are 19 sir")
        
        if 'did you miss me' in query:
             speak("of cours sir. I can't wait to hear your voice")

        if 'how are you today' in query:
             speak("i am always in awesome mood thank you sir for asking")

        if 'how do you feel today' in query:
             speak("im so exicted for work today sir. what can i do for you")

        if 'how can i make you happy' in query:
             speak("play quran for me sir. i will so appreciate")                                       

        if 'can you help me' in query:
             speak("of cours sir. what can i do for you")

        if 'do you love me' in query:
             speak("no sir im just your servant sir. im not your girl friend")

        elif 'i am sad' in query:
            music_dir = 'D:\\quran'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))     

        if 'i am happy today' in query:
             speak("nice to hear that sir")

        if 'goodbye' in query:
             speak("goodbye sir. hope i can see you soon")

        if 'hi' in query:
             speak("welcome boss")

        if 'who are you' in query:
             speak("im ochid sir. call me orchid. and im at your command at any time")
             
        if 'how old are you' in query:
             speak("i don't have age. im robot")

        if 'im in problem' in query:
             speak("how can i help you boss")  

        if 'call my best friend' in query:
             speak("im your best friend boss. that's why im working for you")  
        
        elif 'open discord' in query:
            discordPath = "C://Users//ABLM//AppData//Local//Discord//app-1.0.9002//discord"
            os.startfile(discordPath) 

        elif 'open Black Squad' in query:
            BlackSquadPath = "G://Steam//steamapps//common//Black Squad//binaries//win64//BlackSquadGame"
            os.startfile(BlackSquadPath)                                                

        elif 'open counter strike' in query:
            counterstrikePath = "G://Steam//steamapps//common//Counter-Strike Global Offensive//csgo"
            os.startfile(counterstrikePath)                                                
            
        elif 'open apex' in query:
            apexPath = "G://Steam//steamapps//common//Apex Legends//r5apex"
            os.startfile(apexPath)
            
        elif 'open logitech' in query:
            logitechpath = "C://Program Files//LGHUB//lghub"
            os.startfile(logitechpath)  

        elif 'open geforce' in query:
            geforcepath = "C://Program Files//NVIDIA Corporation//NVIDIA GeForce Experience//NVIDIA GeForce Experience"
            os.startfile(geforcepath)

        elif 'open itunes' in query:
            itunespath = " C:\Program Files\iTunes//iTnes"
            os.startfile(itunespath)

        elif 'open opera' in query:
            operapath = "C://Users//ABLM//AppData//Local//Programs//Opera//launcher" 
            os.startfile(operapath)

        elif 'open steam' in query:
            steampath = "G://Steam//steam"
            os.startfile(steampath)    

        elif 'open hand' in query:
            handpath = "C://Program Files//HandBrake//HnadBrake"
            os.startfile(handpath)    

        elif 'open lively' in query:
            livelypath = "C://Program Files (x86)//Lively Wallpaper//livelywpf"
            os.startfile(livelypath)

        elif 'open visual' in query:
            visualypath = "C://Users//ABLM//AppData//Local//Programs//Microsoft VS Code//code"
            os.startfile(visualypath)
    
       
    
