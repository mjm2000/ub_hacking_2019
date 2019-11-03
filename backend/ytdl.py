from __future__ import unicode_literals
import youtube_dl 
from operator import itemgetter, attrgetter, methodcaller
#from playsound import playsound
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

def download_vid(url,name):
    url_list = [url] 
    #arguments for downloading 
    yt_info ={
    'format': 'bestaudio/best',
    'outtmpl': 'data/' + name + ".mp3" ,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        
    }]

    #downloaded  
    }
    
    with youtube_dl.YoutubeDL(yt_info) as ydl:
        ydl.download(url_list)
    return "data/" + name + ".mp3"
        
def get_desc(url,name):
    meta = {}
    yt_info = {}
    filePath = download_vid(url, name)  
    with youtube_dl.YoutubeDL(yt_info) as ydl:
        meta = { filePath : ydl.extract_info(url,download=False)}
    return meta


def sort(urls,criteria):
    uul = {}
    for url_map in urls: 
        uul.update(get_desc(url_map))  
        
    oul = {}
    
    for url in uul:
        element_type = uul[url][criteria]
        if element_type in oul:
           element_type = oul[url][criteria]
           oul[element_type] += url
        else: 
           oul[element_type] = [url ] 
    return oul 
def sort_tags(urls):
    #unorder list 
    uul = {}
    for url_map in urls:
        #adds all the meta data of urls into a map
        uul.update(get_desc(url_map))  
    oul = {}
    
    for url in uul:
        tags = uul[url]['tags']
        for tag in tags:
            if tag in oul:
                oul[tag] += url
            else:
                oul[tag] = url 

    return oul 



#url1 ="https://www.youtube.com/watch?v=ENXvZ9YRjbo"  
#url2 ="https://www.youtube.com/watch?v=gGdGFtwCNBE" 

#download_vid(url1,"bevboys.mp3")


#for file1 in info:
     
 #       print(info[file1]['tags'])
   #   print( info[url1][file1] ) 

#print(sort(url_list,'title' ))


#print(info[url]['title'])
    

