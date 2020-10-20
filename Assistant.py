
import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon !")    
   
    else: 
        speak("Good Evening !")   
    assistname = 'James'
    speak("I am your Assistant ") 
    speak("there is still a lot of debate going over my name ")
    speak("But you can call me " + assistname + " for now")
      
  
def usrname(): 
    speak("What should i call you sir") 
    uname = takeCommand() 
    speak("Welcome" + uname) 
    columns = shutil.get_terminal_size().columns 

    speak("How can i Help you, Sir") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to Recognize your voice.")   
        return "None"
      
    return query 
   
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('your email id', 'your email passowrd') 
    server.sendmail('your email id', to, content) 
    server.close() 
if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
      
    clear() 
    wishMe() 
    usrname() 
      
    while True: 
          
        query = takeCommand().lower() 
          
        if 'open wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
        
        elif 'open youtube' in query: 
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")
            
  
        elif 'open google' in query: 
            speak("Here you go to Google") 
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
  
        elif 'play music' in query or "play song" in query: 
            speak("I am showing you songs") 
            
            # music_dir = "G:\\Song" 
            music_dir = "C:\\Users\\VINOD\\Music"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 
  
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("% H:% M:% S")     
            speak(f"Sir, the time is {strTime}") 
  
        elif 'open chrome' in query: 
            codePath = r"C:\Program Files (x86)\Google\Chrome\Application"
            os.startfile(codePath) 

        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'i am doing very fine' in query or "i am good" in query: 
            speak("It's good to know that") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assistname) 
            print("My friends call me Jason") 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by joshua.") 
              
        elif ' tell me a joke' in query: 
            speak(pyjokes.get_joke()) 
              
        elif "calculate" in query:  
              
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who am i" in query: 
            speak("If you talk then you are definetely a human.") 
  
        elif "how did you come into the world" in query: 
            speak("Thanks to esvin joshua. further It's a secret") 
  
        elif 'power point presentation' in query: 
            speak("opening Power Point presentatione") 
            power = r"C:\\Users\\VINOD\\Desktop\\JAMES.pptx"
            os.startfile(power) 
  
        elif 'What is love' in query: 
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in query: 
            speak("I am your virtual assistant created by Joshua") 
  
        elif 'what is the reason for your existence' in query: 
            speak("I was created as a Practice project by Master Joshua") 
  
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
            speak("Background changed succesfully") 
  
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how long do you want to stop me from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "James Camera ", "img.jpg") 
  
        elif "restart" or 'restart my computer' in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('James.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
  
        elif "update assistant" in query: 
            speak("I am constantly in contact with the servers of my creator and i am the latest version")
            print('contact with jos-es servers successful')
            print('assistant updated')
            
        # NPPR9-FWDCX-D2C8J-H872K-2YT43 
        elif assistname in query: 
              
            wishMe() 
            speak("James in your service Mister") 
         
  
        elif "what is the weather" in query: 
              
  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ") 
              
  
        elif "open wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A warm" + query) 
            speak("How are you")  
  
      
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about that,  you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you asked me that") 
  
        elif "what is" in query or "who is" in query: 
              
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
