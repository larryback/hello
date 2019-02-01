import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import urllib.request
import urls
import urllib.parse as parse
import os.path as path
import time
from selenium import webdriver

url = "https://www.melon.com/chart/index.htm"

heads = {
    "Referer": "https: // www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}



res = requests.get(url, headers=heads)
html = res.text

soup = BeautifulSoup(res.text, "html.parser")

sel = "#lst100 > td > div > a > img"

imgs = soup.select(sel)




imgs = soup.select(sel)
# print(imgs, len(imgs))

if len(imgs) < 1:
    exit()


print("--------------------------------------")

for i, img in enumerate(imgs):
    src = img.get('src')
    print("img>>", src)
    # with open("./images/" + urls.getFilename(src), "wb") as file:
    with open("./images01/" + str(i + 1) + '.jpg', "wb") as file:
        file.write(requests.get(src).content)

