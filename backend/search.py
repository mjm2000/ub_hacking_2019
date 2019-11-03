from googleapiclient.discovery import build

YT_ID = AIzaSyAap4qD61RlxjcseLvYoDhYpBojd84fSvI   
SERVICE = 'youtube'

YOUTUBE_API_VERSION = 'v3'


def yt_search(info):
    yt = build(YT_ID, SERVICE,developerKey=YT_ID)
