# JARVIS program

# Import modules
import pyttsx3  # for TTS
import speech_recognition as sr  # For Speech Recognition
import datetime  # For finding the Date
import time  # for finding the time
import cv2  # for opening camera and taking photos
import random  # for piking random responses
import os  # for accessing and opering on the Operating System
import sys  # Used to consle the entire System as a whole
import winsound  # for playing sound files using wav file formats on Windows
import requests  # for finding IP Address
from requests import get  # use the get function
import wikipedia  # for gettingh results from wikipedia
import webbrowser  # To Open Links to specific web pages in the default web browser
import pywhatkit  # to Send messages on Whats App andďto open videos on YouTube
import smtplib  # for sending emails and performing other SMTP functions


# Global Variables
botname = "JARVIS"

# initialize tts engine
engine = pyttsx3.init()


def SpeakOutput(message):
    # function fot perform Text to speech
    engine.say(message)
    print(message)
    engine.runAndWait()


def TakUserInput():
    # function to take input form user
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("listening...")
        winsound.PlaySound('sound\Speech On.wav', winsound.SND_ASYNC)
        r.pause_threshold = 1
        audio = r.listen(source=mic, timeout=1, phrase_time_limit=60)
        try:
            winsound.PlaySound('sound\Speech Off.wav', winsound.SND_ASYNC)
            UserQuery = r.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            SpeakOutput("Say that again")
            return "none"
        except sr.RequestError:
            SpeakOutput("Say that again")
    return UserQuery


def Greetings():
    # Function to greet the user depending on the time of day
    hour = int(datetime.datetime.now().hour)

    if (hour >= 8 and hour < 12):
        SpeakOutput("Good Morning "+os.getlogin())
        print("Good Morning "+os.getlogin())
    elif (hour >= 12 and hour < 18):
        SpeakOutput("Good Afternoon "+os.getlogin())
        print("Good Afternoon "+os.getlogin())
    else:
        SpeakOutput("Good Evening "+os.getlogin())
        print("Good Evening "+os.getlogin())
    SpeakOutput("I am "+botname+" How may I help you")


def TakePhoto():
    # Function to open camera and take a photo
    webcam = cv2.VideoCapture(0)

    imageCounter = 0
    flag = True
    while flag:
        ret, frames = webcam.read()
        if not ret:
            print("Failed to grab image")
            SpeakOutput("Failed to Capture")
            flag = False
            break
        cv2.imshow("Image Capture Window", frames)

        # Close webcame when presing the ESC key
        k = cv2.waitKey(50)

        # Take Screenshort when space key is pressed
        if k == 32:
            imagename = f"image_{imageCounter}.png"
            winsound.PlaySound('sound\camera-shutter.wav', winsound.SND_ASYNC)
            cv2.imwrite(imagename, frames)
            print("Image Captured")

            imageCounter += 1
        # CLose the camera when ESC key is pressed
        elif k == 27:
            webcam.release()
            cv2.destroyAllWindows()
            ret = False
            break

# Open Applications


def OpenCMD():
    path = "C:\\Windows\\system32\\cmd.exe"
    os.startfile(path)


def OpenChome():
    path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(path)

# Get info form Internet


def GetSystemIPAddress():
    ip = get("https://api.ipify.org").text
    SpeakOutput(f"Your Public IP Address is {ip}")


def Searchwikipedia(query):
    SpeakOutput("Searching wikipedia")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=5)
    SpeakOutput("According to wikipedia...")
    SpeakOutput(result)


def OpenYouTube():
    webbrowser.open_new_tab('youtube.com')


def OpenAmazon():
    webbrowser.open_new_tab('https://www.amazon.in/')


def GoogleSearch():
    webbrowser.open_new_tab("google.com")


def GetUserAccountName():
    SpeakOutput(os.getlogin())

# Send message using WhatsApp


def SendWhatsAppMessage():
    SpeakOutput("Enter Phone Number with Country Code")
    phoneno = input("Enter Phone Number with Country Code")

    SpeakOutput("Speek the Message that you want to send")
    message = TakUserInput()

    pywhatkit.sendwhatmsg_instantly(phoneno, message)
    print("Message Sent")
    SpeakOutput(message+" was sent Successfully to "+phoneno)


def PlayVidoesOnYouTube():
    SpeakOutput("Mention the name of the Video to Play")
    VideoName = TakUserInput()
    pywhatkit.playonyt(VideoName)
    SpeakOutput("Sure Playing "+VideoName + " from Youtube")


# Get Date and Time from System
def FetchYear():
    current_time = datetime.datetime.now()
    year = current_time.year
    SpeakOutput("The Current Year is "+str(year))


def FetchMonth():
    current_time = datetime.datetime.now()
    month = current_time.month
    if month == 1:
        SpeakOutput("The Current Month is January")
    elif month == 2:
        SpeakOutput("The Current Month is February")
    elif month == 3:
        SpeakOutput("The Current Month is March")
    elif month == 4:
        SpeakOutput("The Current Month is April")
    elif month == 5:
        SpeakOutput("The Current Month is May")
    elif month == 6:
        SpeakOutput("The Current Month is June")
    elif month == 7:
        SpeakOutput("The Current Month is July")
    elif month == 8:
        SpeakOutput("The Current Month is Augest")
    elif month == 9:
        SpeakOutput("The Current Month is September")
    elif month == 10:
        SpeakOutput("The Current Month is October")
    elif month == 11:
        SpeakOutput("The Current Month is November")
    elif month == 12:
        SpeakOutput("The Current Month is Descember")


def FetchDay():
    weekday = datetime.datetime.now().weekday()
    if weekday == 0:
        SpeakOutput("The Current Date is Monday")
    elif weekday == 1:
        SpeakOutput("The Current Date is Tuesday")
    elif weekday == 2:
        SpeakOutput("The Current Date is Wednessday")
    elif weekday == 3:
        SpeakOutput("The Current Date is Thirsday")
    elif weekday == 4:
        SpeakOutput("The Current Date is Friday")
    elif weekday == 5:
        SpeakOutput("The Current Date is Saturday")
    elif weekday == 6:
        SpeakOutput("The Current Date is Sunday")


def FetchDate():
    current_time = datetime.datetime.now()


Greetings()

query = TakUserInput().lower()

if "command prompt" in query:
    SpeakOutput("Sure")
    OpenCMD()
elif "cmd" in query:
    SpeakOutput("Sure")
    OpenCMD()

elif "google chrome" in query:
    SpeakOutput("Sure")
    OpenChome()
elif "chrome" in query:
    SpeakOutput("Sure")
    OpenChome()
elif "camera" in query:
    SpeakOutput("Sure Press ESC to close and Space to Capture")
    TakePhoto()
elif "what is my ip" in query:
    SpeakOutput("Sure")
    GetSystemIPAddress()
elif "wikipedia" in query:
    Searchwikipedia(query=query)
elif "youtube" in query:
    SpeakOutput("Sure Opening YouTube")
    OpenYouTube()
elif "amazon" in query:
    SpeakOutput("Sure Opening Amazon India")
    OpenAmazon()
elif "google" in query:
    GoogleSearch()
elif "whatsapp" in query:
    SendWhatsAppMessage()
elif "online video" in query:
    PlayVidoesOnYouTube()

elif "day" in query:
    FetchDay()
elif "month" in query:
    FetchMonth()
elif "year" in query:
    FetchYear()

elif "no thinks " in query:
    SpeakOutput("Thank You for using "+botname+" Have a good day")
    sys.exit()
