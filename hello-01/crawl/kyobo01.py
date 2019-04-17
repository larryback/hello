from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf"

#soup = BeautifulSoup(html, 'html.parser')
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
#print(res)

a_list = soup.select("#main_contents > ul > li > div > div > a > strong")

for a in a_list:
    title = a.string
    print(title)


