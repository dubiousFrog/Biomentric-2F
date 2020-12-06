import gtts
import os
import speech_recognition as sr
from playsound import playsound
import webbrowser
from datetime import datetime
import win32com.client as wincl

#%%
'''
   // Voice Recognition (Speech-to-Text) - Google Speech Recognition API
   -> This API converts spoken text (microphone) into written text (Python strings)
   -> Personal or testing purposes only
   -> Generic key is given by default (it may be revoked by Google at any time)
   -> If using API key, quota for your own key is 50 requests per day
'''

def voice_out(answer):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(answer)



#%%

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
            audio = recognizer.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #   update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable/unresponsive"
            continue
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
            continue

        return response

#%%

def do_stuff(phrase):
    while True:
        answer = "sorry, i didn't get that" #don't have that answer stored in my tiny female brain, i should go back to the kitchen where i belong"
        recognizer = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        response = recognize_speech_from_mic(recognizer, mic)
        print (response["transcription"])
        request = response["transcription"]
       
        
        if response["transcription"] == "Hello computer" or response["transcription"] == "computer":
            now = datetime.now()  
            time = now.strftime("%H:%M")
            d = datetime.strptime(time, "%H:%M")
            timenow = d.strftime("%I:%M %p")
            answer = "Hello. It is now " + timenow + ", what would you like to do?"
        
        elif (response["transcription"].find("play") != -1 and response["transcription"].find("music") != -1) or response["transcription"] == "play some music":
            os.system("start chrome https://www.youtube.com/watch?v=utbxHliZqmg&ab_channel=ColterWall-Topic")
            answer = "OK"
       # elif response["transcription"].find("call") != -1 and response["transcription"].find("me") != -1:

        #elif response["transcription"].find("my") != -1 and response["transcription"].find("name")
         #   answer = myname
        else:
            os.system(request)
            answer = "OK!"
        voice_out(answer)
  #  print('\nSuccess : {}\nError   : {}\n\nText from Speech\n{}\n\n{}' \
  #        .format(response['success'],
  #                response['error'],
  #                '-'*17,
  #                response['transcription']))


    