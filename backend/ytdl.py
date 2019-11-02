from __future__ import unicode_literals
import youtube_dl 
from playsound import playsound
#from playsound import playsound
#import html.parser.HTMLParser

#title = get_desc['title']


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def download_vid(url):
    url_list = [url] 
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
        ydl.download(url_list)
        
def get_desc(file):
    meta = {}
    yt_info = {}
    with youtube_dl.YoutubeDL(yt_info) as ydl:
        meta = { file:ydl.extract_info(file,download=False)}
    return meta


def sort(urls,sort_type ,criteria):
    for url in urls.values:
        print(url) 

url ="https://www.youtube.com/watch?v=ENXvZ9YRjbo"  
url_list= [url]
download_vid(url)

info = get_desc(url)

print (info[url]['title'])
    

