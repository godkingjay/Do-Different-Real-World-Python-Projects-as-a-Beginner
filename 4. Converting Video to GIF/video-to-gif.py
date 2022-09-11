from moviepy.editor import *

video_dir = "video/"
gif_dir = "gif/"

video = VideoFileClip(f"{video_dir}video.mp4")
video.write_gif(f"{gif_dir}video-to-gif.gif")