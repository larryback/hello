import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json



url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

res = requests.get(url)

with open("kma.xml", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "html.parser")
print("------------------------------------------------------------------------")
print(soup)
#title = soup.select('item title')
#print(title)
