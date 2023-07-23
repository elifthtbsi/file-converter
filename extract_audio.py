import moviepy.editor

def extract_audio(video_name):
    video=moviepy.editor.VideoFileClip(video_name)
    audio=video.audio
    video_name=video_name.split(".")[0]
    audio.write_audiofile(video_name+".wav")

extract_audio("What’s the smartest age_ - Shannon Odell.mp4")
