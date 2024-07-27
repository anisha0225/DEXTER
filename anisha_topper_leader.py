from msilib.schema import SelfReg

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
from bs4 import BeautifulSoup
import sys
import pyjokes 
import pyautogui 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from os import startfile
from pyautogui import click,press
from keyboard import write
from time import sleep 
from keyboard import press 
import pywhatkit as kit
import operator  
import random
import json





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait() 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3,phrase_time_limit=5)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again pease...") 
        return"none"
        
    return query   

def wishMe():
    hour = int(datetime.datetime.now().hour) 

    if hour>=0 and hour<=12:
        speak("good morning")

    elif hour>12 and hour<18:
        speak("good evening") 

    else:
        speak("good evening")

    strtime = datetime.datetime.now().strftime("%H: %M: %S") 
    speak(f"Sir,the time is {strtime}")  


    speak("i am dexter sir,please tell me how may i help you?") 






def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mousumisarkar422002@gmail.com' , 'guria@200025')
    server.sendmail('moisumisarkar422002@gmail.com' , to,content)
    server.close

def _init_(self, query):
    #self
    self.query = query    


    def run(self):
        self.TaskExecution 



   


Hello = ('hello','hi','hey')
reply_Hello = ('hello there how are you',
                'hello I am Dexter',
                'hi how can I help you',
                'hey there its good to see you again')

Bye = ('goodbye','bye','see you later','exit')
reply_Bye = ('ok friend see you later',
            'goodbye have a good time',
            'thanks for using me , have a good day'
            )

How_are_you = ('how are you')
reply_How_are_you = ('I am fine and I hope you are fine as well',
                    'I am fine',
                    'I am good',
                    'Absolutely fine')

Nice = ('good','nice','thanks')
reply_Nice = ('Thanks'
            'you are welcome'
            "no problem")

have_a_relax = ('have a relax')
reply_have_a_relax =('see you not for mind')

Functions = ('funtions','abilities','what can you do','features',)
reply_funtions = ('just tell me what to do and you will see')

reply_sorry = ('Sorry but I am not programmed for this',
                'sorry I have no information regarding this')


def Chatbotfunc(Text):

    Text = str(Text)
  
    for word in Text.split():
            if word in Hello:
               reply = random.choice(reply_Hello)
               return reply
                
            elif word in Bye:
                reply = random.choice(reply_Bye)
                return reply
                
            elif word  in How_are_you:
                reply= random.choice(reply_How_are_you)
                return reply

            elif word in Nice:
                reply= random.choice(reply_Nice)
                return reply
            
            elif word in Functions:
                reply = random.choice(reply_funtions)
                return reply

            elif word in have_a_relax:
                reply = random.choice(reply_have_a_relax)
                return reply
            else:
                reply= random.choice(reply_sorry)
                return reply


def TaskExe():
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system('start cmd')  

        elif 'open camera' in query: 
            cap = cv2.VideoCapture(0)  
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img) 
                k = cv2.waitKey(50)
                if k==27:
                 break
            cap.release()
            cv2.destroyAllWindows() 

        elif 'open code' in query:
           codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
           os.startfile(codePath) 

        elif 'music' in query:
            music_dir = "D:\\musics" 
            songs = os.listdir(music_dir) 
            rd = random.choice(songs)  
            os.startfile(os.path.join(music_dir, rd)) 

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text  
            speak(f"your IP adress is {ip}")  

        elif "wikipedia" in query: 
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia..")
            speak(results)
            print(results)  

        elif "open youtube" in query:
            webbrowser.open("youtube.com")


        elif "open stackoverflow" in query: 
            webbrowser.open("stackoverflow.com")

        elif "open facebook" in query: 
            webbrowser.open("facebook.com")

        elif "google search" in query: 
            speak("sir,what should i search in google??")
            b = takeCommand().lower()
            webbrowser.open(f"{b}") 

        
        elif 'youtube search' in query:
            Query = query.replace("dexter", "")   
            query = Query.replace("youtubeSearch", "")
            result = "https://www.youtube.com/results?search_query=" + query 

            webbrowser.open(result)

            speak("this is the results sir!")

            pywhatkit.playonyt(query)

            speak("this may help you sir!")  

        elif "you can sleep" in query:
            speak("thanks for using me sir, have a good day")     


        elif "news" in query:

             main_url = 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'
             main_page = requests.get(main_url).json()
             print(main_page)    
             articles = main_page["articles"]
             print(articles)
             head = []
             day = ["first", "second", "third", "fourth" , "fifth", "sixth", "seventh", "eigth", "ninth", "tenth"]
             for ar in articles:
              head.append(ar["title"])
             for i in range (len(day)):
              print(f"today's {day[i]} news is: {head[i]}")  
              speak(f"today's {day[i]} news is: {head[i]}")
            

      

        elif "email to anisha" in query:
            try:
                speak("what should i say??")
                content = takeCommand().lower()
                to = "anisha2002sarkar@gmail.com"
                sendEmail(to,content)
                speak("email has been sent") 

            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send this email") 

        
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke) 

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5") 

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0") 

        elif "where I am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i think we are in {city} city of {country} country")

            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are")
                pass


        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            import psutil 
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"sir our system have {percentage} percent battery")

        elif "net speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")



        elif "no thanks" in query:
           speak("thanks for using me sir, have a good day")
           sys.exit()

        #speak("sir,do you have any other work??")    
           
        elif "do some calculations" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("say what do you want to calculate, example: 4 plus 5")
                print("listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    'x' : operator.mul, #multiplied by
                    '/' : operator.truediv, #divided
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2) 
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))

        else:
            from anisha_topper_leader import Chatbotfunc
            reply = Chatbotfunc(query)
            speak(reply)


TaskExe()