from bs4 import BeautifulSoup
import requests
import urllib.parse as parse
import os.path as path


url = "https://blog.naver.com/korea_diary/221433346994"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

ifrs = soup.select('iframe#mainFrame')

for ifr in ifrs:
    print(ifr)
    print("---------------------")
    print(ifr.attrs['src'])