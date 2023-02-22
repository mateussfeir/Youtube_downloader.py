import pytube
import os

def download_video(url, filepath):
    yt = pytube.YouTube(url)
    video = yt.streams.filter(file_extension='mp4').first()
    video.download(output_path=filepath)

user_input = input('Paste the link of the video you want to download: ')
url = user_input
filepath = os.path.join(os.path.expanduser('~'), 'Downloads')
download_video(url, filepath)
