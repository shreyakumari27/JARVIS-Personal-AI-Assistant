
# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
# while 1:
#     print("Enter the word you want to speak it out by computer")
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.pause_threshold = 1
#         audio = r.listen(source)
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}")
#         return query
#
#     s = input()
#     speaker.Speak(s)
# import speech_recognition as sr
# import os
# import webbrowser
# # import openai
# import win32com.client
#
# def say(text):
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     speaker.Speak(text)
#     # os.system(f"say {text}")
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             print("Recognizing...")
#             queue = r.recognize_google(audio, language='en-in')
#             print(f"user said: {query}")
#             return query
#         except Exception as e:
#             return "Some Error Occurred.  Sorry from Jarvis"
#
#
# if __name__ == "__main__":
#     print('PyCharm')
#     say('Hello I am Jarvis A.I')
#     while True:
#         print("Listening...")
#         query = takeCommand()
#         sites = [["youtube.com", "https://www.youtube.com"],["facebook.com", "https://www.facebook.com"],["google.com", "https://www.google.com"],]
#         for site in sites:
#             if f"open {site[0]}".lower() in query.lower():
#                 say(f"Opening {site[0]} sir...")
#                 webbrowser.open(site[1])
#         # say(query)


# import speech_recognition as sr
# import os
# import webbrowser
# import win32com.client
# from datetime import datetime
#
#
# def say(text):
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     speaker.Speak(text)
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source, timeout=5, phrase_time_limit=10)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             print("Error:", e)
#             return "Some Error Occurred. Sorry from Jarvis"
#
# if __name__ == "__main__":
#     print('PyCharm')
#     say('Hello, I am Jarvis A.I.')
#     while True:
#         query = takeCommand().lower()
#         sites = [
#             ["youtube", "https://www.youtube.com"],
#             ["facebook", "https://www.facebook.com"],
#             ["google", "https://www.google.com"]
#         ]
#         for site in sites:
#             if f"open {site[0]}" in query:
#                 say(f"Opening {site[0]}, Shreya...")
#                 webbrowser.open(site[1])
#             if "the time" in query:
#                 strfTime = datetime.now().strftime("%H:%M:%S")
#                 say(f"The time is {strfTime}")

# import speech_recognition as sr
# import os
# import webbrowser
# import win32com.client
#
# def say(text):
#     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     speaker.Speak(text)
#
# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source, timeout=5, phrase_time_limit=10)
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print(f"User said: {query}")
#             return query
#         except Exception as e:
#             print("Error:", e)
#             return "Some Error Occurred. Sorry from Jarvis"
#
# if __name__ == "__main__":
#     print('PyCharm')
#     say('Hello, I am Jarvis A.I.')
#     while True:
#         query = takeCommand().lower()
#
#         sites = [
#             ["youtube", "https://www.youtube.com"],
#             ["facebook", "https://www.facebook.com"],
#             ["google", "https://www.google.com"]
#         ]
#         for site in sites:
#             if f"open {site[0]}" in query:
#                 say(f"Opening {site[0]}, sir...")
#                 webbrowser.open(site[1])
#
#         if "open music" in query:
#             musicPath = r"C:\Users\SHREYA KUMARI\Downloads\GxL - MONTAGEM INDIA [NCS Release].mp3"
#             if os.path.exists(musicPath):
#                 say("Playing your music, sir.")
#                 os.startfile(musicPath)
#             else:
#                 say("Sorry sir, I could not find the music file.")


import speech_recognition as sr
import os
import webbrowser
import win32com.client
from datetime import datetime
import random


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == "__main__":
    print('PyCharm')
    say('Hello, I am Jarvis A.I.')
    music_dir = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\GxL - MONTAGEM INDIA [NCS Release].mp3"

    while True:
        query = takeCommand().lower()

        # List of sites
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["facebook", "https://www.facebook.com"],
            ["google", "https://www.google.com"]
        ]

        # Open websites
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]}, Shreya...")
                webbrowser.open(site[1])
                break  # so it doesn’t loop again unnecessarily

        # Tell the time
        if "the time" in query:
            strfTime = datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        # 🎵 Play music feature
        elif "play music" in query or "play song" in query:
            say("Playing music, Shreya...")
            try:
                songs = os.listdir(music_dir)
                if songs:
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_dir, song))
                    print(f"Playing: {song}")
                else:
                    say("No songs found in your music folder.")
            except Exception as e:
                print("Error playing music:", e)
                say("Sorry, I couldn’t play music.")

        # Exit condition
        elif "stop" in query or "exit" in query or "quit" in query:
            say("Goodbye Shreya, see you soon!")
            break

