from __future__ import unicode_literals
import youtube_dl 


def download_vid(file):
    yt_info ={
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(yt_info) as ydl:
        ydl.download(file)


download_vid(["https://www.youtube.com/watch?v=ENXvZ9YRjbo"])
    
    
