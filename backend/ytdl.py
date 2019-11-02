from __future__ import unicode_literals
import youtube_dl 
#from playsound import playsound
#import html.parser.HTMLParser

title = get_desc['title']


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def download_vid(file):
    #arguments for downloading 
    yt_info ={
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        
    }]
    #downloaded  
    }

    with youtube_dl.YoutubeDL(yt_info) as ydl:
        ydl.download(file)
        
def get_desc(file):
    meta = ""
    yt_info = {}
    with youtube_dl.YoutubeDL(yt_info) as ydl:
        meta = ydl.extract_info(file,download=False)
    return meta

url ="https://www.youtube.com/watch?v=ENXvZ9YRjbo"  
url_list= [url]
#download_vid(url)

info = get_desc(url)

for thing in info: 
    print(thing)


