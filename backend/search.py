from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE = 'youtube'

API_VERSION = 'v3'


def yt_search(search_term):

    YT_ID = "AIzaSyAap4qD61RlxjcseLvYoDhYpBojd84fSvI"   
    yt = build( SERVICE,API_VERSION,developerKey=YT_ID)

    search_response = yt.search().list(
    q=search_term,
    part='id,snippet',
    maxResults=25
  ).execute()

    videos = {}
    channels = []
    playlists = []
    


    for search_result in search_response.get('items', []):
        ytus = "https://www.youtube.com/watch?v="
        if search_result['id']['kind'] == 'youtube#video':
            videos[search_result['snippet']['title']] = ytus + search_result['id']['videoId']
       # elif search_result['id']['kind'] == 'youtube#channel':
       #     channels.append('%s (%s)' % (search_result['snippet']['title'],
        #                           search_result['id']['channelId']))
       # elif search_result['id']['kind'] == 'youtube#playlist':
        #    playlists.append('%s (%s)' % (search_result['snippet']['title'],
        #                            search_result['id']['playlistId']))
    #returns videos access index 0 for vids  
    return videos
    
#print(yt_search("weezer"))
