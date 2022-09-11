# import Python Module
import moviepy.editor as me

audio_dir = "audio/"
video_dir = "video/"
filename = "mr-blue-sky-electric-light-orchestra-lyrics"

clip = me.VideoFileClip(f"{video_dir}{filename}.mp4");
clip.audio.write_audiofile(f"{audio_dir}{filename}.mp3")