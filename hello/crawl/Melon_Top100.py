from bs4 import BeautifulSoup
import urllib.request as req
import requests
url = "https://www.melon.com/chart/index.htm"

#soup = BeautifulSoup(html, 'html.parser')
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
print(res)

#a_list = soup.select("#lst50 > td > div > div > div > span > a")

#for a in a_list:
#    title = a.string
#    print(title)


url = "https://www.melon.com/chart/index.htm#params%5Bidx%5D=1"
resp = requests.get(url)
print (resp.status_code) # 200
print (resp.content)