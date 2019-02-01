import requests, json
from bs4 import BeautifulSoup

url = "https://openapi.naver.com/v1/search/book.json"

title = "파이썬"
params = {
    "query": title,
    "display": 20,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "h8D7yhnqUBsVaCHQOViJ",
    "X-Naver-Client-Secret": "TYwzilDXGl"
}

result = requests.get(url, params=params, headers=headers).text

jsonData = json.loads(result)

str = json.dumps(jsonData, ensure_ascii=False, indent=2)

with open('./n_research_result.json', 'w+') as json_file:
    json.dump(jsonData, json_file)





#print(json.dumps(jsonData, ensure_ascii=False, indent=2))

# for item in jsonData['items']:
#     item['']