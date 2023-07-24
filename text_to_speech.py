from gtts import gTTS
import os

file_name="Why Having #fun Is the Secret to a Healthier Life #shorts.txt"

def text_to_speech(file_name):

    with open (file_name, "r") as mytext:
        mytext=mytext.read()
        
        audio=gTTS(text=mytext, lang="en", slow=False)
        file_name=file_name.split(".")[0]
        audio.save(file_name+".mp3")
        os.system("start"+file_name+".mp3")

text_to_speech(file_name)