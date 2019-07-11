import pyttsx3 as py3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import random
import smtplib
import time
#import pygame

engine=py3.init('sapi5')#In-built voice of microsoft speech API
print(engine)
#engine.say("My first code on text-to-speech") 
#engine.say("Thank you, Geeksforgeeks") 
voices=engine.getProperty('voices')
print('VOICE->',voices)
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Mr Sourav Nayak!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Mr Sourav Nayak!")
    else:
        speak("Good evening Mr Sourav Nayak!")

    speak("I am Just A Rather Very Intelligent System. You can also call me JARVIS. How may I help you sir??")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1 #seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold=400 #seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("User said",query)

    except Exception as e:
        #print(e)
        print("Say that again please..")
        return 'None'

    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("souravnayak.nayak@gmail.com","sourav36@3nayak8035")
    server.sendmail("saswat07@gmail.com",to,content)
    server.quit()    
    

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            wb.open("youtube.com")
        elif 'open google' in query:
            wb.open("google.com")
        elif 'open gmail' in query:
            wb.open("gmail.com")
        elif 'open geeksforgeeks' in query:
            wb.open("geeksforgeeks")
        elif 'play music' in query:
            #pygame.mixer.init()
            music_dir="D:\\My playlist\\Songs_BGM"
            songs= os.listdir(music_dir)
            print(songs)
            print(len(songs))
            '''playlist=list()
            for songs in songs:
                playlist.append(songs)
            print(playlist)
            SONG_END=pygame.USEREVENT+1
            pygame.mixer.music.load(playlist.pop())
            pygame.mixer.music.queue(playlist.pop())
            pygame.mixer.music.set_endevent(SONG_END)
            pygame.mixer.music.play()

            while True:
                for event in pygame.event.get():
                    if event.type==SONG_END:
                        if len(playlist)>0:
                            pygame.mixer.music.queue(playlist.pop())'''
            
            i=random.choice(range(0,len(songs)))
            for i in range(0,len(songs)):
                print(songs[i])
                os.startfile(os.path.join(music_dir,songs[i]))
                time.sleep(60)

        elif 'love me' in query:
            speak("Sorry sir, I'm not what you think me to be!!")
        elif 'why do you think so' in query:
            speak("A human is bounded to section 377, but I'm not sir. In any case, I can't give you the real pleasure of love.")
                
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strftime}")
        elif 'open code' in query:
            codePath="D:\\Python programs\\demo84.py"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("What should I say sir?")
                content=takeCommand()
                to="souravnayak.nayak@gmail.com"
                sendEmail(to,content)
                print("Email has been sent sir!")
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I couldnt send the mail.")
                
            
    
    #speak("I'm a starboy")
