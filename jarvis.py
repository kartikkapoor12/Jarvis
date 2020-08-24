import pyttsx3   
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib




engine=pyttsx3.init('sapi5') # Microsoft API to take voice
voices = engine.getProperty('voices')
#print(voices[0].id)    
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good Morning User")   
    elif hour>=12 and hour<18:
        speak("Good Afternoon User") 
    else:
        speak("Good Evening User")
    speak("I am Jarvis Sir! How may I help you")

def take():
    '''Takes the voice input from the user
     and return string output '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio,language='en-in')
        print("User said: ",query)

    except Exception as e:
       # print(e)
        print("Say that again please...")    
        return "None"
    return query

def sendEmail(to,content):
    # We will be using SMTPlib
    # add the less security app in gmail
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com','your_password')
    server.sendmail('your_email@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
   wishMe()
   while True: 
       query = take().lower()   # so that the query can match easily 
        # Logic based on query 


     # Wikipedia command
       if 'wikipedia' in query:

         speak("Searching in Wikipedia sir...")
         query = query.replace("wikipedia","")
         result = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia")
         print(result)
         speak(result)



     # Hello command
       elif 'hello' in query:
           speak("Hello sir!")


     # How Are you Command
       elif 'how are you' in query:
           speak('i am pretty awesome User you say wassup!')
           take()
           speak('thats pretty good, So tell me how may I help you')
      
      
     # Google Classroom Command
       elif 'classroom' in query:
           speak ("Opening your Google Classroom")
           webbrowser.open("https://classroom.google.com/u/2/h")    
      

     # Youtube command
       elif 'youtube' in query:
           speak('What do you want to open in Youtube Sir !')
           text=take()
           speak("Opening song list on youtube sir!")
           webbrowser.open("https://www.youtube.com/results?search_query="+text)



     # Google command
       elif  'open google' in query:

           speak('What do you want to open in Google Sir !')
           text=take()
           speak("Opening Google search sir!")
           webbrowser.open("https://www.google.com/?#q="+text)



     # Play song from playlist command
       elif 'play a song' in query:
           speak('Opening Song')
           path="C:\\Users\\tanvi\\OneDrive\\Desktop\\JARVIS AI project\\Maroon.mp3"  # Enter your song path      
           os.startfile(path)


     # Time command
       elif 'time' in query: 
           strtime=datetime.datetime.now().strftime("%H:%M:%S")
           speak("Sir, the time is ")
           speak(strtime)


     # Android Studio command       
       elif 'android studio' in query :

           speak("Opening Android Studio sir!")
           path= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio\\Android Studio.exe"      # Enter the path 
           os.startfile(path)


     # Visual Studio command        
       elif 'visual studio code' in query:
            speak("Opening Visual Studio sir!")
            path="C:\\Users\\tanvi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"                       # Enter the path 
            os.startfile(path)    
            

     # Sending Mail command  
       elif 'send an email' in query:
           try:
               speak("What should I  mail")
               content=take()
               speak("confirm me ! do you want to send this message")
               a= take()
               if 'yes'or 'yes jarvis' or ' sure' in a:
                   to="email@gmil.com"
                   sendEmail(to,content)
                   speak("Email has been sent")
               else:
                   speak("Email Declined")    
           except Exception as e:
               #print(e)
               speak("Sorry User ! the mail was not able to sent right now")
               print("Mail not sent!")    
    
    
     # Quit Command
       elif 'quit' in query:
           speak("Goodbye User, pleasure to talking you")
           exit()        

               



            
 
