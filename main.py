
import speech_recognition as sr
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random

warnings.filterwarnings('ignore')

def recordAudio():    
    # Record the audio
    r = sr.Recognizer()
    mic =sr.Microphone()
    with mic as source:  
       r.adjust_for_ambient_noise(source)
       print('Say something!')
       audio = r.listen(source)
       print('done')
    # Speech recognition using Google's Speech Recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand')
    except sr.RequestError as e:
        print('Request error from Google Speech Recognition')
    return data

def assistantResponse(text):
    print('response')
    print(text)
    # Convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)
     # Save the converted audio to a file    
    myobj.save('assistant_response.mp3')
    # Play the converted file
    os.system('start assistant_response.mp3')

def wakeWord(text):
    WAKE_WORDS = ['ok karen','hello karen'] 
    text = text.lower()  # Convert the text to all lower case words
  # Check to see if the users command/text contains a wake word    
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
  # If the wake word was not found return false
    return False

def greeting(text):
    # Greeting Inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello','ok']
     # Greeting Response back to the user
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']
     # If the users input is a greeting, then return random response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    # If no greeting was detected then return an empty string
    return ''



while True:
    # Record the audio
    text = recordAudio()
    response = '' #Empty response string
     
    # Checking for the wake word/phrase
    if (wakeWord(text) == True):
         # Check for greetings by the user
        response = response + greeting(text)
         # Check to see if the user said date
       
       # Assistant Audio Response
    assistantResponse(response)