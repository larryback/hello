import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv, codecs
import re
import pymysql


#url = "https://www.melon.com/chart/index.htm"
url = "http://vlg.berryservice.net:8099/melon/list"

    # heads = {
    #     "Referer": "https: // www.melon.com/chart/index.htm",
    #     "User-Agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    # }

#res = requests.get(url, headers=heads)

res = requests.get(url)
html = res.text

soup = BeautifulSoup(html, "html.parser")
trs = soup.select('div#tb_list table tbody tr[data-song-no]')
print(len(trs))
pattern = re.compile('(\d)')




for tr in trs:
    string = tr.select_one('div.wrap span.cnt')
    print("=========================================================================")
    print(string)
    exit()
    m1 = re.findall(pattern, string)
    print(m1)