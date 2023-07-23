import moviepy.editor
import speech_recognition as sr
from os import path
from pydub import AudioSegment


def extract_audio(video_name):
    video=moviepy.editor.VideoFileClip(video_name)
    audio=video.audio
    video_name=video_name.split(".")[0]
    audio.write_audiofile(video_name+".wav")

    return video_name


video="Why Having #fun Is the Secret to a Healthier Life #shorts.mp4"
audio_name=extract_audio(video)
file_name=audio_name
audio_name=audio_name+".wav"


r=sr.Recognizer()

with sr.AudioFile(audio_name) as source:
    audio=r.record(source)
    try:
        print("working on...")
        
        with open(file_name+".txt", "w") as export:
            export.write(r.recognize_google(audio))

    except:
        print("something went wrong")