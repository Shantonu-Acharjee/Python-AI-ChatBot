from playsound import playsound
from gtts import gTTS
import os


def GttsText(YourText):
    FilePath = 'GttsDemo.mp3'
    your_text = gTTS(YourText, lang='en-in') # Change Language from Hare ------------------------------------- Lang
    your_text.save(FilePath)
    playsound(FilePath)
    os.remove(FilePath)