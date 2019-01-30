from apiclient.discovery import build
from pprint import pprint
from pymongo import MongoClient, DESCENDING
from pprint import pprint

API_KEY = "AIzaSyDZXPBytbLkh4IWwMtc5ZoRian-J77M_7s" 
youtube = build('youtube', 'v3', developerKey=API_KEY)

search_res = youtube.search().list(
    part='snippet',
    q='시니어코딩',
    type='video',
    maxResults = 50
).execute()

for item in search_res['items']:
    #pprint(item)
    #print(len(search_res['items']))


# mongo_client = MongoClient('localhost', 27017)
# collection = mongo_client.dooodb.Youtube

# result = collection.insert_many(items)
# print('Affected docs is {}'.format(len(result.inserted_ids)))
# lst = collection.find().sort('likecnt', DESCENDING).limit(10)
