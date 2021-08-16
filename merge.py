# Import everything needed to edit video clips
from moviepy.editor import *


# loading video dsa gfg intro video
clip = VideoFileClip("recording.mp4")


# getting only first 5 seconds
clip = clip.subclip(0, 5)

# loading audio file
audioclip = AudioFileClip("recording.mp3").subclip(0, 5)

# adding audio to the video clip
videoclip = clip.set_audio(audioclip)

# showing video clip
videoclip.write_videofile("merged.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')
