from apiclient.discovery import build
from pprint import pprint

API_KEY = "AIzaSyDZXPBytbLkh4IWwMtc5ZoRian-J77M_7s" 
youtube = build('youtube', 'v3', developerKey=API_KEY)

search_res = youtube.search().list(
    part='snippet',
    q='파이썬',
    type='video',
    maxResults = 50
).execute()

for item in search_res['items']:
    pprint(item)
    print(len(search_res))