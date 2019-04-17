import requests, json
from bs4 import BeautifulSoup


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
url = "https://openapi.naver.com/v1/search/blog"
# url = "https://openapi.naver.com/v1/search/image"
html = requests.get(url, params=params, headers=headers).text
#print("______________________________________________________________________________________________________________")
#print(html)
#items = html['items']





jsonData = json.loads(html)
items = jsonData['items']

print(items)
exit()

for item in items:
    print ("title: " , item['title'])
    print ("link: " , item['link'])
    print ("bloggername: ", item['bloggername'])
    print ("postdate: ", item['postdate'])

#print(json.dumps(jsonData, ensure_ascii=False, indent=2))

