from pymongo import MongoClient, DESCENDING
import requests, json
from bs4 import BeautifulSoup
from pprint import pprint

headers = {
    "X-Naver-Client-Id": "DJp53oSwPDBoa8kGI4tB",
    "X-Naver-Client-Secret": "VCL3gyA7wH"
}

# title = "Python"
title = "파이썬"

params = {
    "display": 20,
    "start": 1,
    "sort": "date",
    "query": title
   
}

#items = {
 #   "title":"title",
 #   "link":"link",
 #   "bloggername":"bloggername",
 #   "postdate":"postdate"
 #   }


# url = "https://openapi.naver.com/v1/search/book.json"
url = "https://openapi.naver.com/v1/search/book"
# url = "https://openapi.naver.com/v1/search/image"
html = requests.get(url, params=params, headers=headers).text
#print("______________________________________________________________________________________________________________")
#print(html)
#items = html['items']





jsonData = json.loads(html)
items = jsonData['items']

pprint(items)
exit()
mongo_client = MongoClient('localhost', 27017)
collection = mongo_client.dooodb.Books

result = collection.insert_many(items)
print('Affected docs is {}'.format(len(result.inserted_ids)))
lst = collection.find().sort('likecnt', DESCENDING).limit(5)





result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

#print(json.dumps(jsonData, ensure_ascii=False, indent=2))
#exit()




jsonData = json.loads(html)
items = jsonData['items']
Blogger = []
for item in items:
    # print ("title: " , item['title'])
    # print ("link: " , item['link'])
    # print ("bloggername: ", item['bloggername'])
    # print ("postdate: ", item['postdate'])
    bloggerID = re.sub(e, "", item['bloggerlink'])
    #print(bloggerID)
    #exit()
    Blogger.append([item['bloggerID'], item['bloggername'], item['bloggerlink']])
    #print(lst)
    exit()